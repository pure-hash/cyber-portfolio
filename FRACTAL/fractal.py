import docker
import yaml
import json
import time
import subprocess
import os

LOG_PATH = "./logs/"
RESULTS_PATH = "./results/"

def load_manifest():
    with open("config/test_manifest.yaml", "r") as f:
        return yaml.safe_load(f)["tests"]

def run_atomic(container, atomic_cmd):
    exec_cmd = f"powershell -Command {atomic_cmd}"
    print("[*] Executing attack:", exec_cmd)
    container.exec_run(exec_cmd)
    time.sleep(3)

def extract_logs(container):
    print("[*] Extracting logs...")
    container.exec_run(r'powershell -Command "wevtutil qe Microsoft-Windows-Sysmon/Operational /f:xml > C:\\logs.xml"')
    bits, _ = container.get_archive("C:\\logs.xml")
    with open(LOG_PATH + "sysmon.xml", "wb") as f:
        for chunk in bits:
            f.write(chunk)
    print("[+] Logs saved to logs/sysmon.xml")

def run_sigma(sigma_rule, log_file):
    result = subprocess.run(
        ["sigma-cli", "scan", "-r", f"rules/{sigma_rule}", log_file, "--output=json"],
        capture_output=True,
        text=True
    )

    try:
        output = json.loads(result.stdout)
        return len(output) > 0
    except:
        return False

def save_report(test_id, detected, details=None):
    report = {
        "test_id": test_id,
        "detected": detected,
        "details": details
    }
    fname = RESULTS_PATH + f"report_{test_id}.json"
    with open(fname, "w") as f:
        json.dump(report, f, indent=4)
    print("[+] Report saved:", fname)

def main():
    print("[*] Loading configuration...")
    tests = load_manifest()

    print("[*] Starting Docker container...")
    client = docker.from_env()
    container = client.containers.run("fractal_victim", detach=True)

    time.sleep(5)

    for test in tests:
        print(f"\n=== Running Test {test['id']} ===")
        run_atomic(container, test["atomic_test"])
        extract_logs(container)

        detected = run_sigma(test["sigma_rule"], LOG_PATH + "sysmon.xml")
        save_report(test["id"], detected)

    print("[*] Stopping and removing container...")
    container.stop()
    container.remove()

if __name__ == "__main__":
    main()
