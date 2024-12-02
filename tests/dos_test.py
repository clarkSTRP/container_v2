import threading
import requests
import time

stop_event = threading.Event()
test_failed = False
failure_code = None

def send_requests(url, num_requests):
    global test_failed, failure_code
    for _ in range(num_requests):
        if stop_event.is_set():
            break
        try:
            response = requests.get(url, timeout=120)
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

def test_dos_attack(url, num_threads, requests_per_thread):
    global test_failed, failure_code
    threads = []

    print("Launching DoS testing, please wait...")
    for _ in range(num_threads):
        thread = threading.Thread(target=send_requests, args=(url, requests_per_thread))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    if test_failed:
        print(f"[WARNING] DoS Test Failed with error code: {failure_code}")
    else:
        print("[OK] DoS Test Passed")
