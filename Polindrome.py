word = "Malayalam".lower()
word_bacwords = word[::-1]
if word==word_bacwords:
    print("Its a polindrome")
else:
    print("Its not a polindrom")


#color
from colorama import Fore,Back,Style
word = input("Enter world >> ").lower()
word_bacwords = word[::-1]
if word==word_bacwords:
    print(Fore.GREEN+ "Its a polindrome"+ Fore.RESET)
else:
    print(Back.BLUE+ "Its not a polindrom"+Back.RESET)

#style
from colorama import Fore,Back,Style
word = "Malayalam".lower()
word_bacwords = word[::-1]
if word==word_bacwords:
    print(Style.BRIGHT+ "Its a polindrome"+ Style.RESET_ALL)
else:
    print(Style.DIM+ "Its not a polindrom"+ Style.RESET_ALL)