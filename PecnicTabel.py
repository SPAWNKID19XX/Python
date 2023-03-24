def printPicnicList(leftSize, rightSize, productList):
    print('GET TO PECNIC'.center(leftSize + rightSize, '*'))
    for key, value in productList.items():
        print(key.ljust(leftSize, '=') + str(value).rjust(rightSize, '='))

productList = {'Aaple': 20, 'Cuckies': 8000, 'Sandwitch': 15, 'Buns':9}
printPicnicList(10, 10, productList)