import re


def is_strong_password(password):
    # Check length
    if len(password) < 8:
        return False
    # Check for at least one uppercase letter
    if not re.search(r"[A-Z]", password):
        return False
    # Check for at least one lowercase letter
    if not re.search(r"[a-z]", password):
        return False
    # Check for at least one digit
    if not re.search(r"\d", password):
        return False
    # Check for at least one symbol
    if not re.search(r"[@_!#$%^&*()<>?/\|}{~:]", password):
        return False
    return True


def main():
    password = input("Enter a password: ")
    if is_strong_password(password):
        print("Strong password!")
    else:
        print("Weak password!")


if __name__ == "__main__":
    main()
