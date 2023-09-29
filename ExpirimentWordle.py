########################################
# Name: Teo Mendoza
# Collaborators (if any): Help from professor and section leaders
# Estimated time spent (hr): 6-7 hours
# Description of any added extensions: ?
########################################

from WordleGraphics import WordleGWindow, N_ROWS, N_COLS
from english import ENGLISH_WORDS, is_english_word
from WordleGraphics import CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR, UNKNOWN_COLOR
import random


GREEN = "#66BB66"
YELLOW = "#CCBB66"
GRAY = "#999999"
WHITE = "#FFFFFF"

def get_user_word(gw: WordleGWindow, ro: int):
    user_word = ""
    for col in range(5):
        x = gw.get_square_letter(ro, col)
        user_word += x
    user_word = user_word.lower()
    user_word = user_word.strip()
    return user_word

def set_green(gw: WordleGWindow, ro: int, col: int, user_word: str):
    gw.set_square_color(ro,col, GREEN)
    gw.set_key_color(user_word[col], GREEN) 

def set_yellow(gw: WordleGWindow, ro: int, col: int, user_word: str):
    gw.set_square_color(ro,col, YELLOW)
    gw.set_key_color(user_word[col], YELLOW)

def set_gray(gw: WordleGWindow, ro: int, col: int, user_word: str):
    gw.set_square_color(ro,col, GRAY)
    gw.set_key_color(user_word[col], GRAY)

def reset(gw:WordleGWindow, ro: int, col: int):
    gw.set_current_row(ro)
    gw.set_square_letter(ro, col, "")
    gw.set_square_color(ro, col, "#FFFFFF")



def wordle():
    
    """ The main function to play the Wordle game. """
   
    def guess_word():
    #changes optmal word every time it hits a new row, but i want to keep optimal word the same, also fix the row stuff
        five = []

        for i in ENGLISH_WORDS:
            if len(i) == 5:
                five.append(i)
        optimal_word = random.choice(five)
        return optimal_word
    optimal_word = guess_word()
    print(optimal_word)
            
    def enter_action():
        """ What should happen when the RETURN or ENTER key is pressed. """
        user_word = ""
        print(optimal_word)
        ro = gw.get_current_row()
        word_check = optimal_word
        
        if ro < 6:
            user_word = get_user_word(gw, ro)
            
            if len(user_word) < 5:
                gw.show_message("Please type in a five letter word")
                for col in range(5):
                    reset(gw, ro, col)
                

            elif user_word == optimal_word:
                gw.show_message("You Win!")
                for col in range(5):
                    set_green(gw, ro, col, user_word)
                gw.set_current_row(N_ROWS)

            elif user_word in ENGLISH_WORDS and ro != 5:
                gw.show_message("Valid Word")
                for col in range(5):
                    if user_word[col] == word_check[col]:
                        set_green(gw, ro, col, user_word)
                        word_check = word_check.replace(user_word[col], "*", 1)

                for col in range(5):
                    if user_word[col] in word_check and user_word[col] != word_check[col] and gw.get_square_color(ro,col) not in [GREEN]:
                        set_yellow(gw, ro, col, user_word)
                        word_check = word_check.replace(user_word[col], "*", 1)
                    elif user_word[col] not in word_check and gw.get_square_color(ro,col) not in [YELLOW, GREEN]:
                        set_gray(gw, ro, col, user_word)
                gw.set_current_row(ro+1)

            elif user_word in ENGLISH_WORDS and ro == 5 and user_word != optimal_word:
                for col in range(5):
                    if user_word[col] == word_check[col]:
                        set_green(gw,ro,col,user_word)
                        word_check = word_check.replace(user_word[col], "*", 1)
                        gw.set_current_row(ro+1)

                for col in range(5):
                    if user_word[col] in word_check and user_word[col] != word_check[col] and gw.get_square_color(ro,col) not in [GREEN]:
                        set_yellow(gw, ro, col, user_word)
                        word_check = word_check.replace(user_word[col], "*", 1)
                        gw.set_current_row(ro+1)

                    elif user_word[col] not in word_check and gw.get_square_color(ro,col) not in [YELLOW, GREEN]:
                        set_gray(gw, ro, col, user_word)
                gw.show_message("You Lose :(, The Mystery Word was " + optimal_word)
                gw.set_current_row(N_ROWS)

            else:
                gw.show_message("Please type in a valid word")
                for col in range(5):
                    reset(gw, ro, col)
                    
                   
            
        
        
                
    gw = WordleGWindow()
    
    gw.add_enter_listener(enter_action)
    


    
# Startup boilerplate
if __name__ == "__main__":

    wordle()
    