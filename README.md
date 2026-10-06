# Syntecxhub TCP Port Scanner

A simple multithreaded TCP port scanner developed as part of the Syntecxhub Cybersecurity Internship Program.

## Features

- Scan a single host using an IP address or hostname
- Scan a custom range of TCP ports
- Multithreaded scanning for faster results
- Detect OPEN, CLOSED, TIMEOUT, and ERROR states
- Identify common service names such as HTTP, SSH, FTP, and HTTPS
- Validate port numbers
- Handle invalid input and network errors
- Save scan results automatically to log files
- Display a final scan summary

## Technologies Used

- Python
- Socket Programming
- ThreadPoolExecutor
- File Handling
- Exception Handling

## How to Run

1. Make sure Python is installed.

2. Open the project folder in VS Code.

3. Run:
-----bash

python port_scanner.py

4. Enter the target IP address or hostname.

127.0.0.1

5. Enter the starting port.

1

6. Enter the ending port.

100

## Example Output
=============================================
        SYNTECXHUB TCP PORT SCANNER
=============================================

Enter target IP or hostname: 127.0.0.1
Enter starting port: 1
Enter ending port: 100

Scanning 127.0.0.1 from port 1 to 100...

Port 21: CLOSED - FTP
Port 22: CLOSED - SSH
Port 80: CLOSED - HTTP

Scan completed.
-------------------------
Total scanned: 100
Open ports: 0
Closed ports: 100
Timeouts: 0
Errors: 0
-------------------------
## Logs
Scan results are automatically saved inside the logs folder.

## Disclaimer
This project is intended for educational purposes only.
Only scan systems, networks, and devices that you own or have permission to test.

## Internship
Developed as part of the Syntecxhub Cybersecurity Internship Program.
