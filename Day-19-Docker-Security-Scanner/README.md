# Day 19 – Docker Security Configuration Scanner

**Prepared by:** Christian Adam Anilbhai

## Project Overview

This project is a Python-based static analysis tool that reviews Dockerfile text for selected security misconfigurations. It checks for an explicitly `latest` image tag, exposed SSH port 22, and the absence of an explicit `USER` instruction.

## Objective

To audit Dockerfile configuration and identify selected security risks using Python text-analysis routines.

## Technologies Used

- Python 3
- Regular expressions (`re`)
- File handling
- Visual Studio Code
- Windows PowerShell

No Docker installation is required because the scanner analyzes the Dockerfile as text and does not build or run containers.

## Security Checks

| Check | Description |
|---|---|
| Latest image tag | Detects a `FROM` image explicitly ending in `:latest` |
| SSH port exposure | Detects port 22 in an `EXPOSE` instruction |
| Missing USER instruction | Flags Dockerfiles without an explicit `USER` instruction |

## Project Files

```text
Day-19-Docker-Security-Scanner/
├── docker_scanner.py
├── Dockerfile
├── docker_security_report.txt
├── security_checklist.md
└── README.md
```

The Dockerfile used during the recorded test was named `Dockerfile.dockerfile`.

## How It Works

1. Opens and reads the Dockerfile.
2. Skips blank lines and comments.
3. Checks `FROM` instructions for an image using the `latest` tag.
4. Checks `EXPOSE` instructions for port 22.
5. Tracks whether an explicit `USER` instruction exists.
6. Reports findings with severity labels and line numbers when available.
7. Saves the findings to `docker_security_report.txt`.

## How to Run

Ensure Python 3 is installed and the scanner and Dockerfile are in the same folder. The filename configured in `docker_scanner.py` must match the actual Dockerfile filename.

Run:

```bash
python docker_scanner.py
```

## Test Results

The recorded execution analyzed `Dockerfile.dockerfile` and reported three findings.

| Finding | Result |
|---|---|
| Image uses `python:latest` | Detected on line 2 |
| SSH port 22 exposed | Detected on line 8 |
| Explicit `USER` instruction missing | Detected |
| Total findings | 3 |

The tool generated `docker_security_report.txt`.

## Output

The report contains:

- Finding severity
- Issue description
- Line number, when available
- Details about the detected configuration
- Total findings

## Learning Outcomes

- Understanding Dockerfiles and container configuration
- Identifying selected container security misconfigurations
- Performing static analysis using Python
- Reading configuration files
- Applying rule-based security checks
- Generating audit reports

## Limitations

This scanner checks only the rules implemented in the script. It does not inspect image contents, dependencies, secrets, runtime configuration, or vulnerabilities. The presence of `EXPOSE 22` does not itself publish a port, and a missing `USER` instruction does not conclusively prove that the container runs as root; behavior depends on the base image and runtime configuration.

## Security Note

The Dockerfile is intentionally configured with example misconfigurations for educational analysis. The project performs static analysis and does not build, run, or deploy containers.

## Conclusion

The Day 19 Docker Security Configuration Scanner successfully analyzed the test Dockerfile and detected three configured security findings: an explicit `python:latest` image tag, SSH port 22 exposure, and the absence of an explicit `USER` instruction. The project demonstrates static configuration auditing and defensive security reporting with Python.
