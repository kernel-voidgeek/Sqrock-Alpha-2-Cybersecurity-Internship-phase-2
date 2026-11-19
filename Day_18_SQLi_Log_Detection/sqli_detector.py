
import re
from urllib.parse import unquote_plus
from datetime import datetime

LOG_FILE = "sample_logs.txt"
OUTPUT_FILE = "detection_results.txt"


SQLI_PATTERNS = {
    "UNION SELECT": re.compile(
        r"\bUNION\s+(?:ALL\s+)?SELECT\b", re.IGNORECASE
    ),

    "OR-based SQL Injection": re.compile(
        r"""(?:['"]\s*)?OR\s+['"]?\d+['"]?\s*=\s*['"]?\d+['"]?""",
        re.IGNORECASE
    ),

    "SQL Comment Sequence": re.compile(
        r"(?:--|#)"
    )
}


def analyze_logs(logs):
    findings = []

    print("=" * 65)
    print("       SQROCK CYBERSECURITY - DAY 18")
    print("          SQLi LOG DETECTION ENGINE")
    print("=" * 65)

    for line_number, entry in enumerate(logs, start=1):

        
        decoded_entry = unquote_plus(entry)

        detected_patterns = []

        
        for pattern_name, pattern in SQLI_PATTERNS.items():

            if pattern.search(decoded_entry):
                detected_patterns.append(pattern_name)

        if detected_patterns:

            source_ip = entry.split(" ")[0]

            finding = {
                "line": line_number,
                "ip": source_ip,
                "patterns": detected_patterns,
                "log": entry.strip()
            }

            findings.append(finding)

            print(f"\n[!] SUSPICIOUS ACTIVITY DETECTED")
            print(f"    Source IP : {source_ip}")
            print(f"    Log Line  : {line_number}")
            print(f"    Signatures: {', '.join(detected_patterns)}")

        else:
            print(f"[+] Line {line_number}: No SQLi signature detected")

    return findings


def save_results(findings):

    with open(OUTPUT_FILE, "w", encoding="utf-8") as file:

        file.write("DAY 18 - SQLi DETECTION REPORT\n")
        file.write(f"Scan Time: {datetime.now()}\n")
        file.write("=" * 65 + "\n\n")

        if not findings:
            file.write("No suspicious patterns detected.\n")

        for finding in findings:

            file.write("[SUSPICIOUS ACTIVITY]\n")
            file.write(f"Source IP: {finding['ip']}\n")
            file.write(f"Line Number: {finding['line']}\n")
            file.write(
                f"Detected Patterns: "
                f"{', '.join(finding['patterns'])}\n"
            )
            file.write(f"Log Entry: {finding['log']}\n")
            file.write("-" * 65 + "\n")

        file.write(f"\nTotal suspicious entries: {len(findings)}\n")

    print(f"\n[+] Results saved to {OUTPUT_FILE}")


def main():

    try:
        with open(LOG_FILE, "r", encoding="utf-8") as file:
            logs = file.readlines()

        print(f"\n[*] Loaded {len(logs)} log entries")
        print("[*] Analyzing SQL Injection signatures...\n")

        findings = analyze_logs(logs)

        print("\n" + "=" * 65)
        print(f"Total log entries : {len(logs)}")
        print(f"Suspicious entries: {len(findings)}")
        print("=" * 65)

        save_results(findings)

    except FileNotFoundError:
        print(f"[!] Error: {LOG_FILE} not found.")
        print("[!] Make sure sample_logs.txt is in the same folder.")


if __name__ == "__main__":
    main()
