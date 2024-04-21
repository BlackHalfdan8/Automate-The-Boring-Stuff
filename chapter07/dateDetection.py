import re


def date_detection(text):
    # Define the regular expression pattern
    date_pattern = re.compile(r"(\d{1,2})[-/](\d{1,2})[-/](\d{4})")

    # Find all matches in the text
    matches = date_pattern.findall(text)

    # Process and validate the matches
    for match in matches:
        day, month, year = map(int, match)
        if is_valid_date(day, month, year):
            print(f"Found valid date: {day:02d}/{month:02d}/{year}")
        else:
            print(f"Invalid date: {day:02d}/{month:02d}/{year}")


def is_valid_date(day, month, year):
    # Simple validation for day, month, and year ranges
    if year < 1000 or year > 2999:
        return False
    if month < 1 or month > 12:
        return False
    if day < 1 or day > 31:
        return False
    if month in [4, 6, 9, 11] and day > 30:
        return False
    if month == 2:
        if day > 29:
            return False
        if day == 29 and not (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)):
            return False
    return True


# Test the program with sample text
sample_text = """
Today's date is 25/04/2024, and tomorrow will be 26-04-2024.
However, the date 31/04/2024 is invalid, and so is 29/02/2023.
"""
date_detection(sample_text)
