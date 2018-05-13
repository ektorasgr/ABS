spam = ['apples', 'bananas', 'tofu', 'cats']

output = ''
for i in range(len(spam)):
    if i < (len(spam)-1):
        output += str(spam[i]) + ', '
    elif i == (len(spam)-1):
        output += 'and '+ str(spam[i])
        print(output)
