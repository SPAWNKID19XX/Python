from typing import Tuple
import random

#assign a random value to randNum
randNum = random.randint(2**10, 2**15)

#function wich will check and print a maxim 
#sqr(value) before randNum 

def four_squares(n: int) -> Tuple[int, int, int, int]:
    for a in range(100):
        for b in range(100):
            for c in range(100):
                for d in range(100):
                    #print(a**2+b**2+c**2+d**2)
                    if a**2+b**2+c**2+d**2 == n:
                        return a, b, c, d
                    
print(four_squares(randNum))