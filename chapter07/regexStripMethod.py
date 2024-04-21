import re


def regex_strip(text, chars_to_strip=None):
    if chars_to_strip:
        pattern = f"[{re.escape(chars_to_strip)}]+"
    else:
        pattern = r"^\s+|\s+$"
    return re.sub(pattern, "", text)


# Example usage:
original_text = "   Hello, world!   "
modified_text = regex_strip(original_text)
print("Original Text:", repr(original_text))
print("Modified Text:", repr(modified_text))

custom_stripped_text = regex_strip("...Hello, world!...", ".!")
print("Custom Stripped Text:", repr(custom_stripped_text))
