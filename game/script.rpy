# The script of the game goes in this file.


####################################################
# CHARACTERS

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define p = Character("Protagonist",color="#ffff00")     # protagonist
define g = Character("Time God",color="#809fff")        # god
define f = Character("Friend",color="#33cc33")          # friend
define m = Character("Mother",color="#ff0066")          # mother
define n = Character("",color="#d9d9d9")               # narrator


####################################################
# START

label start:

    menu:
        n "Do you need the RenPy short tutorial?"
        "Yes - show the tutorial":
            jump start_tutorial
        "No - skip to the game":
            jump start_game

####################################################
# START GAME

label start_game:

    menu:
        n "Which chapter of the game you want to jump to?"
        "Chapter 1":
            jump start_chapter1
        "Chapter 2":
            jump start_chapter2
        "Testing Zone":
            jump start_testingZone
