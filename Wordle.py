########################################
# Name:
# Collaborators (if any):
# Estimated time spent (hr):
# Description of any added extensions:
########################################

from WordleGraphics import WordleGWindow, N_ROWS, N_COLS
from english import ENGLISH_WORDS, is_english_word
from WordleGraphics import CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR, UNKNOWN_COLOR
import random



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
        print(gw.get_current_row())
        row = 0
        if row  != 6:
            gw.set_current_row(row)
            for col in range(5):
                x = gw.get_square_letter(row, col)
                user_word += x
            user_word = user_word.lower()
            if user_word == optimal_word:
                gw.show_message("You Win!")
                gw.set_current_row(5)
            elif user_word in ENGLISH_WORDS:
                gw.show_message("yay")
                for i in range(5):
                    if user_word[i] == optimal_word[i]:
                        gw.set_square_color(row,i, "#66BB66")
                    elif user_word[i] in optimal_word and user_word[i] != optimal_word[i]:
                        gw.set_square_color(row,i, "#CCBB66")
                    else:
                        gw.set_square_color(row,i, "#999999")
            else:
                for i in range(5):
                    gw.set_square_letter(row, i, " ")
                    gw.set_square_color(row, i, "#FFFFFF")
                    gw.show_message("Not in word list")  
            row += 1      
            
    
    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)
    
        
# Startup boilerplate
if __name__ == "__main__":

    wordle()
    