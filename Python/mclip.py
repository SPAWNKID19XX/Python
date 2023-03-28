<<<<<<< HEAD
#! python3
# mclip.py - A multi-clipboard program.

TEXT = {'agree': """Yes, I agree. That sounds fine to me.""",
        'busy': """Sorry, can we do this later this week or next week?""",
        'upsell': """Would you consider making this a monthly donation?"""}

import sys, pyperclip
if len(sys.argv) < 2:
    print('Usage: py mclip.py [keyphrase] - copy phrase text')
    sys.exit()

keyWord = sys.argv[1]    # first command line arg is the keyphrase

if keyWord in TEXT:
    pyperclip.copy(TEXT[keyWord])
    print('Text for ' + keyWord + ' copied to clipboard.')
else:
=======
#! python3
# mclip.py - A multi-clipboard program.

TEXT = {'agree': """Yes, I agree. That sounds fine to me.""",
        'busy': """Sorry, can we do this later this week or next week?""",
        'upsell': """Would you consider making this a monthly donation?"""}

import sys, pyperclip
if len(sys.argv) < 2:
    print('Usage: py mclip.py [keyphrase] - copy phrase text')
    sys.exit()

keyWord = sys.argv[1]    # first command line arg is the keyphrase

if keyWord in TEXT:
    pyperclip.copy(TEXT[keyWord])
    print('Text for ' + keyWord + ' copied to clipboard.')
else:
>>>>>>> 2e949e990693a6f7fd6e5331c39ade638c4d7d45
    print('There is no text for ' + keyWord)