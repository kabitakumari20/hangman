import random
from image import IMAGES
def hangman():
    list_of_word=["kabita","hangman","india","computer","microsoft"]
    words=random.choice(list_of_word)
    print(len(words))
    turns=8
    gusemade=" "
    while turns>0:
        main_word=" "
        missed=0
        for letter in words:
            if letter in gusemade:
                print(letter)
            else:
                print("-")
                missed+=1
        if missed==0:
            print("you won")
            print("congralation your gas is right",words)
            break
            print("gess is right ")
        guess=input("enter the singale latter=")
        gusemade+=guess
        i=0
        if guess not in words:
            turns-=1
            l=len(IMAGES)
            print("your gas is wrong")
            while i<=(l-turns-2):
                print(IMAGES[i])
                i=i+1
            print("you have",turns,"guess")
            
name=input("enter the name=")
print("welcome",name)
print("--------------")
print("try to gass les than 8 times")
hangman()            
                
            