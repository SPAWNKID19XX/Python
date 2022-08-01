spam = ['яблоки', 'бананы', 'тофу', 'коты']


def printList(arr, leng):  
    lenArr = len(arr)
    count = 0
    while count < lenArr - 2:
        print(arr[count], end=', ')
        count += 1
    print(str(arr[lenArr-2]) + ' and ' + str(arr[lenArr-1]) + '.')

printList(spam, len(spam))