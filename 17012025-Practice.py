import re

sentense="XYZ12345 this is My ID"

pattern=r"(XYZ\d+)"

match=re.search(pattern,sentense)

if match:
    employee_id=match.group(1)
    print("MY ID is: ",employee_id)
else:
    print("ID not Found")

