from typing import Tuple
import random

#assign a random value to randNum
randNum = random.randint(100, 200)

#function wich will check and print a maxim 
#sqr(value) before randNum 

def four_squares(n: int) -> Tuple[int, int, int, int]:
    res = {}
    for a in range(10):
        for b in range(10):
            for c in range(10):
                for d in range(10):
                    #print(a**2+b**2+c**2+d**2)
                    if a**2+b**2+c**2+d**2 == n:
                        lol = [a, b, c, d]
                        print(lol)
                        if lol not in res:
                            res.append(lol)
    return res
                    
print(four_squares(randNum))