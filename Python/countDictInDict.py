import pprint

allGuess = {
    'Aaron' : {'Apple' : 3, 'Orange' : 3, 'Banana' : 3},
    'Emily' : {'Apple' : 3, 'juice' : 2, 'Bun' : 5},
    'Boris' : {'Bun' : 5, 'Banana' : 3, 'Candies' : 10},
    'Natasha' : {'Candies' : 10, 'Apple' : 3, 'juice' : 2, 'Bun' : 5, 'Candies' : 10}
}
productItems = {}
totalProductList = {}

def countProducts(guess):
    listAllGuess = list(guess)# List All Peaple   
    for i in range(len(listAllGuess)):
        productGuess = list(guess[listAllGuess[i]])
        #Creating new dictionaries with list of items
        for j in range(len(productGuess)):
            item = productGuess[j]
            if item not in productItems: 
                productItems[item] = 0
        
        #startin to regist and count total of items
        for key in productItems.keys():
            if key in guess[listAllGuess[i]]:
                productItems[key] += guess[listAllGuess[i]][key] 
    return productItems
    
    
                


print(countProducts(allGuess))