# The script of the game goes in this file.


####################################################
# CHARACTERS

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define p = Character("Protagonist",color="#ffff00")     # protagonist
define g = Character("Time God",color="#809fff")        # god
define f = Character("Friend",color="#33cc33")          # friend
define m = Character("Mother",color="#ff0066")          # mother
define n = Character(" ",color="#d9d9d9")               # narrator


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
# START TUTORIAL

label start_tutorial:

    # scene = background image
    scene bg restaurant room
    n "The command scene displays a background"

    # show = character appears (one character can have several “moods” = sprites)
    # multiple characters can appear on the same page (we just need to place them right/left)
    show eileen happy
    n "The command show displays an image, usually a character"

    show eileen happy at right
    n "You can define where on the screen you want the character to appear"

    show eileen happy at right
    n "You can move the character on the screen"

transform move_slide:
    xalign 1.0 yalign 0.0
    linear 3.0 xalign 0.0
    pause 1.0
    repeat
 

    show lucy happy at right
    n "You can show multiple characters at once"

    # hide = remove the character
    hide lucy
    n "The command hide removes one image"

    jump start












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


####################################################
label start_chapter1:
    # play music "funiculifunicula.mp3" fadeout 1       # ADD MUSIC
    scene bg restaurant room
    show eileen vhappy
    n "START CHAPTER 1."

    n "This part is currently empty"

    hide eileen
    hide bg

    jump start


####################################################
label start_chapter2:
    # play music "funiculifunicula.mp3" fadeout 1       # ADD MUSIC
    scene bg restaurant room
    show eileen vhappy
    n "START CHAPTER 2."

    n "This part is currently empty"

    hide eileen
    hide bg

    # ending
    return

####################################################
label start_testingZone:
    # play music "funiculifunicula.mp3" fadeout 1       # ADD MUSIC
    scene bg restaurant room
    show eileen vhappy
    n "START TESTING ZONE."

    n "This part is currently empty"

    hide eileen
    hide bg

    jump start




