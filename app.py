from flask import Flask, render_template, request
from scanner import check_port, check_password
from risk_engine import calculate_risk
from advisor import suggest
from report import generate_report
import os

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        password = request.form["password"]
        network = request.form["network"]
        role = request.form["role"]

        context = {"network": network, "user_role": role}
        issues = []

        # Check Port
        port_issue = check_port(21)
        if port_issue:
            issues.append(port_issue)

        # Check Password
        pass_issue = check_password(password)
        if pass_issue:
            issues.append(pass_issue)

        # Risk Calculation
        score, level = calculate_risk(issues, context)

        # Suggestions
        suggestions = [suggest(i, context) for i in issues]

        # Generate Report
        generate_report(issues, score, level)

        return render_template("index.html",
                               issues=issues,
                               score=score,
                               level=level,
                               suggestions=suggestions)

    return render_template("index.html")


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
