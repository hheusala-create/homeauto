import csv
import glob
import json
import os


RAW_GLOB = "data/raw/shelly_scan_*.json"
OUTPUT_JSON = "data/processed/shelly_master_inventory.json"
OUTPUT_CSV = "data/processed/shelly_master_inventory.csv"


def load_scan_files():
    files = sorted(glob.glob(RAW_GLOB))
    valid_files = []

    for path in files:
        if os.path.basename(path).startswith("shelly_scan_all_"):
            continue
        valid_files.append(path)

    print(f"Found {len(valid_files)} Shelly scan JSON file(s).")
    return valid_files


def normalize_string(value):
    if value is None:
        return ""
    return str(value).strip()


def build_unique_key(device):
    mac = normalize_string(device.get("mac")).upper()
    ip = normalize_string(device.get("ip"))

    if mac:
        return f"MAC:{mac}"
    if ip:
        return f"IP:{ip}"
    return f"NAME:{normalize_string(device.get('name'))}"


def score_device(device):
    score = 0

    for field in ["ip", "device_type", "model", "name", "mac", "firmware", "generation"]:
        if normalize_string(device.get(field)):
            score += 1

    return score


def merge_devices(files):
    merged = {}
    source_map = {}

    for path in files:
        print(f"Reading {path}")
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)

        if not isinstance(data, list):
            continue

        for device in data:
            if not isinstance(device, dict):
                continue

            key = build_unique_key(device)
            current_score = score_device(device)

            if key not in merged:
                merged[key] = device
                source_map[key] = [path]
            else:
                existing_score = score_device(merged[key])

                if current_score >= existing_score:
                    merged[key] = device

                source_map[key].append(path)

    results = []

    for key, device in merged.items():
        row = {
            "ip": normalize_string(device.get("ip")),
            "hostname": normalize_string(device.get("hostname")),
            "generation": normalize_string(device.get("generation")),
            "device_type": normalize_string(device.get("device_type")),
            "model": normalize_string(device.get("model")),
            "current_name": normalize_string(device.get("name")),
            "mac": normalize_string(device.get("mac")).upper(),
            "firmware": normalize_string(device.get("firmware")),
            "detected_by": normalize_string(device.get("detected_by")),
            "source_files": " | ".join(source_map.get(key, [])),
            "room": "",
            "purpose": "",
            "switch_or_load": "",
            "planned_ha_name": "",
            "notes": normalize_string(device.get("notes")),
        }
        results.append(row)

    def ip_sort_key(row):
        ip = row["ip"]
        if not ip:
            return (999, 999, 999, 999)
        try:
            return tuple(int(part) for part in ip.split("."))
        except Exception:
            return (999, 999, 999, 999)

    results.sort(key=ip_sort_key)
    return results


def save_json(devices):
    with open(OUTPUT_JSON, "w", encoding="utf-8") as f:
        json.dump(devices, f, indent=2, ensure_ascii=False)


def save_csv(devices):
    fieldnames = [
        "ip",
        "hostname",
        "generation",
        "device_type",
        "model",
        "current_name",
        "mac",
        "firmware",
        "detected_by",
        "source_files",
        "room",
        "purpose",
        "switch_or_load",
        "planned_ha_name",
        "notes",
    ]

    with open(OUTPUT_CSV, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(devices)


def main():
    files = load_scan_files()

    if not files:
        print("No Shelly scan JSON files found in data/raw/")
        return

    devices = merge_devices(files)

    print(f"Merged unique devices: {len(devices)}")

    save_json(devices)
    save_csv(devices)

    print(f"Saved JSON: {OUTPUT_JSON}")
    print(f"Saved CSV:  {OUTPUT_CSV}")


if __name__ == "__main__":
    main()
