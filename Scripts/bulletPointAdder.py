#! python3
# bulletPointAdder.py - Adds bullet points to the start
# of each line on the clipboard

import pyperclip
text = pyperclip.paste()

# Seperate lines and add stars.
lines = text.split('\n')
for i in range(len(lines)): #loop through all the indexes in the "lines" list
    lines[i] = '* ' + lines[i] # add start to each string in "lines" list
text = '\n'.join(lines)
pyperclip.copy(text)
