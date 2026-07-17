# 🔐 Authenticated VAPT Scanner

A Python-based **Authenticated Vulnerability Assessment and Penetration Testing (VAPT)** tool designed to identify authorization flaws in authenticated web applications.

The scanner automates authenticated request analysis to detect security vulnerabilities such as **Insecure Direct Object Reference (IDOR)** and **Privilege Escalation** by mutating requests and comparing server responses.

---

## 📌 Features

- 🔑 Authenticated Web Application Scanning
- 🔍 Automatic Endpoint Discovery
- 🧪 Request Mutation Engine
- 🚨 IDOR Detection
- 👑 Privilege Escalation Detection
- 📊 JSON Report Generation
- 📝 Formatted Report Export
- 🌐 Web Dashboard
- ⚙️ Modular Architecture

---

## 🏗️ Project Structure

```
authenticated-vapt-scanner/
│
├── analyzer.py              # Response analysis engine
├── config.py                # Configuration settings
├── endpoint_discovery.py    # Finds accessible endpoints
├── exporter.py              # Export scan results
├── idor_scanner.py          # IDOR detection module
├── main.py                  # Main application
├── mutator.py               # Request mutation engine
├── privilege_scanner.py     # Privilege escalation detection
├── report_generator.py      # Generates reports
├── request_engine.py        # Sends HTTP requests
├── scanner.py               # Scan orchestration
├── webapp.py                # Flask web interface
│
├── templates/
│   └── dashboard.html       # Dashboard UI
│
├── reports/                 # Generated JSON reports
│
└── README.md
```

---

## ⚙️ Technologies Used

- Python 3.x
- Flask
- Requests
- JSON
- HTML
- CSS

---

## 🚀 How It Works

1. Authenticate into the target application.
2. Discover accessible endpoints.
3. Capture authenticated requests.
4. Generate mutated requests.
5. Replay requests with modified parameters.
6. Compare responses.
7. Detect:
   - IDOR
   - Privilege Escalation
8. Generate JSON and formatted reports.

---

## 🔍 Vulnerabilities Detected

### ✅ Insecure Direct Object Reference (IDOR)

Tests whether object identifiers (IDs, UUIDs, usernames, etc.) can be modified to access unauthorized resources.

Example:

```
GET /api/user/101
```

↓

```
GET /api/user/102
```

If sensitive data is returned, an IDOR vulnerability is reported.

---

### ✅ Privilege Escalation

Checks whether a lower-privileged authenticated user can perform administrative actions by modifying requests.

Example:

```
POST /admin/delete-user
```

If the request succeeds without administrator privileges, it is flagged.

---

## 📊 Output

The scanner generates:

- JSON Reports
- Formatted Security Reports
- Dashboard View

Example output:

```
Scan Started...

✔ Endpoint discovered
✔ Testing IDOR
✔ Testing Privilege Escalation

---------------------------------

HIGH
IDOR detected
/api/users/102

MEDIUM
Privilege Escalation Possible
/admin/delete

---------------------------------

Report Saved
```

---

## 📁 Sample Reports

Generated reports are stored as:

```
report_124520.json
report_131708.json
report_133322.json
...
```

---

## ▶️ Running the Project

Clone the repository

```bash
git clone https://github.com/yourusername/authenticated-vapt-scanner.git
```

Navigate into the project

```bash
cd authenticated-vapt-scanner
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
python main.py
```

Or launch the web interface

```bash
python webapp.py
```

---

## 📈 Future Improvements

- JWT Authentication Support
- OAuth Authentication
- Role-based User Enumeration
- CSRF Detection
- Broken Access Control Detection
- GraphQL API Testing
- Rate Limiting Detection
- PDF Report Generation
- Multi-threaded Scanning
- OWASP Top 10 Coverage

---

## ⚠️ Disclaimer

This project is intended **only for educational purposes and authorized security testing**.

Do **NOT** use this tool against systems without explicit permission. Unauthorized security testing may violate laws and regulations.

---

## 👨‍💻 Author

Harsha Vardhan Reddy

Cyber Security Student | VAPT | Python | Web Security

GitHub: https://github.com/yourusername
