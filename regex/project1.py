import re 


phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My number is 415-555-4242.')
areaCode,mainNumber = mo.groups()
print('Phone number found:'+mo.group(1))
print(areaCode)
print(mainNumber)
print(mo.group(2))
print(mo.group(0))