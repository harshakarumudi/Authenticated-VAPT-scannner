from mutator import generate_payloads
from request_engine import send_request
from analyzer import analyze

def run_idor_scan():

    payloads = generate_payloads()
    base_status, base_body = send_request(payloads[0])

    results = []

    for payload in payloads:
        status, body = send_request(payload)
        result = analyze(base_status, base_body, status, body)

        results.append({
            "object": payload,
            "status": status,
            "result": result
        })

    return results