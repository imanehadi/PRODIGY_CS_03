# 🔐 Password Complexity Checker (Python)

A simple command-line tool that evaluates the strength of a password based on security best practices.  
It checks **length, lowercase letters, uppercase letters, numbers, and special characters** and provides feedback to help users improve their passwords.

---

## ✨ Features
- ✅ Checks if password meets minimum length (default: 8 characters, customizable).  
- ✅ Verifies presence of:
  - Lowercase letters  
  - Uppercase letters  
  - Numbers  
  - Special characters (`!@#$%^&*` etc.)  
- ✅ Gives a **strength score** and a **rating** (Very Weak → Very Strong).  
- ✅ Provides **suggestions** to improve weak passwords.  
- ✅ Supports **JSON output** for automation/integration.  
- ✅ Includes **unit tests** (pytest).  

---

## ⚙️ Installation, Usage & Tests

```bash
================= ⚙️ INSTALLATION =================
cd password-checker

# Create virtual environment
python3 -m venv .venv
source .venv/bin/activate

# (Optional) Install test dependencies
pip install -r requirements-dev.txt
===================================================


================= 🖥 USAGE =========================
# 1) Run with secure input
python password_checker.py
# Example prompt:
# Password (hidden input):
# Strength: Moderate
# Score: 3/5
# Suggestions:
#  - Add at least one special character (e.g. !@#$%^&*).

# 2) Pass password via argument
python password_checker.py --password "Abcdef12!"

# 3) JSON output
python password_checker.py --password "Abcdef12!" --json

# Example Output:
# {
#   "strength": "Very Strong",
#   "score": 5,
#   "max_score": 5,
#   "suggestions": [],
#   "details": {
#     "length": true,
#     "lowercase": true,
#     "uppercase": true,
#     "digit": true,
#     "special": true
#   }
# }

# 4) Change minimum length
python password_checker.py --password "Abcdef12!" --min-length 12
===================================================


================= 🧪 RUN TESTS =====================
pytest -q

# Expected output:
# .....                                                                  [100%]
# 5 passed in 0.15s
===================================================



