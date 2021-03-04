print("welcome our first github project")
name=input("what is your name?")

import random
import os




def cls(): return os.system('cls')

cls()
print(f"welcom to you {name}")
print(f"{name.title()} has  {len(name)} letters" )

for index,letter in enumerate(name):
    print(f"{index+1} {letter}")
    if letter=="b":
        print("❤❤❤❤❤❤❤❤❤❤❤❤")
    else:
        print("😂❤")    