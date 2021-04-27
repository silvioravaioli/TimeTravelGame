# The script of the game goes in this file.


# Use the transforms file to generate fancy transitions
call transforms

####################################################
# CHARACTERS

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define n        = Character("",color="#d9d9d9")                                 # narrator

define p        = Character("protagonist_name",color="#ffff00", dynamic=True)   # protagonist
define protagonist_name = "You"

define pp       = Character("You (from the past)",color="#888888")              # past protagonist

define barista  = Character("Barista",color="#ff0066")                          # barista
define boss     = Character("Boss",color="#ff0066")                             # boss

define coworker  = Character("Coworker",color="#33cc33")                        # coworker
define coworker2 = Character("Coworker 2",color="#33cc33")                      # coworker 2

define g        = Character("timegod_name" ,color="#809fff", dynamic=True)      # time god
define timegod_name = "???"



####################################################
# START

label start:

    # INITIALIZE MISSIONS
    $ mission1personal_success = 0
    $ mission1timegod_success = 0
    $ mission2personal_success = 0
    $ mission2timegod_success = 0
    $ mission3personal_success = 0
    $ mission3timegod_success = 0
    $ mission4personal_success = 0
    $ mission4timegod_success = 0

    $ testing_mode = True

    if testing_mode:
        jump start_game

    if not testing_mode:
        jump start_chapter1

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
        "Chapter 3":
            jump start_chapter3
        "Chapter 4":
            jump start_chapter4
        "Chapter 5":
            jump start_chapter5
