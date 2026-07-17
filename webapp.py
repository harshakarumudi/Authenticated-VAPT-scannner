from flask import Flask, render_template
from main import run_scan

app = Flask(__name__)

# ✅ NEW: severity counter
def count_severity(results):
    counts = {"high": 0, "medium": 0, "low": 0, "critical": 0}

    for r in results:
        sev = r.get("severity", "low")
        if sev in counts:
            counts[sev] += 1

    return counts


@app.route("/")
def dashboard():

    results = run_scan()

    idor = results["idor"]
    privilege = results["privilege"]

    # ✅ NEW: calculate severity distribution
    idor_sev = count_severity(idor)
    priv_sev = count_severity(privilege)

    total_severity = {
        "critical": idor_sev["critical"] + priv_sev["critical"],
        "high": idor_sev["high"] + priv_sev["high"],
        "medium": idor_sev["medium"] + priv_sev["medium"],
        "low": idor_sev["low"] + priv_sev["low"]
    }

    return render_template(
        "dashboard.html",
        idor=idor,
        privilege=privilege,
        frameworks=results["frameworks"],
        severity=total_severity   # ✅ NEW
    )


if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)