# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")


# The game starts here.

label start:

    e "Example of how to use navigation maps."

label imagemap_displayables:

    e "Imagemaps use two or more images to show buttons and bars. Let me start by showing you an example of an imagemap in action."

    window hide None

    $ workingFlag = 1;
    if workingFlag>0:

        screen imagemap_example():
            imagemap:
                idle "imagemap ground"
                hover "imagemap hover"

                hotspot (44, 238, 93, 93) action Jump("swimming") alt "Swimming"
                hotspot (360, 62, 93, 93) action Jump("science") alt "Science"
                hotspot (726, 106, 93, 93) action Jump("art") alt "Art"
                hotspot (934, 461, 93, 93) action Jump("home") alt "Home"

        label imagemap_example:

            # Call the imagemap_example screen.
            call screen imagemap_example

        label swimming:

            e "You chose swimming."

            e "Swimming seems like a lot of fun, but I didn't bring my bathing suit with me."

            jump imagemap_done

        label science:

            e "You chose science."

            e "I've heard that some schools have a competitive science team, but to me research is something that can't be rushed."

            jump imagemap_done

        label art:
            e "You chose art."

            e "Really good background art is hard to make, which is why so many games use filtered photographs. Maybe you can change that."

            jump imagemap_done

        label home:

            e "You chose to go home."

            jump imagemap_done

        label imagemap_done:

            e "Anyway..."


    # This ends the game.

    return
