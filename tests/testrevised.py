import threading
import requests
import time
import socket

# Event to stop all threads
stop_event = threading.Event()

# Failure global variable
test_failed = False
failure_code = None

# Function to send requests with threads to stress the server (used in test_dos_attack)
def send_requests(url, num_requests, thread_id):
    global test_failed, failure_code
    for i in range(num_requests):
        if stop_event.is_set():
            break

        try:
            response = requests.get(url, timeout=5)  # Added timeout for stability
            # Capture the error code and set the test as failed
            if response.status_code != 200:
                failure_code = response.status_code
                stop_event.set()
                test_failed = True
                break
        except requests.exceptions.RequestException as e:
            failure_code = f"RequestException: {e}"
            stop_event.set()
            test_failed = True
            break

# Test DoS with more threads and multiple requests per thread
def test_dos_attack(url, num_threads, requests_per_thread):
    print("Launching DoS testing, please wait ....")
    threads = []

    # Create threads
    for i in range(num_threads):
        thread = threading.Thread(target=send_requests, args=(url, requests_per_thread, i))
        threads.append(thread)
        thread.start()

    # Wait for all threads to finish
    for thread in threads:
        thread.join()

# Test that the port 8080 is up
def test_http_port_8080():
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

# Test that the 3306 port is up
def test_sql_port_3306():
    host = "localhost"  # Updated from 'db' to 'localhost' for simplicity
    port = 3306
    try:
        # Create a socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(5)
        result = sock.connect_ex((host, port))
        if result == 0:
            print("[OK] SQL server on port 3306 is accessible.")
            sock.close()
            return True
        else:
            print(f"[WARNING] Unable to connect to the SQL server on port {port}. Error code: {result}.")
            sock.close()
            return False
    except socket.error as e:
        print(f"[ERROR] Error connecting to SQL server on port 3306: {e}")
        return False

# Test Telnet connectivity on multiple ports
def test_telnet(host, port):
    try:
        # Create a socket
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

# Test HTTP security headers
def test_http_security_headers(url):
    # List of security headers to check for
    security_headers = [
        "Strict-Transport-Security",
        "X-Content-Type-Options",
        "X-Frame-Options",
        "Content-Security-Policy",
        "X-XSS-Protection"
    ]

    try:
        response = requests.get(url, timeout=5)
        print(f"\nChecking security headers for {url}...")

        # Check if each security header is present in the server response
        for header in security_headers:
            if header in response.headers:
                print(f"[OK] {header} is present: {response.headers[header]}")
            else:
                print(f"[WARNING] {header} is missing!")
    except requests.exceptions.RequestException as e:
        print(f"[ERROR] Error while checking security headers for {url}: {e}")

# Constructor to execute the code in a specified order
if __name__ == "__main__":
    url = "http://localhost:8080"  # Changed from 172.20.0.1 to localhost

    # Connectivity Tests
    if test_http_port_8080() and test_sql_port_3306():

        # We can adjust on which port we want to test the Telnet protocol
        test_telnet("127.0.0.1", 23)
        test_telnet("127.0.0.1", 8080)
        test_telnet("127.0.0.1", 3306)

        # Test HTTP security headers
        test_http_security_headers(url)

        # Adjust the number of threads and requests per thread here
        num_threads = 600
        requests_per_thread = 200

        # Measure the starting and ending time
        start_time = time.time()
        test_dos_attack(url, num_threads=num_threads, requests_per_thread=requests_per_thread)
        end_time = time.time()

        # If test failed, print the error code, else return test OK
        if test_failed:
            print(f"[WARNING] DoS Test Failed with error code: {failure_code}")
        else:
            print("[OK] DoS Test Passed")

        print(f"Total time for DoS test: {end_time - start_time:.2f} seconds")
    else:
        print("Connectivity tests failed.")
