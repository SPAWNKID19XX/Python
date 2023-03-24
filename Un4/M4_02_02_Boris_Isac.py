#Python 3.10.8
"""
Ask the user for some text and a word, which we will search within the text. If you find it,
extract from that position to the end, save it to another var, and print it.
• Sample text: Olá mundo que tal
• Search: mundo
• Result: mundo que tal
"""
text = input("Insert some text: ")
searchWord = input("insert some word from text witch you had been inserted before: ")

indx = text.find(searchWord)#save start index of searchWord
result = text[indx:]
print(result)
