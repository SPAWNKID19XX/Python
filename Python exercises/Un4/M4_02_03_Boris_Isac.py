#Python 3.10.8
"""
Starting from a sentence with different words separated by spaces, create a list where the
elements are every word of the text. Show this list and the number of times it is found
word “world” in this list.
"""
text = "Olá mundo mundo que tal mundo estás"
myList = text.split()


def countMundo(word, myList = []):
    cntMundo = 0
    for obj in myList:
        if obj == word:
            cntMundo += 1
    return cntMundo

result = countMundo("mundo", myList)
print(text)
print("Result:",result)