# Day 18 – SQL Injection (SQLi) Log Detection Engine

**Prepared by:** Christian Adam Anilbhai

## Project Overview

This project is a Python-based defensive log analysis tool that detects suspicious SQL Injection patterns in simulated web access logs. It uses regular expressions and URL decoding to identify potentially malicious request strings.

## Objective

To analyze web access logs and identify entries matching selected SQL Injection signatures.

## Technologies Used

- Python 3
- `re` (regular expressions)
- `urllib.parse` (`unquote_plus`)
- `datetime`
- Visual Studio Code
- Windows PowerShell

## Detection Signatures

The tool checks for the following patterns:

- `UNION SELECT`
- OR-based SQL Injection patterns such as `' OR '1'='1`
- SQL comment sequences such as `--` and `#`

The log entries are URL-decoded before pattern matching so encoded characters can be analyzed.

## Project Files

```text
Day-18-SQLi-Log-Detection/
├── sqli_detector.py
├── sample_logs.txt
├── detection_results.txt
└── README.md
```

## How It Works

1. Reads entries from `sample_logs.txt`.
2. Decodes URL-encoded text using `unquote_plus()`.
3. Checks each entry against configured regular-expression signatures.
4. Identifies matching entries as suspicious.
5. Displays the source IP, line number, and detected signatures.
6. Saves findings to `detection_results.txt`.

## How to Run

Ensure Python 3 is installed and all project files are in the same folder.

Run:

```bash
python sqli_detector.py
```

## Test Results

The recorded test analyzed five simulated log entries.

| Metric | Result |
|---|---:|
| Total log entries | 5 |
| Suspicious entries | 2 |
| Entries with no matching signatures | 3 |
| Output file | `detection_results.txt` |

The detector identified an OR-based SQL Injection signature in one entry and `UNION SELECT` plus an SQL comment sequence in another.

## Output

The generated `detection_results.txt` includes:

- Scan timestamp
- Source IP address
- Log line number
- Detected pattern names
- Original log entry
- Total suspicious entries

## Learning Outcomes

- Understanding SQL Injection indicators
- Reading and processing log files in Python
- Using regular expressions for signature detection
- URL decoding encoded request parameters
- Creating a basic defensive log analysis tool
- Writing detection results to a report file

## Limitations

This is a basic signature-based detector. It may produce false positives and may not detect obfuscated or unfamiliar SQL Injection patterns. A suspicious log entry is not proof that an attack succeeded.

## Security Note

This project uses simulated log entries for educational and defensive analysis. It does not test or attack live websites.

## Conclusion

The Day 18 SQLi Log Detection Engine successfully analyzed five simulated log entries and identified two entries matching the configured signatures. The project demonstrates basic log analysis, regular-expression matching, URL decoding, and defensive security reporting using Python.
