import requests
import re


result = requests.get('http://www.ipap.ru')
text = result.text
phones = re.findall(r'\b\d\d\d\d\d\d\d\b|\b\d\d\d\d\d\d\d\d\d\d\d\b',text)
print(phones)
emails = re.findall(r'\w+@\w+.\w+',text)
print(emails)


