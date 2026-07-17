def analyze(base_status, base_body, status, body):

    if status == 200 and body != base_body:
        return "Confirmed IDOR"

    if status != base_status:
        return "Potential IDOR"

    return "No vulnerability"