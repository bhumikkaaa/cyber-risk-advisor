# Context-Aware Cybersecurity Risk Advisor

A Python-based Governance, Risk, and Compliance (GRC) tool that analyzes system vulnerabilities and dynamically evaluates risk using context-aware security models.

This project demonstrates how security risk can change based on environmental factors such as network type (public or private) and user role (admin or standard user).

---

## Key Highlights

* Developed a context-aware risk scoring engine for dynamic security assessment
* Implemented port scanning and password strength analysis modules
* Designed adaptive risk classification (Low, Medium, High)
* Built a recommendation system for vulnerability mitigation
* Created a Flask-based web interface for real-time analysis
* Generated structured security risk reports

---

## Tech Stack

* Python
* Flask
* Socket Programming
* HTML

---

## Core Concept

Traditional security tools assign fixed risk levels.
This system introduces context-aware cybersecurity where risk varies based on usage conditions.

Examples:

* Weak password + Admin user → High Risk
* Weak password + Standard user → Medium Risk
* Open port + Public network → High Risk

---

## Project Structure

cyber-risk-advisor/
│
├── app.py
├── scanner.py
├── risk_engine.py
├── advisor.py
├── report.py
├── requirements.txt
│
├── templates/
│   └── index.html

---

## How to Run

1. Install dependencies
   pip install -r requirements.txt

2. Run the application
   python app.py

3. Open in browser
   http://127.0.0.1:5000

---

## Live Demo

(Add your Render deployment link here)

---

## Sample Output

Issues Detected:

* Weak Password
* Port 21 Open

Context:

* Public Network
* Admin User

Risk Level: High

Recommendations:

* Disable FTP or use secure alternatives
* Use strong password policies

---

## Use Cases

* Cybersecurity Risk Assessment
* Compliance Monitoring
* GRC Analysis
* Security Awareness Training

---

## Future Scope

* AI-based threat detection
* Cloud compliance integration (AWS, Azure)
* User authentication system
* Dashboard visualization

---

## Author

Bhumika Priyadarshini
B.Tech CSE (Cyber Security)

---

## License

This project is for academic and educational purposes.
