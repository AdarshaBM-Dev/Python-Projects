import random

secretnum = random.randint(0,50)
#print(secretnum)
count = 1 
while(True):
    guess = int(input("guess the number (0-50) >> "))
    if guess ==  secretnum:
        print("you guessed it right. Victory")
        break
    else:
        print("Oh no! Try Again")
        count += 1

print(f"you took {count}chances")