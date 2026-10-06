import socket
import os
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor, as_completed

print("=" * 45)
print("        SYNTECXHUB TCP PORT SCANNER")
print("=" * 45)

def get_service_name(port):
    try:
        return socket.getservbyport(port, "tcp").upper()
    except (OSError, ValueError):
        return "UNKNOWN"

def scan_port(target, port):
    scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    scanner.settimeout(0.5)

    try:
        result = scanner.connect_ex((target, port))

        if result == 0:
            status = "OPEN"
        elif result in [10060, 110]:
            status = "TIMEOUT"
        else:
            status = "CLOSED"

    except socket.timeout:
        status = "TIMEOUT"

    except Exception:
        status = "ERROR"

    finally:
        scanner.close()

    service = get_service_name(port)
    return port, status, service


try:
    target = input("Enter target IP or hostname: ")

    start_port = int(input("Enter starting port: "))
    end_port = int(input("Enter ending port: "))

    if start_port < 1 or end_port > 65535:
        print("Error: Ports must be between 1 and 65535.")
        exit()

    if start_port > end_port:
        print("Error: Starting port cannot be greater than ending port.")
        exit()

    os.makedirs("logs", exist_ok=True)

    log_file = f"logs/scan_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    
    start_time = datetime.now()
    print(f"Scan started at: {start_time.strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"\nScanning {target} from port {start_port} to {end_port}...\n")

    results = []

    with ThreadPoolExecutor(max_workers=50) as executor:

        futures = {
            executor.submit(scan_port, target, port): port
            for port in range(start_port, end_port + 1)
        }

        for future in as_completed(futures):
            port, status, service = future.result()
            results.append((port, status, service))

    # Sort results by port number
    results.sort()

    open_count = sum(1 for port, status, service in results if status == "OPEN")
    closed_count = sum(1 for port, status, service in results if status == "CLOSED")
    timeout_count = sum(1 for port, status, service in results if status == "TIMEOUT")
    error_count = sum(1 for port, status, service in results if status == "ERROR")

    total_scanned = len(results)

    with open(log_file, "w") as file:

        file.write("SYNTECXHUB PORT SCANNER\n")
        file.write("=======================\n")
        file.write(f"Target: {target}\n")
        file.write(f"Port Range: {start_port} - {end_port}\n\n")

        for port, status, service in results:
         print(f"Port {port}: {status} - {service}")
        file.write(f"Port {port}: {status} - {service}\n")

        file.write("\nSCAN SUMMARY\n")
        file.write("-------------------------\n")
        file.write(f"Total scanned: {total_scanned}\n")
        file.write(f"Open ports: {open_count}\n")
        file.write(f"Closed ports: {closed_count}\n")
        file.write(f"Timeouts: {timeout_count}\n")
        file.write(f"Errors: {error_count}\n")
        file.write("-------------------------\n")

        end_time = datetime.now()
        duration = end_time - start_time

    print("\nScan completed.")
    print("-------------------------")
    print(f"Total scanned: {total_scanned}")
    print(f"Open ports: {open_count}")
    print(f"Closed ports: {closed_count}")
    print(f"Timeouts: {timeout_count}")
    print(f"Errors: {error_count}")
    print(f"Scan duration: {duration}")
    print("-------------------------")
    print(f"Results saved to: {log_file}")
    
except ValueError:
    print("Error: Please enter numbers for the port values.")