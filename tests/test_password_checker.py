import sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))


import subprocess, sys, json
from password_checker import evaluate_password

def test_very_weak():
    r = evaluate_password("a", min_length=8)
    assert r.strength == "Very Weak"
    assert r.score <= 1

def test_weak_lower_only():
    r = evaluate_password("abcdefgh", min_length=8)
    assert r.strength == "Weak"
    # length + lowercase
    assert r.score == 2

def test_strong_missing_special():
    r = evaluate_password("Abcdef12", min_length=8)
    assert r.strength == "Strong"
    assert r.score == 4

def test_very_strong_all_criteria():
    r = evaluate_password("Abcdef12!", min_length=8)
    assert r.strength == "Very Strong"
    assert r.score == 5

def test_json_cli():
    cp = subprocess.run(
        [sys.executable, "password_checker.py", "--password", "Abcdef12!", "--json"],
        capture_output=True, text=True, check=True
    )
    data = json.loads(cp.stdout)
    assert data["strength"] == "Very Strong"
    assert data["score"] == 5
