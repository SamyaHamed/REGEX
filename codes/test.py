"""library to use regex "regular expression" in python"""

import re

# 1 :
TEXT = "Contact us at support@gmail.com or sales@company.org for more info.Call 059-123-4567 or 056-999-8888 now!"
PATTERN1 = r"[\w\.-]+@[\w\.-]+\.\w+"
emails = re.findall(PATTERN1, TEXT)
print(emails)


# 2:
PATTERN2 = r"\d+\-\d+\-\d+"
number = re.findall(PATTERN2, TEXT)
print(number)

# 3
TEXT2 = "My score is 95 and yours is 88."
PATTERN3 = r"\d+"
new_text = re.sub(PATTERN3, " ", TEXT2)
print(new_text)

# 4
TEXT3 = "HelloWorld"
TEXT4 = "Hello123"
PATTERN4 = r"[A-Za-z]+"
r1 = bool(re.fullmatch(PATTERN4, TEXT3))
r2 = bool(re.fullmatch(PATTERN4, TEXT4))
print(f"r1 = {r1}", f"r2= {r2}")


# 5
TEXT5 = "Files: report.pdf image.png script.py"
PATTERN5 = r"[a-z]+\.[a-z]+"
for result in re.finditer(PATTERN5, TEXT5):
    print(result.group())

# 6
TEXT6 = "Today is 2026-02-11"
PATTERN6 = r"(\d{4})-(\d{2})-(\d{2})"
new_text6 = re.sub(PATTERN6, r"\3/\2/\1", TEXT6)
print(new_text6)


# 7
HTML = "<html><title>My Website</title></html>"
title_search = re.search(r"<title>(.*)</title>", HTML, re.IGNORECASE)
if title_search:
    title = title_search.group(1)
    print(title)
