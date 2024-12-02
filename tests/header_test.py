import requests

def test_http_security_headers(url):
    security_headers = [
        "Strict-Transport-Security",
        "X-Content-Type-Options",
        "X-Frame-Options",
        "Content-Security-Policy",
        "X-XSS-Protection",
    ]

    try:
        response = requests.get(url, timeout=5)
        print(f"\nChecking security headers for {url}...")

        for header in security_headers:
            if header in response.headers:
                print(f"[OK] {header} is present: {response.headers[header]}")
            else:
                print(f"[WARNING] {header} is missing!")
    except requests.exceptions.RequestException as e:
        print(f"[ERROR] Error while checking security headers for {url}: {e}")
