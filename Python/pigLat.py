#python 3
#PIGLATIM is a game where user will insert some phrase and a 
#script will chack a words
#If first latter is VOWEL then in this word will added 'yay', 
#If consonant letter or more then 1, 
#then it will move to finish of word and then will added 'au'

#create list with VOWEL
import pyperclip

VOWEL = ['a', 'e', 'i', 'o', 'u', 'y']

#user insert phrase
inputMsg = input('Insert some phrase or word: ')
phrase = inputMsg.lower()
#translated variable
PigLatin= [] 


# devide all words from phrase with ' ', 
# and each words devide for letters
splitPhrase= phrase.split(' ')
for word in range(len(splitPhrase)):
    #word with vowel first leter
    if splitPhrase[word][0] in VOWEL:
        splitPhrase[word] = splitPhrase[word] + 'yay'
        PigLatin.append(splitPhrase[word])
    else:
        #modify words with not vowel first leter
        count = 0
        locWordVar = list(splitPhrase[word])
        while splitPhrase[word][count] not in VOWEL:
            count += 1
            divWord1 = ''.join(locWordVar[:count])
            divWord2 = ''.join(locWordVar[count:])
            divWord2 += (divWord1 + 'ua') 
            PigLatin.append(divWord2)
            PigLatin = ' '.join(PigLatin)         


print(PigLatin)