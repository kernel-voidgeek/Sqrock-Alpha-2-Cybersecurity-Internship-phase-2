
import re
from datetime import datetime


DOCKERFILE = "Dockerfile.dockerfile"
OUTPUT_FILE = "docker_security_report.txt"


def analyze_dockerfile(path):

    findings = []
    has_user_instruction = False

    print("=" * 60)
    print("      SQROCK CYBERSECURITY - DAY 19")
    print("     DOCKER SECURITY CONFIGURATION SCANNER")
    print("=" * 60)

    try:
        with open(path, "r", encoding="utf-8") as file:
            lines = file.readlines()

    except FileNotFoundError:
        print(f"[!] Error: {path} not found.")
        return None

    print(f"[*] Analyzing Dockerfile: {path}\n")

    for line_number, line in enumerate(lines, start=1):

        # Ignore empty lines and comments
        cleaned = line.strip()

        if not cleaned or cleaned.startswith("#"):
            continue

        upper_line = cleaned.upper()

        # Check FROM instruction
        if upper_line.startswith("FROM "):

            image = cleaned.split()[1]

            if image.lower().endswith(":latest"):
                findings.append({
                    "severity": "MEDIUM",
                    "line": line_number,
                    "issue": "Unpinned latest image tag",
                    "details": f"Image '{image}' uses the latest tag."
                })

                print(
                    f"[!] RISK DETECTED | Line {line_number}: "
                    f"Image uses latest tag ({image})"
                )

        # Check USER instruction
        if upper_line.startswith("USER "):
            has_user_instruction = True

        # Check exposed SSH port
        if upper_line.startswith("EXPOSE "):

            ports = cleaned.split()[1:]

            for port in ports:

                port_number = port.split("/")[0]

                if port_number == "22":

                    findings.append({
                        "severity": "HIGH",
                        "line": line_number,
                        "issue": "SSH port exposure",
                        "details": "Dockerfile exposes port 22."
                    })

                    print(
                        f"[!] HIGH RISK | Line {line_number}: "
                        "SSH port 22 is exposed"
                    )

    # Check for explicit USER instruction
    if not has_user_instruction:

        findings.append({
            "severity": "HIGH",
            "line": "-",
            "issue": "Missing USER instruction",
            "details": "No explicit USER instruction was found."
        })

        print(
            "[!] HIGH RISK | No USER instruction found. "
            "Container may run as root."
        )

    if not findings:
        print("[+] No configured security issues detected.")

    return findings


def generate_report(findings):

    with open(OUTPUT_FILE, "w", encoding="utf-8") as file:

        file.write("DAY 19 - DOCKER SECURITY AUDIT REPORT\n")
        file.write(f"Scan Time: {datetime.now()}\n")
        file.write("=" * 60 + "\n\n")

        if not findings:
            file.write("No configured security issues detected.\n")

        for finding in findings:

            file.write(
                f"[{finding['severity']}] "
                f"{finding['issue']}\n"
            )

            file.write(
                f"Line: {finding['line']}\n"
            )

            file.write(
                f"Details: {finding['details']}\n"
            )

            file.write("-" * 60 + "\n")

        file.write(
            f"\nTotal findings: {len(findings)}\n"
        )

    print("\n" + "=" * 60)
    print(f"Total security findings: {len(findings)}")
    print("=" * 60)

    print(f"[+] Report saved to {OUTPUT_FILE}")


def main():

    findings = analyze_dockerfile(DOCKERFILE)

    if findings is not None:
        generate_report(findings)


if __name__ == "__main__":
    main()
