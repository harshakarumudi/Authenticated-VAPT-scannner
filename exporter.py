import json
from datetime import datetime

def export_json(data):

    filename = f"report_{datetime.now().strftime('%H%M%S')}.json"

    with open(filename, "w") as f:
        json.dump(data, f, indent=4)

    print(f"[+] Report saved: {filename}")