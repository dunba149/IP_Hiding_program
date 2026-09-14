import requests


def get_public_ip(session=None):
    url = "https://api.ipify.org?format=json"

    try:
        if session:
            response = session.get(url, timeout=15)
        else:
            response = requests.get(url, timeout=15)

        response.raise_for_status()
        return response.json()["ip"]

    except Exception as e:
        return f"Error: {e}"


original_ip = get_public_ip()

print("Your Real Public IP:", original_ip)

tor_session = requests.Session()

tor_session.proxies = {
    "http": "socks5h://127.0.0.1:9150",
    "https": "socks5h://127.0.0.1:9150"
}


print("Checking IP through Tor...")

tor_ip = get_public_ip(tor_session)

print("Your Tor IP:", tor_ip)


if original_ip != tor_ip and not tor_ip.startswith("Error"):
    print("\nSUCCESS!")
    print("Your externally visible IP changed.")
else:
    print("\nTor connection could not be verified.")