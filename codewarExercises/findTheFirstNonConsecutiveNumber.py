arr = [1,2,3,4,5,6,7,8]

def first_non_consecutive(arr):
    num = arr[0]
    for i in range(len(arr)):
        if num != arr[i]:
            return arr[i]
        num += 1
        
print(first_non_consecutive(arr))