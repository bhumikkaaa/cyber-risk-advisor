import os

def generate_report(issues, score, level):
    os.makedirs("reports", exist_ok=True)

    with open("reports/report.txt", "w") as f:
        f.write("Cyber Risk Report\n")
        f.write("====================\n\n")

        f.write("Issues Found:\n")
        for i in issues:
            f.write(f"- {i}\n")

        f.write(f"\nRisk Score: {score}")
        f.write(f"\nRisk Level: {level}\n")
