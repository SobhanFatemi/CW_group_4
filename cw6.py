import random

randomk = random.randint(1000, 10000)
guess = ""


while guess != randomk:
    counter = 0
    guess = (input("guess your number:"))
    randomk = str(randomk)
    print(randomk)

    for i in range (len(guess)):
        if guess[i] == randomk[i]:
            counter += 1

    print(f"currect number digit: {counter}")
    print(f"wrong number digit: {4-counter}")

print(f"congraution {guess} is currect")
   





