# The script of the game goes in this file.


# Use the transforms file to generate fancy transitions
call transforms

####################################################
# CHARACTERS

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define p = Character("You",color="#ffff00")     # protagonist
define pp = Character("You (from the past)",color="#888888")     # past protagonist
define coworker = Character("Coworker",color="#33cc33")        # coworker
define barista = Character("Barista",color="#ff0066")       # barista
define boss = Character("Boss",color="#ff0066")         # boss
define n = Character("",color="#d9d9d9")               # narrator

define g = Character("timegod_name" ,color="#809fff", dynamic=True)        # god
define timegod_name = "???"


## extra - in case we want to add more
define e = Character("Eileen")
define s = Character("Unclear",color="#33cc33")        # coworker
define f = Character("Friend",color="#33cc33")          # friend
define m = Character("Mother",color="#ff0066")          # mother



####################################################
# INITIALIZE MISSIONS
$ mission1personal_success = 0
$ mission1timegod_success = 0
$ mission2personal_success = 0
$ mission2timegod_success = 0
$ mission3personal_success = 0
$ mission3timegod_success = 0
$ mission4personal_success = 0
$ mission4timegod_success = 0


####################################################
# START

label start:
    $ testing_mode = False
    if not testing_mode:
        jump start_game
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
        "Testing Zone":
            jump start_testingZone
