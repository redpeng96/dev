from random import *

words = ["apple", "banana", "orange", "grape", "watermelon", "cherry", "melon", "mango", "tomato", "strawberry", "blueberry"]
word = choice(words)

print("Answer: " + word)

letters = ""

while True:
    succeed = True
    for w in word:
        if w in letters:
            print(w, end=" ")
        else:
            print("_", end=" ")
            succeed = False

    if succeed:
        print("\nCongratulations!!!")
        break
    print("\n")
    
    letter = input("Input a letter: ")
    if letter not in letters:
        letters += letter
    else:
        print("\nInput Again!!!")
        continue

    if letter in word:
        print("\nCorrect!!!")
    else:
        print("\nWrong!!!")



