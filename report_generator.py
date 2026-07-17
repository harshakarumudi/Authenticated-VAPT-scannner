def get_severity(result):

    if "Confirmed" in result:
        return "high"
    elif "Potential" in result:
        return "medium"
    elif "Privilege" in result:
        return "critical"
    return "low"


def generate_summary(idor, privilege):

    for r in idor:
        r["severity"] = get_severity(r["result"])

    for r in privilege:
        r["severity"] = get_severity(r["result"])

    return {
        "idor": idor,
        "privilege": privilege,
        "frameworks": {
            "OWASP": "A01: Broken Access Control",
            "MITRE": "T1068: Privilege Escalation"
        }
    }