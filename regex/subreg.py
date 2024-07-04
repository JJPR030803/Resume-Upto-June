import re

caseInsensReg = re.compile(r'robocop',re.I)
print(caseInsensReg.search('Robocop es muy ROBOCOP').group())


namesRegex = re.compile(r'Agent \w+')

print(namesRegex.sub('CENSORED','Agent Alice gave the secret document to Agent BOB'))

agentNamesRegex = re.compile(r'Agent (\w)\w*')

print(agentNamesRegex.sub(r'\1****', 'Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent.'))