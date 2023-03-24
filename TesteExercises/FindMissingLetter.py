#python 3.10.8

'''
Write a method that takes an array of consecutive (increasing) letters as input and returns the missing letter in the array.
You will always receive a valid array and it will always be missing exactly one letter. The length of the array will always be at least 2.
The array will always contain letters in only one case.
'''
a = ["a", "b", "c", "d", "f"]

def misLatter(arr):
    for i, latter in enumerate(arr):
        if ord(latter)+1 != ord(arr[i+1]):
            str = "{} => {}".format(arr , chr(ord(latter)+1))
            return str


print(misLatter(a))