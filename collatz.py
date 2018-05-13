def collatz(number):
    if number % 2 == 0:
        #print(str(number) + ' // 2')
        number = number / 2
        return number
    else:
        #print('3 * ' + str(number) + ' + 1')
        number = 3 * number + 1
        return number

print('Type in a number')
try:
    spam = int(input())
    while spam != 1:
        spam = collatz(spam)
        print(str(int(spam)))
except ValueError:
    print("Error: Please type an integer")
