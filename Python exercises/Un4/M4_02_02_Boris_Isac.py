#Python 3.10.8
"""
Ask the user for some text and a word, which we will search within the text. If you find it,
extract from that position to the end, save it to another var, and print it.
• Sample text: Olá mundo que tal
• Search: mundo
• Result: mundo que tal
"""
text = "Olá mundo que tal"
searchWord = "mundo"

indx = text.find(searchWord)
result = text[indx:]
print(result)
