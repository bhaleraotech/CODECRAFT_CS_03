import re

def check_password_strength(password):
    strength_points = 0
    remarks = []

    # Length check
    if len(password) >= 8:
        strength_points += 1
    else:
        remarks.append("Password should be at least 8 characters long.")

    # Uppercase check
    if re.search(r"[A-Z]", password):
        strength_points += 1
    else:
        remarks.append("Add at least one uppercase letter (A-Z).")

    # Lowercase check
    if re.search(r"[a-z]", password):
        strength_points += 1
    else:
        remarks.append("Add at least one lowercase letter (a-z).")

    # Digit check
    if re.search(r"[0-9]", password):
        strength_points += 1
    else:
        remarks.append("Add at least one number (0-9).")

    # Special character check
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        strength_points += 1
    else:
        remarks.append("Add at least one special character (!@#$...).")

    # Strength level
    if strength_points <= 2:
        strength = "Weak ❌"
    elif strength_points == 3:
        strength = "Medium ⚠️"
    elif strength_points == 4:
        strength = "Strong ✅"
    else:
        strength = "Very Strong 🔥"

    return strength, remarks


# -------- Main Program --------
print("===== Password Complexity Checker =====")
password = input("Enter password: ")

strength, feedback = check_password_strength(password)

print("\nPassword Strength:", strength)

if feedback:
    print("\nSuggestions to improve:")
    for item in feedback:
        print("-", item)
else:
    print("Your password is strong and secure! 👍")
