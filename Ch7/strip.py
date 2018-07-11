'''
Ch7 Practice Project - Regex version of strip()

If no argument is passed, then whitespace characters are removed
from beginning and end of string

Otherwise, the character specified in the second argument to the function
will be removed from the string

'''

import re

# strip command
def strip(string, character=''):
# strip whitespace at beginnging or end if no second argument
    if character == '':
        #replace whitespice at beginning
        lspaceRegex = re.compile(r'^\s+')
        temp = lspaceRegex.sub('',str(string))
        #replace whitespice at the end
        rspaceRegex = re.compile(r'\s+$')
        print(rspaceRegex.sub('',str(temp)))
# strip character of second argument
    else:
        temp2 = str(character)
        charRegex = re.compile(temp2)
        print(charRegex.sub('', str(string))

strip('   The cat in the hat   ')
strip('   The cat in the hat   ', 'a')
strip('   The cat in the hat   ', 'ca')
