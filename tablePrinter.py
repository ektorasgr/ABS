'''
this function takes a list of lists of strings and displays it
in a well-organized table with each column right-justified

ABS Ch. 6 Practice Project
'''

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def printTable(Data):
    #find the longest string of each list and store in colWidths
    colWidths = [0] * len(Data)
    for i in range(len(Data)):
        for k in range(len(Data[i])):
            if len(Data[i][k]) > colWidths[i]:
                colWidths[i] = len(Data[i][k])
            #else:
                #continue
    #find the longest string of the sublists and store in longest
    longest = 0
    for i in range(len(colWidths)):
        if colWidths[i] > longest:
            longest = colWidths[i]
        #else:
            #continue
    for i in range(len(Data[i])):
        for k in range(len(Data)):
            if k < (len(Data)-1):
                print(Data[k][i].rjust(longest), end = '')
            else:
                print(Data[k][i].rjust(longest))


printTable(tableData)
