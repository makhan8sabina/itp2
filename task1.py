import random

number=random.randint(1,100)
g=0
a=0
c=0

print('1 - EASY (8 attempts)')
print('2 - MEDIUM (6 attempts)')
print('3 - HARD (4 attempts)')
l=int(input("Enter a number: "))

if l == 1:
    c=8
elif l == 2:
    c=6
elif l == 3:
    c=4

while g != number:
    g = int(input("Enter your guess: "))
    a += 1
    if g > number:
        print("Too high! Try again.")
    elif g<number:
        print("Too low! Try again.")
    else:
        print("Correct! You guessed it in {a} attempts.")


    if a == c:
        print("GAME OVEEEER")
        break