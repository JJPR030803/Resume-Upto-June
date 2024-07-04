import re


tel = "1234567ad5"

telRegex = re.compile(r"\d+")
mo = telRegex.search(tel)
if mo:
    print(mo.group())


