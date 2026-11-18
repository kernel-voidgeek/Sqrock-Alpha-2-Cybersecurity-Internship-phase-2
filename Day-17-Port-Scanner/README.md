# Day 17 – Local Network Port & Service Scanning

**Sqrock Alpha 2 Cybersecurity Internship – Phase 2**

**Prepared by:** Christian Adam Anilbhai

## Project Overview

This project implements a Python-based TCP port scanner to identify open and closed ports on a local machine.

The scanner uses Python's built-in `socket` library to attempt TCP connections against specified ports and records the results.

## Objective

To discover accessible local network ports and evaluate potential service exposure on a computer.

## Technologies Used

- Python 3
- Socket library
- Visual Studio Code
- Windows PowerShell

## Ports Scanned

| Port | Common Service |
|---|---|
| 22 | SSH |
| 80 | HTTP |
| 443 | HTTPS |
| 5432 | PostgreSQL |
| 8080 | Alternative HTTP |
| 8000 | Development Server |

## How It Works

1. The scanner targets the localhost IP address (`127.0.0.1`).
2. It creates a TCP socket for each specified port.
3. It sets a connection timeout of 1 second.
4. It uses `connect_ex()` to attempt a connection.
5. If the return value is `0`, the port is reported as OPEN.
6. Otherwise, the port is reported as CLOSED.
7. The results are saved in `output.txt`.

## Installation

No external Python packages are required.

Make sure Python 3 is installed.

Clone the repository or download the project files.

## Execution

Open the project folder in VS Code or PowerShell.

Run:

```bash
python port_scanner.py
```

## Test Results

The scanner was executed against `127.0.0.1`.

| Metric | Result |
|---|---|
| Target IP | 127.0.0.1 |
| Total ports checked | 6 |
| Open ports detected | 0 |
| Closed ports reported | 6 |
| Output file | output.txt |

All six tested ports were reported as CLOSED during the recorded execution.

## Output

The scanner generates an `output.txt` file containing:

- Target IP address
- Scan date and time
- Port numbers
- Service labels
- Port status

## Learning Outcomes

Through this project, I learned:

- Basic TCP networking concepts.
- How IP addresses and ports work.
- Python socket programming.
- How to perform local TCP connection tests.
- How to identify potentially exposed services.
- How to save scan results in a text file.

## Security Note

This project is intended for educational and defensive security testing.

Scanning should only be performed on systems and networks for which authorization has been granted.

## Conclusion

The Day 17 practical successfully demonstrated local TCP port scanning using Python. The scanner checked six configured ports, identified zero open ports in the recorded test, and generated an output file containing the scan results.

**Project:** Cybersecurity Internship – Phase 2, Day 17  
**Organization:** Sqrock IT Solutions
