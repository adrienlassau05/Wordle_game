import random as random

with open('wordle-answers-alphabetical.txt', 'r') as answer_file:
    possible_answer = answer_file.read().splitlines()
with open('wordle-allowed-guesses.txt', 'r') as guess_file:
    possible_guess = guess_file.read().splitlines()

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", 
            "j","k", "l", "m", "n", "o", "p", "q", "r", 
            "s", "t","u", "v", "w", "x", "y", "z"]

def main():
    introduction()
    answer = choose_answer()
    guess = ""
    guess_number = 0
    guess_list = []
    progress_list = []
    while True:
        guess = player_guess()
        alphabet_left(guess, answer)
        guess_list.append(guess)
        green_index, green_character, yellow_index, yellow_character = check_guess(answer, guess)
        yellow_index = check_yellow(yellow_index, yellow_character, guess, answer, green_character)
        progress_list.append(progress(green_index, yellow_index))
        total_progress(progress_list, guess_list)
        guess_number += 1
        if guess == answer:
            print("That was the correct word!")
            print(f"It took you {guess_number} tries to get it!")
            break
    
        elif not game_loss(guess_number):
            print(f"I am sorry, that was it. The word was {answer}")
            break

def choose_answer():
    choice = random.randint(0, len(possible_answer) - 1)
    return possible_answer[choice]

def player_guess():
    guess = input("What is your guess? ").strip().lower()
    while True:
        if guess == "/alphabet":
            for i, ch in enumerate(alphabet):
                print(f"{alphabet[i]}, ", end="")
                if ((i+1) % 9) == 0:
                    print("")
            print("")
            guess = input("What is your guess? ").strip().lower()
        elif guess.isalpha() and len(guess) == 5:
            if allowed_guess(guess) == True:
                break
            elif allowed_guess(guess) == False:
                print("This is not a in the word list, please try again.")
                guess = input("What is your guess: ").strip().lower()
        else:
            print("This is not a valid word, please try again.")
            guess = input("What is your guess: ").strip().lower()
    return guess

def check_guess(answer, guess):
    green_index, green_character = [], []
    yellow_index, yellow_character = [], []
    for i, ch in enumerate(guess):
        if ch == answer[i]:
            green_index.append(i)
            green_character.append(i)
        elif ch in answer:
            yellow_index.append(i)
            yellow_character.append(ch)
        else:
            continue
    return(green_index, green_character, yellow_index, yellow_character)

def progress(green, yellow):
    progress_bar = "⬛⬛⬛⬛⬛"
    for i in green:
        progress_bar = progress_bar[:i] + "🟩" + progress_bar[i+1:]
    for i in yellow:
        progress_bar = progress_bar[:i] + "🟨" + progress_bar[i+1:]
    return progress_bar

def game_loss(number):
    if number >= 6:
        return False
    else:
        return True
    
def allowed_guess(guess):
    while True:
        if guess in possible_guess:
            return True
        elif guess in possible_answer:
            return True
        else:
            return False
        
def check_yellow(yellow_index, yellow_character, guess, answer, green_character):
    #go throught all characters in guess
    for i in green_character:
        if i in yellow_character:
            ind = yellow_character.index(i)
            yellow_character.pop(ind)
            yellow_index.pop(ind)
    
    for i, ch in enumerate(yellow_character):
        if guess.count(ch) > answer.count(ch):
            yellow_character.pop(i)
            yellow_index.pop(i)
    return(yellow_index)

def total_progress(progress_list, guess_list):
    for i, ch in enumerate(progress_list):
        print(ch, " ", end="")
        print(guess_list[i])
        
def alphabet_left(guess, answer):
    for i in guess:
        if i in answer:
            continue
        elif i in alphabet:
            alphabet.pop(alphabet.index(i))
    return alphabet

def introduction():
    print("Welcome to Wordle, the word guessing game we all love.", end = "")
    print("You have 6 guesses to find the word. After each guess, a colored feedback ", end = "")
    print("will show up. Green means correct letter correct placement, while yellow ", end = "") 
    print("means the letter is in the word but not in that position.")
    print('You can type in "/alphabet" at any time to see what letters are still possible.')
main()   