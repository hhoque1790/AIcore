import random 

class Hangman:
    def __init__(self,word_list,num_lives):
        self.word=random.choice(word_list)
        # print(self.word)
        self.word_guessed=["_"]*len(self.word)
        print(self.word_guessed)
        self.num_letters=len(self.word)
        self.num_lives=num_lives
        # self.word_list
        self.list_of_guesses=[]
    
    def check_guess(self, guess):
        guess=guess.lower()
        if guess in self.word:
            print("Good guess! {} is in the word.".format(guess))
            for count, i in enumerate(self.word):
                if i==guess:
                    self.word_guessed[count]=i
                    self.num_letters-=1
            # print(self.num_letters)
            print(self.word_guessed)
            if self.num_letters==0:
                print('Congratulations. You won the game!')
                exit()
        else:
            self.num_lives-=1
            if self.num_lives==0:
                    print("You lost")
                    exit()  
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

def play_game(word_list):
    num_lives =5
    game=Hangman(word_list,num_lives)
    game.ask_for_input()

play_game(["apple","banana","cherry","orange","cucumber"])


