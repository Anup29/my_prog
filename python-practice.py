main_string = "Hello, world!"
substring = "world"
res= main_string.find(substring)
print("Found" if res != -1 else "Not found")
import re
print("Found" if re.search(substring, main_string) else "Not found")

#Email Regex: [a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}
def find_email(text):
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    email_add = re.findall(email_pattern, text)
    return email_add

text = "Please  user@mail.server.com contact \"user@domain\"@example.com us at support@example.com for further information. You can also reach out to sales@company.org."
emails = find_email(text)
print(emails)

#Merge given two list
l1 = [1,2,3]
l2 = [5,6,[7,8],9]
print([*l1, *l2])