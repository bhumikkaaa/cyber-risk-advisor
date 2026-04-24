def calculate_risk(issues, context):
    score = 0

    for issue in issues:
        if "Port" in issue:
            score += 20
            if context["network"] == "public":
                score += 30

        if "Password" in issue:
            score += 25
            if context["user_role"] == "admin":
                score += 25

    if score >= 70:
        return score, "HIGH"
    elif score >= 40:
        return score, "MEDIUM"
    else:
        return score, "LOW"
