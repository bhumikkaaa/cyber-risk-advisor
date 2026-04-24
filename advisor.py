def suggest(issue, context):
    if "Port" in issue:
        if context["network"] == "public":
            return "Disable FTP or use SFTP immediately"
        return "Monitor open ports regularly"

    if "Password" in issue:
        return "Use strong password (12+ chars, symbols, numbers)"

    return "No suggestion available"
