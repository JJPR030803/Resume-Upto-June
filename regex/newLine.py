import re

noNewLine = re.compile(r'.*',re.DOTALL)

print(noNewLine.search('Serve the public trust.\n and protect the innocent.\n Uphold the law').group(0))