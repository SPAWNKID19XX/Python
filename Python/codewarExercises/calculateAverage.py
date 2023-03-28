numberList = []

def find_average(numbers):
    # your code here
    total = 0
    total = sum(numbers)
    if numbers:
        return (total/len(numbers))
    else:
        return 0


print(find_average(numberList))