import re


atRegex = re.compile(r'.at')
at = atRegex.findall('The cat in the hat laying at the mat')


nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
mo = nameRegex.search('First Name: Al Last Name: Sweigart')


nonGreedyReg = re.compile(r'<.*?>')
greedyReg = re.compile(r'<.*>')
mo1 = nonGreedyReg.search('<To serve man> For dinner.>')
mo2= greedyReg.search('<To serve man> For dinner.>')

print(mo1.group(0))
print(mo2.group(0))
print(mo.group(2))

print(at)