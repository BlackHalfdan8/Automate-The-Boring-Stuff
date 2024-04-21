import re

common_passwords = [
    "password",
    "123456",
    "qwerty",
    "12345678",
]  # Commonly used passwords to avoid


def is_strong_password(password):
    # Check length
    if len(password) < 12:
        return False
    # Check for complexity
    if not re.search(r"[A-Z]", password):
        return False
    if not re.search(r"[a-z]", password):
        return False
    if not re.search(r"\d", password):
        return False
    if not re.search(r"[@_!#$%^&*()<>?/\|}{~:]", password):
        return False
    # Check for uniqueness (not reusing passwords)
    if password in common_passwords:
        return False
    return True


def main():
    password = input("Enter a password: ")

    if is_strong_password(password):
        print("Strong password!")
    else:
        print("Weak password! Please follow NIST guidelines.")


if __name__ == "__main__":
    main()
