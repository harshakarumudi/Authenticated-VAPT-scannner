from config import ADMIN_ENDPOINTS
from request_engine import send_request_raw

def run_privilege_scan():

    results = []

    for endpoint in ADMIN_ENDPOINTS:

        status, _ = send_request_raw(endpoint)

        if status == 200:
            result = "Potential Privilege Escalation"
        else:
            result = "Access Controlled"

        results.append({
            "endpoint": endpoint,
            "status": status,
            "result": result
        })

    return results