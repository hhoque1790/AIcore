import random
word_list=["apple","banana","cherry","orange","cucumber"]
print(word_list)


class Hangman:
    def __init__(self,word_list):
        self.word=random.choice(word_list)
        print(self.word)
        self.word_guessed=["_"]*len(self.word)
        print(self.word_guessed)
        self.num_letters=len(self.word)
        self.num_lives=5
        # self.word_list
        self.list_of_guesses=[]
    
    def check_guess(self, guess):
        guess=guess.lower()
        if guess in self.word:
            print("Good guess! {} is in the word.".format(guess))
            indx=""
            for count, i in enumerate(self.word):
                if i==guess:
                    indx=count
                    self.word_guessed[count]=i
                    self.num_letters-=1
            print(indx)
            print(self.num_letters)
            print(self.word_guessed)
        else:
            self.num_lives-=1
            print("Sorry, {} is not in the word. Try again.".format(guess))
            print("You have {} lives left.".format(self.num_lives))

    def ask_for_input(self):
        while True:
            guess=input("Please guess a letter: ")
            if len(guess)!=1 or type(guess)!=str:
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)

game1=Hangman(word_list)
game1.ask_for_input()