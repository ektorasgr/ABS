'''
this function takes a list of lists of strings and displays it
in a well-organized table with each column right-justified

ABS Ch. 6 Practice Project
'''

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def printTable():
    colWidths = [0] * len(tableData)
