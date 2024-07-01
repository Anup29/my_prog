import re

s = input("Enter email address")
m = re.match(r"[a-zA-Z0-9](\w|-|_|\.)+@[a-zA-Z0-9]+\.[a-zA-Z]{1,3}", s)
if m:
    print(f"matched..-> {m.group()}")
else:
    print("no")