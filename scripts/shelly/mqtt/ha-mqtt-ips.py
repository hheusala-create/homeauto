import json
import time
from typing import Any

import requests

# ============================================================
# Shelly MQTT rollout for selected non-critical devices only
# Excluded on purpose:
# - 10.107.1.221  (network core power, critical)
# - 10.107.1.223  (excluded for now)
# - 10.107.1.232  (currently feeding HA OS server)
# ============================================================

TARGET_IPS = [
    "10.107.1.23",
    "10.107.1.35",
    "10.107.1.48",
    "10.107.1.52",
    "10.107.1.70",
    "10.107.1.72",
    "10.107.1.98",
    "10.107.1.118",
    "10.107.1.137",
    "10.107.1.164",
    "10.107.1.179",
    "10.107.1.192",
    "10.107.1.195",
    "10.107.1.203",
    "10.107.1.207",
    "10.107.1.222",
    "10.107.1.224",
    "10.107.1.227",
]

MQTT_SERVER = "10.107.1.101:1883"
MQTT_USERNAME = "shelly"
MQTT_PASSWORD = "4KkZGIMab"

HTTP_TIMEOUT_SECONDS = 10


def rpc_call(ip: str, method: str, params: dict[str, Any] | None = None) -> dict[str, Any]:
    url = f"http://{ip}/rpc"
    payload: dict[str, Any] = {
        "id": 1,
        "src": "chatgpt",
        "method": method,
    }

    if params is not None:
        payload["params"] = params

    response = requests.post(url, json=payload, timeout=HTTP_TIMEOUT_SECONDS)
    response.raise_for_status()
    return response.json()


def get_mqtt_config(ip: str) -> dict[str, Any]:
    return rpc_call(ip, "MQTT.GetConfig")


def set_mqtt_config(ip: str) -> dict[str, Any]:
    params = {
        "config": {
            "enable": True,
            "server": MQTT_SERVER,
            "user": MQTT_USERNAME,
            "pass": MQTT_PASSWORD,
            "rpc_ntf": True,
            "status_ntf": True,
            "enable_control": True,
        }
    }
    return rpc_call(ip, "MQTT.SetConfig", params)


def reboot_device(ip: str, delay_ms: int = 1000) -> dict[str, Any]:
    return rpc_call(ip, "Shelly.Reboot", {"delay_ms": delay_ms})


def summarize_config(config_response: dict[str, Any]) -> str:
    params = config_response.get("params", config_response)

    enable = params.get("enable")
    server = params.get("server")
    rpc_ntf = params.get("rpc_ntf")
    status_ntf = params.get("status_ntf")
    enable_control = params.get("enable_control")
    topic_prefix = params.get("topic_prefix")

    return (
        f"enable={enable}, "
        f"server={server}, "
        f"rpc_ntf={rpc_ntf}, "
        f"status_ntf={status_ntf}, "
        f"enable_control={enable_control}, "
        f"topic_prefix={topic_prefix}"
    )


def main() -> None:
    print("Starting Shelly MQTT rollout for selected devices only.")
    print()

    for ip in TARGET_IPS:
        print("=" * 72)
        print(f"DEVICE: {ip}")

        try:
            set_result = set_mqtt_config(ip)
            print("Set result:")
            print(f"  {json.dumps(set_result, ensure_ascii=False)}")
        except Exception as exc:
            print(f"  ERROR setting MQTT config: {exc}")
            print()
            continue

        try:
            reboot_result = reboot_device(ip)
            print("Reboot result:")
            print(f"  {json.dumps(reboot_result, ensure_ascii=False)}")
            time.sleep(12)
        except Exception as exc:
            print(f"  ERROR rebooting device: {exc}")
            print()
            continue

        try:
            after = get_mqtt_config(ip)
            print("After:")
            print(f"  {summarize_config(after)}")
        except Exception as exc:
            print(f"  ERROR reading config after change: {exc}")

        print()

    print("Done.")


if __name__ == "__main__":
    main()