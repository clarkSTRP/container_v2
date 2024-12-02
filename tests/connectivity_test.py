import requests
import socket

def test_http_port_8080(url):
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            print("[OK] HTTP server on port 8080 is accessible.")
            return True
        else:
            print(f"[ERROR] The server responded with code {response.status_code} on port 8080.")
            return False
    except requests.exceptions.RequestException as e:
        print(f"[ERROR] Error connecting to HTTP server on port 8080: {e}")
        return False

def test_sql_port_3306():
    host = "localhost"
    port = 3306
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(5)
        result = sock.connect_ex((host, port))
        if result == 0:
            print("[OK] SQL server on port 3306 is accessible.")
            sock.close()
            return True
        else:
            print(f"[WARNING] Unable to connect to SQL server on port {port}. Error code: {result}.")
            sock.close()
            return False
    except socket.error as e:
        print(f"[ERROR] Error connecting to SQL server on port 3306: {e}")
        return False
