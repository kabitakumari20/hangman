import string
from words import choose_word
from image import IMAGES
def is_word_guessed(secret_word,letters_guessed):

    if secret_word ==get_guessed_word(secret_word, letters_guessed):
        return True
    return False

def get_guessed_word(secret_word,letters_guessed):
    index=0
    guessed_word=""
    while index<len(secret_word):
        if secret_word[index] in letters_guessed:
            guessed_word+=secret_word[index]
        else:
            guessed_word+="_"
        index+=1
    return guessed_word
def ifValid(user_input):
    if len(user_input) != 1:
        return False
    if not user_input.isalpha():
        return False
    return True 
def get_hint(secret_word, letters_guessed):

    import random
    letters_not_guessed = []

    index = 0
    while (index < len(secret_word)):
        letter = secret_word[index]
        if letter not in letters_guessed:
            if letter not in letters_not_guessed:
                letters_not_guessed.append(letter)
        index=index+1
    return random.choice(letters_not_guessed) 


def get_available_letters(letters_guessed):
    import string
    letters_left=string.ascii_lowercase
    i=0
    alphabet=""
    while i<len(letters_left):
        if letters_left[i]!=letters_guessed:
            alphabet=alphabet+letters_left[i]
        i+=1
    return alphabet

def Hangman(secret_word):
    print ("********WELCOME TO THE GAME HANGMAN!**********")
    print ("I am thinking of a word that is " + str(len(secret_word))+"length")
    print ("")
    user_difficulty_choice = input("choose the difficulty which level you want to play\na\nb\nc\nlevel_choice:---")
    
    if user_difficulty_choice=="a":
        total_lives = remaining_lives = 8
        images_selection_list_indices = [0, 1, 2, 3, 4, 5, 6, 7]
    elif user_difficulty_choice == "b":
        total_lives = remaining_lives = 6
        images_selection_list_indices = [0, 2, 3, 5, 6, 7]
    elif user_difficulty_choice == "c": 
        total_lives = remaining_lives = 4
        images_selection_list_indices = [1, 3, 5, 7]
    else:
        print ("no other level!!!!!")

    letters_guessed = [] 

    remaining_lives=total_lives
    print(secret_word)
    i=0
    while remaining_lives>0:
        available_letters=get_available_letters(letters_guessed)
        print("Available letters: "+ available_letters)
        guess = input("Please guess a letter: ")
        if guess == "hint":
            letter = get_hint(secret_word, letters_guessed)

        else:
            letter = guess.lower()
            if not ifValid(letter):
                continue

        if letter in secret_word:
            letters_guessed.append(letter) 
        letter=guess.lower()
        if letter in secret_word:
            print ("Good guess: "+" "+str(get_guessed_word(secret_word, letters_guessed)))
            print ("")
            if is_word_guessed(secret_word, letters_guessed) == True:
                print ("*********Congratulations, you won!*********")
                print ("")
                break
        else:
            print ("Oops! which letter you guess not in my word: "+" "+str(get_guessed_word(secret_word, letters_guessed)))
            remaining_lives=remaining_lives-1
            print("You have "+str(remaining_lives)+" more chance to get letter")
            if remaining_lives>=1:
                print(IMAGES[images_selection_list_indices[total_lives-remaining_lives]])
            if remaining_lives==0:
                break
            i=i+1
            print(remaining_lives)
            print(" ")
    else:
        print("Sorry you have lost your chance"+" "+ "Your secret word was"+" "+secret_word)  
secret_word=choose_word()
Hangman(secret_word)