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

    def enter_action():
        """ What should happen when the RETURN or ENTER key is pressed. """
        gw.show_message("You need to implement this method")


    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)




# Startup boilerplate
if __name__ == "__main__":
    wordle()
