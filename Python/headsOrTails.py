import random

arr = []
    
def FuelPossibilities():
    for i in range(100000):
        HT = random.randint(0, 1)
        if HT == 0:
            arr.append('H')
        else:
            arr.append('T')        
    return arr

def Search(arr):
    count = 1
    inLine = 0
    #print(arr)
    for i in range(len(arr) - 1):
        #print(arr[i] + ' and ' + arr[i+1])
        if arr[i] == arr[i+1]:
            count += 1
            if count > 5:
                inLine +=1
                count =  1
            #print('Added' + str(count))
        else:
            #print('Clear')
            count = 1
    print('Identical elements in row ' + str(inLine) + ' time(s)')

Search(FuelPossibilities())