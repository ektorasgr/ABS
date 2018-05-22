import re

# Set up regex
# this is for 8 character minimum
charRegex = re.compile(r'\S{8,}')
# this checks to make sure we have at least one uppercase letter
upperRegex = re.compile(r'([A-Z])+')
# this checks to make sure we have at least one lowercase letter
lowerRegex = re.compile(r'([a-z])+')
#this checks for at least one digit
numberRegex = re.compile(r'([0-9])+')

# get input
while True:
    print('Please type your password. Type quit to exit')
    password = str(input())

    if password == 'quit':
        break
    elif charRegex.search(password) == None:
        print('Sorry, the password should be at least 8 characters. \
Try again.')
    elif lowerRegex.search(password) == None:
        print('Sorry, the password should contain a lowercase letter. \
Try again.')
    elif upperRegex.search(password) == None:
        print('Sorry, the password should contain an uppercase letter. \
Try again.')
    elif numberRegex.search(password) == None:
        print('Sorry, the password should contain at least one number. \
Try again.')
    else:
        print('Your password is adequate')
        break
