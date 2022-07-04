#script will say you hello
#and after thet wil quest you what is your name

print ('Hello world!')
print ('What is your name?')
nameUser = input()  #request to name
lengthNameUser = len(nameUser)
print('Nice to meet you mr ' + nameUser)
print ('A length of your name is', lengthNameUser , 'laters.')
print('How old are you?')
ageUser = input()               #request age
print ('The next year you will be ' + str(int(ageUser) + 1)  + ' years old.' )
