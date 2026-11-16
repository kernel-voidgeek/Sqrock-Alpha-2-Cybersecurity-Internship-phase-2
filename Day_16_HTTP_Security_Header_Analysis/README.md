# Day 16 — HTTP Security Header Analysis

**Difficulty:** Beginner  
**Status:** Completed

## Objective
Inspect HTTP response headers on an authorized local test server and identify whether selected browser security headers are configured.

## Tools
- Python 3.14.10
- `requests` 2.34.2
- Python `http.server`
- Visual Studio Code
- Localhost (`localhost:8000`)

## Add these project files
- `header_analyzer.py` — checks four HTTP response headers.
- `secure_server.py` — local demonstration server that adds three security headers.
- `Day_16_HTTP_Security_Header_Analysis_Report_Christian_Adam_Anilbhai.pdf` — technical report.
- `screenshots/` — terminal screenshots from both tests.

## Headers checked
| Header | Purpose |
|---|---|
| `Strict-Transport-Security` | Instructs browsers to use HTTPS for future connections after receiving the policy over HTTPS. |
| `Content-Security-Policy` | Restricts permitted resource sources and can reduce the impact of some XSS attacks. |
| `X-Frame-Options` | Controls framing and helps mitigate clickjacking. |
| `X-Content-Type-Options` | `nosniff` prevents MIME-type sniffing in supported browser contexts. |

## Results
**Test 1 — Basic Python HTTP server:** HTTP 200; all four selected headers were missing.

**Test 2 — Custom local test server:** HTTP 200; CSP (`default-src 'self'`), X-Frame-Options (`DENY`), and X-Content-Type-Options (`nosniff`) were configured. HSTS remained missing.

HSTS remained absent because this demonstration used plain HTTP on localhost. HSTS should be delivered over HTTPS.

## CSP analysis
The policy `default-src 'self'` sets the default permitted resource source to the same origin as the page. A browser enforcing this policy can block resources, such as scripts, loaded from unapproved external origins. CSP is defense in depth, not a replacement for input validation, context-aware output encoding, or safe DOM practices.

## Conclusion
The analyzer successfully compared two local server configurations, identifying all four headers as missing on the basic server and detecting three configured headers on the custom server.

## Safety
Testing was restricted to localhost in an authorized lab. No public or third-party target was scanned.
