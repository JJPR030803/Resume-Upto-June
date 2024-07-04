import re

vowelRegex = re.compile(r'[aeiouAEIOU]')
consonantRegex = re.compile(r'[^aeiouAEIOU]')

vocales = vowelRegex.findall('Robocop ate all the baby food')

consonantes = consonantRegex.findall('Robocop eats baby food BABY FOOD')

print(vocales)
print(consonantes)