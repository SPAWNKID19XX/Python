#python3
#script will lind all ' ' and submit by secound arument ''

import re
text = '   hello world    !!!!  !!'

print(text)

stripRegex = re.compile(r'''
    \s  +
''',re.VERBOSE) 

finalText = stripRegex.sub('', text)
print(finalText)