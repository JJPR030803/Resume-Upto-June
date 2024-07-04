import re

batRegex = re.compile(r'bat(wo)*man')
batRegex2 = re.compile(r'bat(wo)+man')

mo1 = batRegex.search('The adventures of batwowowowowoman')
mo2 = batRegex2.search('The adventures of batwowowowowoman')
mo3 = batRegex2.search('The adventures of batman')
print(mo3 == None)