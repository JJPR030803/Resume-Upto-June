import re

heroRegex = re.compile(r'Batman|Tina Fey')
batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo1 = heroRegex.search('Batman and Tina Fey')
mo2 = heroRegex.search('Tina Fey and Batman')
mo3 = batRegex.search('Batmobile lost a wheel')
print(mo3.group())
print(mo3.group(1))