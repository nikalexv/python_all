import random
import math

def is_valid(num):
    return num.isdigit() and 1 <= int(num) <= 100

random.seed(17)

#n = int(input())
#r = random.randint(1, n)
#print(math.ceil(math.log2(n))) 

r = random.randint(1, 100)
print('Welcome')

while True:
    print('guess a number 1-100')
    n = input()
    if not is_valid(n):
        print('Input correct data')
        continue
    else:
        n = int(n)
        if n > r:
            print('Too many, try again')
            continue
        elif n < r:
            print('Too few, try again')
            continue
        else:
            print('Congtatulations')
            break
print('Thanks for participating')
        


