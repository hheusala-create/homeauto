import csv
import ipaddress
import json
import socket
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime
from urllib.parse import urljoin

import requests

REQUEST_TIMEOUT = 10
CONNECT_TIMEOUT = 4
MAX_WORKERS = 4
RETRIES = 3


def prompt_subnet():
    subnet = input("Enter subnet (e.g. 10.107.1.0/24): ").strip()
    if not subnet:
        subnet = "10.107.1.0/24"
    return subnet


def safe_get(url, attempts=RETRIES):
    last_error = ""
    for attempt in range(attempts):
        try:
            response = requests.get(url, timeout=(CONNECT_TIMEOUT, REQUEST_TIMEOUT))
            return response, last_error
        except Exception as exc:
            last_error = str(exc)
            time.sleep(0.2)
    return None, last_error


def try_resolve_hostname(ip):
    try:
        return socket.gethostbyaddr(ip)[0]
    except Exception:
        return ""


def detect_shelly(ip):
    base_url = f"http://{ip}/"

    result = {
        "ip": ip,
        "hostname": try_resolve_hostname(ip),
        "is_shelly": False,
        "generation": "",
        "device_type": "",
        "model": "",
        "name": "",
        "mac": "",
        "firmware": "",
        "detected_by": "",
        "notes": "",
    }

    checks = [
        ("rpc/Shelly.GetDeviceInfo", "gen4_rpc"),
        ("shelly", "gen1_shelly"),
        ("settings", "gen1_settings"),
        ("status", "gen1_status"),
    ]

    for endpoint, label in checks:
        response, error_text = safe_get(urljoin(base_url, endpoint))

        if response is None:
            if error_text:
                result["notes"] = error_text
            continue

        if response.status_code == 401:
            result["notes"] = f"Auth required on {endpoint}"
            continue

        if response.status_code != 200:
            result["notes"] = f"HTTP {response.status_code} on {endpoint}"
            continue

        try:
            data = response.json()
        except Exception:
            data = None

        if endpoint == "rpc/Shelly.GetDeviceInfo" and isinstance(data, dict):
            if data.get("app") or data.get("gen") or data.get("id"):
                result["is_shelly"] = True
                result["generation"] = f"Gen{data.get('gen', '')}" if data.get("gen") else "Gen4"
                result["device_type"] = str(data.get("app", ""))
                result["model"] = str(data.get("model", ""))
                result["name"] = str(data.get("name") or data.get("id") or "")
                result["mac"] = str(data.get("mac", ""))
                result["firmware"] = str(data.get("ver", ""))
                result["detected_by"] = label
                return result

        if endpoint == "shelly" and isinstance(data, dict):
            if data.get("type") or data.get("mac"):
                result["is_shelly"] = True
                result["generation"] = "Gen1"
                result["device_type"] = str(data.get("type", ""))
                result["model"] = str(data.get("model", ""))
                result["name"] = str(data.get("name", ""))
                result["mac"] = str(data.get("mac", ""))
                result["firmware"] = str(data.get("fw", ""))
                result["detected_by"] = label
                return result

        if endpoint == "settings" and isinstance(data, dict):
            device = data.get("device", {})
            if isinstance(device, dict) and (device.get("type") or device.get("mac")):
                result["is_shelly"] = True
                result["generation"] = "Gen1"
                result["device_type"] = str(device.get("type", ""))
                result["model"] = str(device.get("hostname", ""))
                result["name"] = str(device.get("hostname", ""))
                result["mac"] = str(device.get("mac", ""))
                result["firmware"] = str(data.get("fw", ""))
                result["detected_by"] = label
                return result

        if endpoint == "status" and isinstance(data, dict):
            if any(k in data for k in ["wifi_sta", "cloud", "mqtt", "time"]):
                result["is_shelly"] = True
                result["generation"] = "Gen1?"
                result["detected_by"] = label
                result["notes"] = "Detected by /status only"
                return result

    return result


def scan_subnet(subnet):
    network = ipaddress.ip_network(subnet, strict=False)
    hosts = [str(ip) for ip in network.hosts()]

    print(f"Scanning {len(hosts)} IPs...\n")

    results = []

    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        futures = [executor.submit(detect_shelly, ip) for ip in hosts]

        done = 0
        for f in as_completed(futures):
            done += 1
            r = f.result()
            results.append(r)

            if r["is_shelly"]:
                print(f"{r['ip']} | {r['device_type'] or '-'} | {r['name'] or '-'} | {r['generation']} | {r['detected_by']}")
            elif done % 20 == 0:
                print(f"Checked {done}/{len(hosts)}")

    return results


def save_results(results):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    json_file = f"data/raw/shelly_scan_{timestamp}.json"
    csv_file = f"data/raw/shelly_scan_{timestamp}.csv"
    all_json_file = f"data/raw/shelly_scan_all_{timestamp}.json"

    shellys = [r for r in results if r["is_shelly"]]

    with open(json_file, "w", encoding="utf-8") as f:
        json.dump(shellys, f, indent=2, ensure_ascii=False)

    with open(all_json_file, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)

    if shellys:
        with open(csv_file, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=list(shellys[0].keys()))
            writer.writeheader()
            writer.writerows(shellys)

    print(f"\nSaved Shelly JSON: {json_file}")
    print(f"Saved all-results JSON: {all_json_file}")
    if shellys:
        print(f"Saved Shelly CSV: {csv_file}")


def main():
    subnet = prompt_subnet()

    try:
        ipaddress.ip_network(subnet, strict=False)
    except ValueError:
        print(f"Invalid subnet: {subnet}")
        sys.exit(1)

    results = scan_subnet(subnet)
    save_results(results)


if __name__ == "__main__":
    main()
