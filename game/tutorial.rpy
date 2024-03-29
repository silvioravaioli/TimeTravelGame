####################################################
# START TUTORIAL

label start_tutorial:

    ##### DIALOGUES AND ANIMATIONS

    # scene = background image
    scene bg restaurant room
    n "The command scene displays a background"

    # show = character appears (one character can have several “moods” = sprites)
    # multiple characters can appear on the same page (we just need to place them right/left)
    show eileen happy
    n "The command show displays an image, usually a character"

    show eileen happy at right
    n "You can define where on the screen you want the character to appear (on the right?)"

    show eileen happy:
        xalign 1.0 yalign 0.0
        linear 3.0 xalign 0.0 # 3 seconds
    n "You can move the character on the screen (to the left?)"

    show eileen happy:
        xalign 1.0 yalign 0.0
        linear 1.0 xalign 0.0 # 1 seconds
    n "Or you can move it quickly (to the left again?)"

    show lucy happy at right
    n "You can show multiple characters at once"

    # hide = remove the character
    hide lucy
    n "The command hide removes one image"



    ##### CHOICES AND MENUS

    # input text (any)
    "What is your name?"
    $ input_text = renpy.input("What is your name?", "")

    # input number
    "What is your favorite number?"
    $ input_number = renpy.input("What is your favorite number?", "123", allow="0123456789")

    # menu
    n "You can collect choices using menus."
    menu:
        n "Which of these sentences is correct?"
        "the other sentence is correct":
            #jump aaa1
            n "are you sure?"
        "this sentence is not correct":
            #jump aaa2
            n "interesting choice"

    # map
    if 1>0: # just a placeholder condition
        screen imagemap_example():
            imagemap:
                idle "imagemap ground"
                hover "imagemap hover"

                hotspot (44, 238, 93, 93) action Jump("swimming") alt "Swimming"
                hotspot (360, 62, 93, 93) action Jump("science") alt "Science"
                hotspot (726, 106, 93, 93) action Jump("art") alt "Art"
                hotspot (934, 461, 93, 93) action Jump("home") alt "Home"

        n "You can also create maps to macke choices."

        label imagemap_example:
            # Call the imagemap_example screen.
            call screen imagemap_example

        label swimming:
            n "You chose swimming."
            jump imagemap_done

        label science:
            n "You chose science."
            jump imagemap_done

        label art:
            n "You chose art."
            jump imagemap_done

        label home:
            n "You chose to go home."
            jump imagemap_done



label imagemap_done:

    n "END OF THE TUTORIAL"
    hide eileen
    scene black
    jump start
