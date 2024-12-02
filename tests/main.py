from connectivity_test import test_http_port_8080, test_sql_port_3306
from dos_test import test_dos_attack
from telnet_test import test_telnet
from header_test import test_http_security_headers
import time

if __name__ == "__main__":
    url = "http://localhost:8080"

    if test_http_port_8080(url) and test_sql_port_3306():
        test_telnet("127.0.0.1", 23)
        test_telnet("127.0.0.1", 8080)
        test_telnet("127.0.0.1", 3306)

        test_http_security_headers(url)

        
        print("Do you want to initiate a DoS test? (yes/no)")
        response = input().strip().lower()

        if response == "yes":
            start_time = time.time()
            test_dos_attack(url, num_threads=600, requests_per_thread=200)
            end_time = time.time()
            print(f"DoS test completed in {end_time - start_time:.2f} seconds.")
        elif response == "no":
            print("DoS test aborted.")
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")
    else:
        print("Connectivity tests failed.")
