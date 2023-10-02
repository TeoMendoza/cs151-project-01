########################################
# Name: Teo Mendoza
# Collaborators (if any): Help from professor and section leaders
# Estimated time spent (hr): 7-8 hours
# Description of any added extensions: ?
########################################

from WordleGraphics import WordleGWindow, N_ROWS, N_COLS
from english import ENGLISH_WORDS, is_english_word
from WordleGraphics import CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR, UNKNOWN_COLOR
import random

# Constants of colors for use in code
GREEN = "#66BB66"
YELLOW = "#CCBB66"
GRAY = "#999999"
WHITE = "#FFFFFF"
greens = []
yellows = []
grays = []
def get_user_word(gw: WordleGWindow, ro: int):
    # Functon that puts the typed in word in a variable called user_word and also strips of empty spaces for the case that the player types in less than 5 letters
    user_word = ""
    for col in range(5):
        x = gw.get_square_letter(ro, col)
        user_word += x
    user_word = user_word.lower()
    user_word = user_word.strip()
    return user_word

def set_green(gw: WordleGWindow, ro: int, col: int, user_word: str):
    # Function that sets a square and key color to green
    gw.set_square_color(ro,col, GREEN)
    gw.set_key_color(user_word[col], GREEN) 

def set_yellow(gw: WordleGWindow, ro: int, col: int, user_word: str):
    # Function that sets a square color to yellow
    gw.set_square_color(ro,col, YELLOW)
    

def set_gray(gw: WordleGWindow, ro: int, col: int, user_word: str):
    # Function that sets a square color to gray
    gw.set_square_color(ro,col, GRAY)
    
def set_keys(gw: WordleGWindow):
    # Function that sets key colors from least important to most important
    for i in grays:
        gw.set_key_color(i, GRAY)
    for i in yellows:
        gw.set_key_color(i, YELLOW)
    for i in greens:
        gw.set_key_color(i, GREEN)

def reset(gw:WordleGWindow, ro: int, col: int):
    # Function that resets a line; used when the word the player types in isn't 5 letters or isn't a real word
    gw.set_current_row(ro)
    gw.set_square_letter(ro, col, "")
    gw.set_square_color(ro, col, "#FFFFFF")



def wordle():
    # The main function to play the Wordle game
   
    def guess_word():
        # Function that gets a random word from a list of valid 5 letter english words, stores it in optimal_word which becomes the word players try to guess
        five = []
        for i in ENGLISH_WORDS:
            if len(i) == 5:
                five.append(i)
        optimal_word = random.choice(five)
        return optimal_word

    optimal_word = guess_word()
    print(optimal_word)
            
    def enter_action():
        # What should happen when the RETURN or ENTER key is pressed

        # Empty user_word string
        user_word = ""
        # Variable to keep track of current row
        ro = gw.get_current_row()
        # Duplicate of the word the player is trying to guess used for special wordle cases; one example being GLASS and SASSY
        word_check = optimal_word
        
        # Code that runs within the Wordle Board Bounds, Runs everytime Enter/Return is pressed
        if ro < 6:
            user_word = get_user_word(gw, ro)
            
            # User doesn't type in a word that is 5 letters Case
            if len(user_word) < 5:
                gw.show_message("Please type in a five letter word")
                for col in range(5):
                    reset(gw, ro, col)

            # Win Case    
            elif user_word == optimal_word:
                gw.show_message("You Win!")
                for col in range(5):
                    set_green(gw, ro, col, user_word)
                gw.set_current_row(N_ROWS)
                
            # Valid word but not a win Case
            elif user_word in ENGLISH_WORDS and ro != 5:
                gw.show_message("Valid Word")
                for col in range(5):
                    if user_word[col] == word_check[col]:
                        set_green(gw, ro, col, user_word)
                        greens.append(user_word[col])
                        word_check = word_check.replace(user_word[col], "*", 1)

                for col in range(5):
                    if user_word[col] in word_check and user_word[col] != word_check[col] and gw.get_square_color(ro,col) not in [GREEN]:
                        set_yellow(gw, ro, col, user_word)
                        yellows.append(user_word[col])
                        word_check = word_check.replace(user_word[col], "*", 1)

                    elif user_word[col] not in word_check and gw.get_square_color(ro,col) not in [YELLOW, GREEN]:
                        set_gray(gw, ro, col, user_word)
                        grays.append(user_word[col])
                gw.set_current_row(ro+1)
                set_keys(gw)
            # Valid word but user has run out of guesses and loses Case
            elif user_word in ENGLISH_WORDS and ro == 5 and user_word != optimal_word:
                for col in range(5):
                    if user_word[col] == word_check[col]:
                        set_green(gw,ro,col,user_word)
                        greens.append(user_word[col])
                        word_check = word_check.replace(user_word[col], "*", 1)
                        gw.set_current_row(ro+1)

                for col in range(5):
                    if user_word[col] in word_check and user_word[col] != word_check[col] and gw.get_square_color(ro,col) not in [GREEN]:
                        set_yellow(gw, ro, col, user_word)
                        yellows.append(user_word[col])
                        word_check = word_check.replace(user_word[col], "*", 1)
                        gw.set_current_row(ro+1)

                    elif user_word[col] not in word_check and gw.get_square_color(ro,col) not in [YELLOW, GREEN]:
                        set_gray(gw, ro, col, user_word)
                        grays.append(user_word[col])
                gw.show_message("You Lose :(, The Mystery Word was " + optimal_word)
                gw.set_current_row(N_ROWS)
                set_keys(gw)
            # User types in a non english word Case
            else:
                gw.show_message("Please type in a valid word")
                for col in range(5):
                    reset(gw, ro, col)
                    
    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)
    
# Startup boilerplate
if __name__ == "__main__":
    wordle()