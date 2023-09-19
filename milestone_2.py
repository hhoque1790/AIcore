import random
word_list=["apple","banana","cherry","orange","cucumber"]
print(word_list)
word=random.choice(word_list)
print(word)

guess=input("Please enter a letter: ")
if len(guess)==1 and type(guess)==str:
    print("good guess")
else:
    print("Oops! That is not a valid input.")