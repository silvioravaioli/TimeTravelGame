####################################################
label start_chapter2:
    scene bg office
    show protagonist neutral at t11
    p "Ok it’s almost 5. I’m heading out."
    n "{i}You walk past and see a poster on the wall{\i}"
    p "Hmm… I wonder what that is?"
    n "{i}Poster says “STAR WARS DAY{\i}"
    show protagonist excited at t11
    p "Oh YES! OH YES OH YES! Next Monday is STAR WARS DAY! I am going to absolutely SMOKE the competition."
    show protagonist anxious at t11
    p "What should I be? Princess Leia? Stormtrooper? I do a mean Darth Vader impression too. Wookie? Hmm…."
    scene black with Dissolve(2.0)
    jump chapter2_office_StarWarsDay1


####################################################
label chapter2_office_StarWarsDay1:
    scene bg office
    n "{i}One week later...{\i}"
    show boss neutral at t33
    boss "What the HELL are you wearing?"
    show protagonist wookie at t31
    p "I’m a Wookie! Star Wars day? Said so on the poster on the wall?"
    show boss angry at t33
    boss "That’s NEXT Monday! Not TODAY! Today’s our investor meeting! You’re presenting and you show up dressed as Bigfoot?"
    show protagonist anxious at t31
    p "Oh..."
    scene black with Dissolve(2.0)

    n "TODO - image of poster and scene with people in suits, protagonist and boss reactions"
    # [Image of Wookie P with a chart he’s presenting. We see the backs of a bunch of people wearing suits in the foreground.
    # B is standing off to the side, facepalming. P is visibly freaking out]
    jump chapter2_home_meetTimeGod


####################################################
label chapter2_home_meetTimeGod:
    scene bg home
    show timegod neutral at t11
    g "Whoa you really messed that up. I see you’ve had a bad day...again."
    g "I have a proposition for you."
    g "Would you like a do over...a chance to undo your mistakes?"
    menu:
        "You again!":
            g "Interesting statement."
        "What do you want me to do this time?":
            g "Interesting question."
        "Huh? I thought you were a dream?":
            g "Interesting question."

    g "I’m going to need you to pick something up for me."
    g "While you’re at it, feel free to destroy this abomination of a Bigfoot costume."
    menu:
        "So what do you need me to get?":
            g "Interesting question."
        "Are we in the past now? How did you do that?":
            g "Interesting question."
        "Shouldn’t you wait until I agree before sending me back in time?":
            g "Interesting question."
