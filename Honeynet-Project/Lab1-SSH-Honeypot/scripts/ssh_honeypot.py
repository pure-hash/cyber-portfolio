#!/usr/bin/env python3
"""
ssh_honeypot.py
Low-interaction SSH-style honeypot that logs attempts as JSON lines.

Behavior:
- Listens on HOST:PORT (default 0.0.0.0:2222)
- Sends SSH banner
- Prompts for Username and Password (plain text prompts)
- Logs: timestamp, src_ip, src_port, username, password, banner, extra
- Saves logs to ../logs/ssh_honeypot.jsonl
"""

import socket, threading, json, os, argparse
from datetime import datetime

# ─────────────────────────────────────────────────────────
# Pretty output helpers (colors + banners)
# ─────────────────────────────────────────────────────────

GREEN = "\033[92m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
RESET = "\033[0m"

def print_banner():
    print("")
    print(CYAN + "┌" + "─" * 36 + "┐" + RESET)
    print(CYAN + "│       SSH Honeypot Active          │" + RESET)
    print(CYAN + "├" + "─" * 36 + "┤" + RESET)
    print(CYAN + "│ Listening on 0.0.0.0:2222          │" + RESET)
    print(CYAN + "└" + "─" * 36 + "┘" + RESET)
    print("")

def print_connection(ip, port):
    print(GREEN + "╔══════════════════════════════════╗" + RESET)
    print(GREEN + f"║ Connection detected!             ║" + RESET)
    print(GREEN + f"║ IP:   {ip:<25}  ║" + RESET)
    print(GREEN + f"║ Port: {port:<23}    ║" + RESET)
    print("")

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
LOG_DIR = os.path.join(BASE_DIR, "logs")
LOG_FILE = os.path.join(LOG_DIR, "ssh_honeypot.jsonl")
BANNER = b"SSH-2.0-OpenSSH_7.9\r\n"

os.makedirs(LOG_DIR, exist_ok=True)

from datetime import datetime, timezone

def utcnow_iso():
    return datetime.now(timezone.utc).isoformat()

def safe_recv(conn, size=2048, timeout=5):
    conn.settimeout(timeout)
    try:
        data = conn.recv(size)
        if not data:
            return ""
        return data.decode(errors="replace").strip()
    except Exception:
        return ""

def log_json(src_ip, src_port, username, password, banner, extra):
    entry = {
        "timestamp": utcnow_iso(),
        "src_ip": src_ip,
        "src_port": src_port,
        "username": username,
        "password": password,
        "banner": banner,
        "extra": extra
    }
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(json.dumps(entry) + "\n")

def handle_client(conn, addr):
    src_ip, src_port = addr[0], addr[1]
    try:
        conn.sendall(BANNER)
        conn.sendall(b"Username: ")
        username = safe_recv(conn)
        conn.sendall(b"Password: ")
        password = safe_recv(conn)
        # Read one more short chunk if client sends it
        extra = safe_recv(conn, size=4096, timeout=1)
        # Log attempt
        log_json(src_ip, src_port, username or "<empty>", password or "<empty>",
                 BANNER.decode(errors="replace").strip(), extra or "")
        conn.sendall(b"Permission denied.\r\n")
    except Exception as e:
        # Minimal error logging (do not crash)
        log_json(src_ip, src_port, "<error>", "<error>", "", str(e))
    finally:
        try:
            conn.shutdown(socket.SHUT_RDWR)
        except Exception:
            pass
        conn.close()

def run_server(host, port):
    srv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    srv.bind((host, port))
    srv.listen(50)

    print_banner()  # Now correctly indented.

    try:
        while True:
            conn, addr = srv.accept()
            client_ip, client_port = addr  # Capture the IP and port from addr
            print_connection(client_ip, client_port)  # Now correctly prints connection details
            t = threading.Thread(target=handle_client, args=(conn, addr), daemon=True)
            t.start()
    except KeyboardInterrupt:
        print("\n[!] Stopping honeypot")
    finally:
        srv.close()

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--host", default="0.0.0.0")
    ap.add_argument("--port", type=int, default=2222)
    args = ap.parse_args()
    run_server(args.host, args.port)
