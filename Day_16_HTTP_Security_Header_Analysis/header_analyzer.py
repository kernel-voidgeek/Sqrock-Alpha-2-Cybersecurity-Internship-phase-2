
import requests

def verify_headers(url):
    print(f"\n[*] Auditing Target Headers: {url}")

    target_headers = [
        "Strict-Transport-Security",
        "Content-Security-Policy",
        "X-Frame-Options",
        "X-Content-Type-Options"
    ]

    try:
        response = requests.get(url, timeout=5)

        print(f"[*] HTTP Status Code: {response.status_code}\n")

        for header in target_headers:
            if header in response.headers:
                print(f"[+] CONFIGURED: {header}")
                print(f"    Value: {response.headers[header]}\n")
            else:
                print(f"[-] MISSING: {header}\n")

    except requests.RequestException as error:
        print(f"[!] Target Unreachable: {error}")


verify_headers("http://localhost:8000")

