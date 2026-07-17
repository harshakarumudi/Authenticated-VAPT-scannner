from idor_scanner import run_idor_scan
from privilege_scanner import run_privilege_scan
from report_generator import generate_summary
from exporter import export_json
from endpoint_discovery import discover_endpoints

def run_scan():

    discover_endpoints()

    idor = run_idor_scan()
    privilege = run_privilege_scan()

    summary = generate_summary(idor, privilege)

    export_json(summary)

    return summary