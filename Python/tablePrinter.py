tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]


def lenWord(arr):
    maxLen = [0] * len(arr)
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if len(arr[i][j]) > maxLen[i]:
                maxLen[i] = len(arr[i][j])
    return maxLen

def printTable(arr, arrLen):
    for row in range(len(arr[0])):
        print(arr[0][row].rjust(arrLen[0]), arr[1][row].rjust(arrLen[1]), arr[2][row].rjust(arrLen[2]))  



 
printTable(tableData, lenWord(tableData))