#  Password Complexity Checker (Python)

A simple command-line tool that evaluates the strength of a password based on security best practices.  
It checks **length, lowercase letters, uppercase letters, numbers, and special characters** and provides feedback to help users improve their passwords.

---

## Features
-  Checks if password meets minimum length (default: 8 characters, customizable).
-  Verifies presence of:
  - Lowercase letters  
  - Uppercase letters  
  - Numbers  
  - Special characters (`!@#$%^&*` etc.)
-  Gives a **strength score** and a **rating** (Very Weak → Very Strong).
-  Provides **suggestions** to improve weak passwords.
-  Supports **JSON output** for automation/integration.
-  Includes **unit tests** (pytest).

---

##  Installation

Clone the repo or copy the script, then create a virtual environment:

```bash
# Clone project (if on GitHub)
git clone https://github.com/your-username/password-checker.git
cd password-checker

# Create virtual environment
python3 -m venv .venv
source .venv/bin/activate

# (Optional) Install test dependencies
pip install -r requirements-dev.txt

🖥Usage
1. Run with secure input (recommended)tall -r requirements-dev.txt
python password_checker.py
It will prompt:
Password (hidden input):
Strength: Moderate
Score: 3/5
Suggestions:
 - Add at least one special character (e.g. !@#$%^&*).
2. Pass password via argument
python password_checker.py --password "Abcdef12!"
3. JSON output
python password_checker.py --password "Abcdef12!" --json
Output:
{
  "strength": "Very Strong",
  "score": 5,
  "max_score": 5,
  "suggestions": [],
  "details": {
    "length": true,
    "lowercase": true,
    "uppercase": true,
    "digit": true,
    "special": true
  }
}
4. Change minimum length
python password_checker.py --password "Abcdef12!" --min-length 12
Run Tests
pytest -q
Expected:
.....                                                                  [100%]
5 passed in 0.15s
Project Structure:
password-checker/
│── password_checker.py        
│── tests/                     
│   └── test_password_checker.py
│── requirements-dev.txt       
│── README.md                 
│── .gitignore
Future Improvements

Check against a list of common breached passwords.

Add entropy-based scoring.

Build a Tkinter GUI or a Flask web app for real-time feedback.


