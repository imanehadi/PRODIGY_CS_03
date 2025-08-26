
import re
import json
import argparse
from getpass import getpass
from dataclasses import dataclass
from typing import List, Dict


SPECIAL_CHARS = "!@#$%^&*()_+-=[]{}|;:'\",.<>/?`~"
SPECIALS_PATTERN = "[" + re.escape(SPECIAL_CHARS) + "]"

@dataclass
class CheckResult:
    strength: str
    score: int
    max_score: int
    suggestions: List[str]
    details: Dict[str, bool]

def evaluate_password(password: str, min_length: int = 8) -> CheckResult:
    length_ok = len(password) >= min_length
    lower_ok = re.search(r"[a-z]", password) is not None
    upper_ok = re.search(r"[A-Z]", password) is not None
    digit_ok = re.search(r"\d", password) is not None
    special_ok = re.search(SPECIALS_PATTERN, password) is not None

    checks = {
        "length": length_ok,
        "lowercase": lower_ok,
        "uppercase": upper_ok,
        "digit": digit_ok,
        "special": special_ok,
    }

    score = sum(1 for v in checks.values() if v)
    max_score = len(checks)

    if score == 5:
        strength = "Very Strong"
    elif score == 4:
        strength = "Strong"
    elif score == 3:
        strength = "Moderate"
    elif score == 2:
        strength = "Weak"
    else:
        strength = "Very Weak"

    suggestions: List[str] = []
    if not length_ok:
        suggestions.append(f"Use at least {min_length} characters.")
    if not lower_ok:
        suggestions.append("Add at least one lowercase letter (a-z).")
    if not upper_ok:
        suggestions.append("Add at least one uppercase letter (A-Z).")
    if not digit_ok:
        suggestions.append("Add at least one number (0-9).")
    if not special_ok:
        suggestions.append("Add at least one special character (e.g. !@#$%^&*).")

    return CheckResult(
        strength=strength,
        score=score,
        max_score=max_score,
        suggestions=suggestions,
        details=checks,
    )

def main():
    parser = argparse.ArgumentParser(description="Password Complexity Checker")
    parser.add_argument("-p", "--password", help="Password to check (unsafe on shared shells)")
    parser.add_argument("--min-length", type=int, default=8, help="Minimum length requirement (default: 8)")
    parser.add_argument("--json", action="store_true", help="Output result as JSON")
    args = parser.parse_args()

    pwd = args.password if args.password is not None else getpass("Password (hidden input): ")

    result = evaluate_password(pwd, min_length=args.min_length)

    if args.json:
        print(json.dumps({
            "strength": result.strength,
            "score": result.score,
            "max_score": result.max_score,
            "suggestions": result.suggestions,
            "details": result.details,
        }, indent=2))
    else:
        print(f"Strength: {result.strength}")
        print(f"Score: {result.score}/{result.max_score}")
        if result.suggestions:
            print("Suggestions:")
            for s in result.suggestions:
                print(f" - {s}")

if __name__ == "__main__":
    main()

