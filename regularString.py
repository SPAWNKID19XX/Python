#python3
#Soft will find a phoneNumber from Regular Model 
#ex: 0({9}6)-000-0000
import re

msg = 'My number is 096-469-6149, my wife\'s number is 096-469-6179.Call me as soon, as it is possibol.\n My secound Number is 969-696-9696, but I use it just in emerence cases'

phoneNumRegex = re.findall(r'\d\d\d-\d\d\d-\d\d\d\d', msg)
print(phoneNumRegex)
