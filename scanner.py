from config import TEST_IDS
from request_sender import send_request
from analyzer import analyze_responses


def run_scan():
    responses = {}

    print("\n[*] Running IDOR Scan\n")

    for user in TEST_IDS:
        status, body = send_request(user)

        responses[user] = body

        print(f"[+] Testing ID: {user}")
        print(f"    Status Code: {status}")
        print(f"    Response Length: {len(body)}\n")

    vulnerable = analyze_responses(responses)

    if vulnerable:
        print("[!!!] Potential IDOR vulnerability detected")
    else:
        print("[✓] No IDOR detected")