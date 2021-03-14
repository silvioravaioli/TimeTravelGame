####################################################
label start_chapter2:
    # play music "funiculifunicula.mp3" fadeout 1       # ADD MUSIC
    scene bg restaurant room
    show eileen vhappy
    n "START CHAPTER 2."

    n "New part of the story"

    hide eileen
    scene black

    # ending
    #return



####################################################
label chapter1_block2:

    scene bg cafeteria

    show pastprotagonist
    pp "Uh... guess I’ll just put this here on the table..."
    pp "Might as well get some lunch while I’m at it."
    pp "Can I get an egg salad sandwich with extra onions, extra pickles, extra garlic?"
    hide pastprotagonist

    show barista
    b  "Sure! Would you like to add a cup of coffee to that order? Promotion week, only 25 cents extra"
    hide barista

    show pastprotagonist
    pp " Past self: “I’m not actually a coffee person. But hey, sure, why not?"
    hide pastprotagonist

    show barista
    b  "Ok, egg salad sandwich with extra onions, extra pickles, extra garlic, and a cup of coffee coming right up!"
    n  "The barista is now standing in front of coffee machine"
    hide barista

    show pastprotagonist
    pp "So... that’s how you make coffee"
    hide pastprotagonist

    #### MENU
    menu:
        n "What do you want to do now?"
        "Explore the coffee shop":
            n "You explore the coffee shop"
        "Leave":
            n "Leave"
        "--other--":
            n "--other--"

    scene black

    # ending
    #return




####################################################
label chapter1_block3:

    scene bg home

    show timegod
    g "So... how do you think it went?"
    hide timegod

    #### MENU
    menu:
        g "So... how do you think it went?"
        "Not great":
            show timegod
            g "Hm. You’ll get better next time."
        "Went OK":
            show timegod
            g "Good. Now you know what to expect next time."
    hide timegod


    show protagonist
    p "So... What happened when I was gone?"
    hide protagonist

    show timegod
    g "Interesting question. Guess you’ll have to find out."
    hide timegod

    n "--- TO BE ADDED: Ways to find out about the impact ----"
    n "--- TO BE ADDED: How does the protagonist realize that the bean water disaster was averted? ----"


    scene black

    # ending
    return


