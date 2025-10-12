import time
import os
import random

numbers = []
guess = []

for _ in range(5):
    numbers.append(random.randint(1,9))
print(numbers)

time.sleep(5)  
os.system('cls')

# while numbers != guess:
#     for i in range