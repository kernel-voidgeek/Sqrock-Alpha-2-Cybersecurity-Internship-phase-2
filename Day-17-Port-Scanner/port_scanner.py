
import socket
from datetime import datetime


TARGET = "127.0.0.1"

PORTS = [22, 80, 443, 5432, 8080, 8000]

TIMEOUT = 1.0


def scan_local_ports(host, ports):
    results = []

    print("=" * 55)
    print("       SQROCK CYBERSECURITY - DAY 17")
    print("          LOCAL PORT SCANNER")
    print("=" * 55)

    print(f"Target IP : {host}")
    print(f"Start Time: {datetime.now()}")
    print("-" * 55)

    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(TIMEOUT)

        try:
            result = sock.connect_ex((host, port))

            try:
                service = socket.getservbyport(port, "tcp")
            except OSError:
                service = "Unknown"

            if result == 0:
                status = "OPEN"
                print(f"[+] PORT {port:<5} | {service:<12} | OPEN")
            else:
                status = "CLOSED/FILTERED"
                print(f"[-] PORT {port:<5} | {service:<12} | CLOSED")

            results.append({
                "port": port,
                "service": service,
                "status": status
            })

        except socket.error as error:
            print(f"[!] Port {port}: {error}")

        finally:
            sock.close()

    print("-" * 55)

    open_ports = [item for item in results
                  if item["status"] == "OPEN"]

    print(f"Total ports checked: {len(ports)}")
    print(f"Open ports found  : {len(open_ports)}")
    print("=" * 55)

    # Save execution results
    with open("output.txt", "w") as file:
        file.write("DAY 17 - LOCAL PORT SCAN REPORT\n")
        file.write(f"Target: {host}\n")
        file.write(f"Date: {datetime.now()}\n\n")

        for item in results:
            file.write(
                f"Port {item['port']} | "
                f"{item['service']} | "
                f"{item['status']}\n"
            )

        file.write(f"\nOpen ports: {len(open_ports)}\n")

    print("[+] Results saved to output.txt")


if __name__ == "__main__":
    scan_local_ports(TARGET, PORTS)
