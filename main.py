import socket
import time

def scanner(ip, port):
    print(f"[~]Scanning port {port}")
    print(f"[~]IP: {ip}")
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        sock.connect((ip, port))
        print(f"[!]Port {port} is open")

    except socket.error:
        print(f"[!]Port {port} is closed")

def main():
    start_time = time.time()
    ip = input("[~]Enter the IP address: ")
    port = input("[~]Enter the port range (separated by comma): ")
    if not port.replace(",", "").isdigit() or len(port.split(",")) != 2:
        print("[!]Invalid port range")
        return
    port_range = port.split(",")
    print(port_range)
    print(f"Scanning IP {ip} started at {start_time}")
    for i in range(int(port_range[0]), int(port_range[1])+1):
        scanner(ip, i)

    end_time = time.time()
    print(f"Scanning IP {ip} completed at {end_time}")

if __name__ == "__main__":
    main()