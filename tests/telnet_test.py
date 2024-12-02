import socket

def test_telnet(host, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(5)
        result = sock.connect_ex((host, port))
        if result == 0:
            print(f"[WARNING] Telnet connection successful on {host}:{port}.")
        else:
            print(f"[OK] Telnet not accessible on {host}:{port}. Error code: {result}.")
        sock.close()
    except socket.error as e:
        print(f"[ERROR] Error establishing Telnet connection on {host}:{port}: {e}")
