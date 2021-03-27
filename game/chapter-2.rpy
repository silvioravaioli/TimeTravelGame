####################################################
label start_chapter2:

    scene bg restaurant room

    show eileen vhappy
    n "START CHAPTER 2."
    n "New part of the story"
    hide eileen

    scene black

    # ending
    # return



####################################################
label chapter1_block2:

    scene bg cafeteria

    show pastprotagonist
    pp "Uh... guess I’ll just put this here on the table..."
    pp "Might as well get some lunch while I’m at it."
    pp "Can I get an egg salad sandwich with extra onions, extra pickles, extra garlic?"
    hide pastprotagonist

    show barista
    bar  "Sure! Would you like to add a cup of coffee to that order? Promotion week, only 25 cents extra"
    hide barista

    show pastprotagonist
    pp " Past self: “I’m not actually a coffee person. But hey, sure, why not?"
    hide pastprotagonist

    show barista
    bar  "Ok, egg salad sandwich with extra onions, extra pickles, extra garlic, and a cup of coffee coming right up!"
    n  "The barista is now standing in front of coffee machine"
    hide barista

    show pastprotagonist
    pp "So... that’s how you make coffee"
    hide pastprotagonist

    show protagonist
    pp "Oh, looks like I’m leaving. Better leave so that I don’t run into myself."
    hide protagonist

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
    # return




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

    scene black

    # ending
    # return




####################################################
label chapter1_block4success:

    n "IF MISSION SUCCESS - OFFICE, NEXT DAY"

    scene bg office

    show boss
    boss "I need you to file these documents, and sign these things for me."
    boss "Also I need those progress reports done by the end of the day."
    boss "Oh, and fix those UGLY bar charts! Who pairs neon green with hot pink?"
    hide boss

    show protagonist
    boss "Ok, anything else?"
    hide protagonist

    show boss
    boss "Oh, yeah. Make me a cup of coffee"
    hide boss

    show protagonist
    p "You want me to make you a cup of coffee?"
    hide protagonist

    show boss
    boss "Yeah, cup of coffee."
    hide boss

    show protagonist incredulous
    p "Me???"
    hide protagonist

    show boss irritated
    boss "Yes. That’s what I SAID."
    boss "And be fast, I need to run to the next meeting."
    hide boss

    show protagonist happy
    p "It worked! (whispered/italics)"
    hide protagonist

    scene black

    # ending
    # return




####################################################
label chapter1_block4failure:

    n "IF MISSION FAILED - OFFICE, NEXT DAY"

    scene bg office

    show boss
    boss "I need you to file these documents, and sign these things for me."
    boss "Also I need those progress reports done by the end of the day."
    boss "Oh, and fix those UGLY bar charts! Who pairs neon green with hot pink?"
    hide boss

    show protagonist
    boss "Ok, anything else?"
    hide protagonist

    show boss
    boss "Oh, yeah. Make me a cup of coffee"
    hide boss

    show protagonist
    p "You want me to make you a cup of coffee?"
    hide protagonist

    show boss
    boss "OF COURSE NOT!"
    show boss pointingAtCoffeeStation
    boss "Actually after yesterday, you are banned from making coffee."
    hide boss

    show protagonist incredulous
    p "Me???"
    hide protagonist

    scene bg coffeeMachineBanned
    n "pan to coffee machine, there’s a huge printout sign with the protagonist’s face on it and a huge prohibited sign over it"

    show boss irritated
    boss "Bean water. My god..."
    hide boss

    scene black

    # ending
    # return
