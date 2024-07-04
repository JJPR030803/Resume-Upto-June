import re

phoneRegex = re.compile(r'''(
    (\d{3|}\(\d{3}\))?  #area code
    (\s|-|\.)? #separador
    \d{3}#primeros 3 digitos
    (\s|-|\.) #separador
    \d{4}
    (\s*(ext|x|ext.)\s*\d{2,5})? #extension
    
    )''',re.VERBOSE)