import requests
from config import BASE_URL, SESSION_COOKIE

def discover_endpoints():

    cookies = {"session": SESSION_COOKIE}

    try:
        r = requests.get(BASE_URL, cookies=cookies)

        links = set()

        for line in r.text.split('"'):
            if "/" in line and "http" not in line and len(line) < 50:
                links.add(line)

        print("\nDiscovered Endpoints:")
        for l in list(links)[:10]:
            print(l)

    except:
        print("Discovery failed")