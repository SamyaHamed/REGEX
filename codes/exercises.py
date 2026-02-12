import re

"""
Exercise 1 — Find consecutive repeated words
Task:
Write a regex to find all words that are repeated consecutively in the text.

Input:
text = "This is is a test test string and and another test."

Expected Output:

is
test
and

"""

TEXT1 = "This is is a test test string and and another test."
PATTERN1 = r"\b([a-zA-Z]+)\s+\1\b"
print("result1 :")
matches = re.findall(PATTERN1, TEXT1, flags=re.IGNORECASE)
print(matches)


"""
Exercise 2 — Extract valid hashtags

Task:
Write a regex to extract hashtags that contain only letters (ignore numbers and special characters).

Input:

text = "I love #python and #regex but not #123 or #!"


Expected Output:

python
regex

"""

TEXT2 = "I love #python and #regex but not #123 or #!"
PATTERN2 = r"#([a-zA-Z]+)"
print("result2:")
for match in re.finditer(PATTERN2, TEXT2):
    print(match.group(1))


"""
Exercise 3 — Validate a strong password

Task:
Write a regex to validate a password with these rules:

At least one uppercase letter

At least one lowercase letter

At least one digit

Minimum length of 8 characters

Test Cases:

Password1    valid
password1    invalid
PASSWORD1    invalid
Pass1        invalid

"""


passwords = ["Password1", "password1", "PASSWORD1", "Pass1"]
PATTERN3 = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{8,}$"
print("result3 :")
for pwd in passwords:
    if re.match(PATTERN3, pwd):
        print(f"{pwd}  valid")
    else:
        print(f"{pwd}  invalid")


"""
Exercise 4 — Reformat phone numbers

Task:
Write a regex to reformat phone numbers from 0591234567 to 059-123-4567.

Input:

text = "Call me at 0591234567 or 0569876543"


Expected Output:

059-123-4567
056-987-6543

"""
TEXT4 = "Call me at 0591234567 or 0569876543"
PATTERN4 = r"(\d{3})(\d{3})(\d{4})"
new_text = re.sub(PATTERN4, r"\1-\2-\3", TEXT4)
print("result4:")
print(new_text)


"""
Exercise 5 — Extract text inside parentheses (non-nested)

Task:
Write a regex to extract text inside parentheses, but ignore nested parentheses.

Input:

text = "Example (first) and (second value) but not (third (nested))"


Expected Output:

first
second value
nested


Hint: Use non-greedy quantifiers.
"""

TEXT5 = "Example (first) and (second value) but not (third (nested))"
PATTERN5 = r"\(([^()]+)\)"
print("result5:")
for match in re.finditer(PATTERN5, TEXT5):
    print(match.group(1))


"""
Exercise 6 (Challenge) — Extract prices

Task:
Write a regex to extract all valid prices in the text.

A valid price starts with $

Can be integer or decimal

Ignore invalid prices like $abc or numbers without $

Input:

text = "Price: $45.99, $100, and $5.5 but not 45.99 or $abc"


Expected Output:

45.99
100
5.5
"""

TEXT7 = "Price: $45.99, $100, and $5.5 but not 45.99 or $abc"
PATTERN7 = r"\$(\d+\.?\d+)"
print("result7 :")
result7 = re.findall(PATTERN7, TEXT7)
print(result7)
