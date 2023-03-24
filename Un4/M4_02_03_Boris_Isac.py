#Python 3.10.8
"""
Starting from a sentence with different words separated by spaces, create a list where the
elements are every word of the text. Show this list and the number of times it is found
word “world” in this list.
"""
text = "Olá mundo mundo que tal mundo estás"
myList = text.split()

result = myList.count("mundo")
print(text)
print("Result:",result)