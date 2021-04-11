####################################################
label start_chapter2:

    ### INITIALIZE MISSIONS
    $ mission2personal_success = 0
    $ mission2timegod_success  = 0

    scene bg office

    show protagonist neutral at t11
    p "Ok it’s almost 5pm. I’m heading out."
    n "{i}You walk past and see a poster on the wall{\i}"
    show protagonist hmm at t11
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
    show timegod laugh at t11
    g "I have a proposition for you."
    show timegod creepy at t11
    g "Would you like a do over...a chance to undo your mistakes?"
    hide timegod

    menu:
        g "Would you like a do over...a chance to undo your mistakes?"
        "You again!":
            show timegod neutral at t11
            g "Interesting statement."
        "What do you want me to do this time?":
            show timegod neutral at t11
            g "Interesting question."
        "Huh? I thought you were a dream?":
            show timegod neutral at t11
            g "Interesting thought."

    g "I’m going to need you to pick something up for me."
    show timegod laugh at t11
    g "While you’re at it, feel free to destroy this abomination of a Bigfoot costume."
    show timegod neutral at t11
    g "Are you ready to go?"
    hide timegod

    menu:
        g "Are you ready to go?"
        "So what do you need me to get?":
            show timegod neutral at t11
            g "Interesting question."
        "Are we in the past now? How did you do that?":
            show timegod neutral at t11
            g "Interesting question."
        "Shouldn’t you wait until I agree before sending me back in time?":
            show timegod neutral at t11
            g "Interesting question."

    show timegod neutral at t11
    g "Your boss has a particularly nice fountainhead pen which I have admired for quite a while."
    g "During work hours, he always maintained at most a 4 foot distance from this favorite object of his."
    show timegod angry at t11
    g "Regrettably, this past Sunday he dropped this pen down the elevator shaft of your office building."
    show timegod happy at t11
    g "I wish to rescue this prize before it becomes lost forever."
    hide timegod

    menu:
        g "I wish to rescue this prize before it becomes lost forever."
        "Got it, I’ll bring it to you soon.":
            show timegod neutral at t11
            g "I was sure you would have accepted."
        "Why do you care so much about a pen?":
            show timegod neutral at t11
            g "Interesting question."

    show timegod laugh at t11
    g "I hope your journey is fruitful!"
    show timegod snap1 at t11
    g "Ready..."
    show timegod snap1 at t11
    g "Set..."
    show timegod snap1 at t11
    g "Go!"
    show timegod snap2 at t11
    g "Go!"

    scene black with Dissolve(2.0)
    n "{i}The Time God snaps his fingers and you’re transported back to last Sunday.{\i}"



####################################################
label chapter2_travelPast1:

    scene bg home

    show protagonist neutral at t11
    p "I need to obtain that pen and somehow get rid of my costume. What should I do first?"
    hide protagonist

    menu:
        p "I need to obtain that pen and somehow get rid of my costume. What should I do first?"
        "Go to the office":
            jump chapter2_travelPast_office1
        "Stay home":
            jump chapter2_travelPast_home1
        "Go to the cafe":
            jump chapter2_travelPast_cafe1



####################################################
label chapter2_travelPast_office1:

    scene bg office
    # starting the office part always completes teh main mission
    $ mission2timegod_success = 1

    show protagonist neutral at t11
    p "So I just have to go get the boss's lucky pen."
    show protagonist excited at t11
    p "EASY!"
    show protagonist at thide
    hide protagonist

    n "{i}B pops into view but not talking to P or anything. and B is holding his pen{\i}"

    show protagonist anxious at t11
    p "Oh. Shoot. He’s literally in his office holding his pen."
    p "Ahhh.. What do I do now?"
    hide protagonist

    menu:
        p "Ahhh.. What do I do now?"
        "Pull the fire alarm":
            jump chapter2_travelPast_office2fire
        "Hide somewhere until boss leaves":
            jump chapter2_travelPast_office2hide



####################################################
label chapter2_travelPast_office2fire:

    #scene bg office

    show protagonist hmm at t11
    p "Hmmm"
    p "What if I pulled the fire alarm? That should empty the building"
    show protagonist at thide
    hide protagonist

    n "{i}P sprite turns into P sprite pulling fire alarm{\i}"
    n "Alternative (if it’s easier to draw): {i}full-screen image of fire alarm on wall, with hand pulling it{\i}"
    n "You hear the sound of the fire alarm"

    show boss neutral at t11
    boss "Uhm?"
    boss "B {i}panicking, is either not holding the pen or is seen dropping it {\i}"
    boss "FIRE! FIRE! EVERYONE, GET OUTTA HERE!"
    show boss at thide
    hide boss

    show protagonist joy at t11
    p "OK, this is my chance."
    show protagonist woohoo at t11
    p "Go go go!"
    show protagonist at thide
    hide protagonist

    n "{i}P sneaks off screen in the direction of the pen{\i}"
    n "{i}P returns, triumphant, holding the pen{\i}"

    show protagonist joy at t11
    p "AH HA! I got it!"
    show protagonist neutral at t11
    p "What should I do now?"
    hide protagonist

    menu:
        p "What should I do now?"
        "Go home":
            if mission2personal_success == 0:
                jump chapter2_travelPast_home1
            else:
                jump chapter2_travelPast_home3
        "Go to the cafe":
            jump chapter2_travelPast_cafe2



####################################################
label chapter2_travelPast_office2hide:

    #scene bg home

    show protagonist hmm at t11
    p "It’s 10am right now. I could just hide until the boss leaves work."
    show protagonist at thide
    hide protagonist

    n "{i}P hides behind potted plant, recycle that image from chapter 1{\i}"
    n "{i}Office transitions from day to night{\i}"
    n "{i}P emerges{\i}"


    show protagonist joy at t11
    p "Yes! Finally, everyone left!"
    show protagonist surprised at t11
    p "Oh! My back! Crouching behind a potted plant really does things to your body."
    show protagonist talking at t11
    p "Ok, now I gotta get that pen"
    show protagonist at thide
    hide protagonist

    n "{i}P sneaks off screen in the direction of the pen{\i}"
    n "{i}P returns, triumphant, holding the pen{\i}"

    show protagonist joy at t11
    p "AH HA! I got it!"
    show protagonist hmm at t11
    p "It is completely dark outside, but maybe there is time to do something else."
    show protagonist neutral at t11
    p "What next?"
    hide protagonist

    menu:
        p "What next?"
        "Go home":
            if mission2personal_success == 0:
                jump chapter2_failedDestruction
            else:
                jump chapter2_travelPast_home3
        "Go to the cafe":
            scene bg cafeoutdoor
            n "{i}The cafe is closed.{\i}"
            n "{i}It makes sense. It is almost 11 pm...{\i}"
            jump chapter2_failedDestruction



####################################################
label chapter2_travelPast122:

    scene bg home
    # visiting home on time completes the personal mission
    $ mission2personal_success = 1

    show protagonist neutral at t11
    p "Now, I need to make sure I don’t wear that costume to work."
    show protagonist at thide
    hide protagonist

    n "P disappears from the screen, sounds of digging/shuffling around"
    n "P reappears with the costume"

    show protagonist neutral at t11
    p "Here it is. What an amazing costume..."
    show protagonist hmm at t11
    p "What should I do with this?"
    hide protagonist

    menu:
        p "What should I do with this?"
        "Burn it":
            jump chapter2_travelPast_home2_burn
        "Throw it away":
            jump chapter2_travelPast_home2_throw



####################################################
label chapter2_travelPast_home2_burn:

    scene bg home

    show protagonist surprised at t11
    p "I can’t believe I spent $300 on this"
    show protagonist anxious at t11
    p "Well… goodbye Wookie costume. You will be missed."
    show protagonist at thide
    hide protagonist

    n "Show same P with Wookie, but the costume is now on fire"

    jump chapter2_travelPast_home2_end



####################################################
label chapter2_travelPast_home2_throw:

    scene bg home

    show protagonist surprised at t11
    p "I can’t believe I spent $300 on this"
    show protagonist anxious at t11
    p "Well… goodbye Wookie costume. You will be missed."
    show protagonist at thide
    hide protagonist

    n "Show same P holding Wookie costume over trash can"

    jump chapter2_travelPast_home2_end



####################################################
label chapter2_travelPast_home2_end:
    # NOTE: NOW THIS PART BRANCHES OUT BASED ON WHETHER YOU COMPLETED ALREADY THE MAIN MISSION

    # IF MAIN MISSION COMPLETED
    if mission1timegod_success == 1:
        show protagonist talking at t11
        p "I rescued the pen, destroyed my costume."
        show protagonist anxious at t11
        p "Now I definitely won’t be showing up accidentally dressed as Wookie..."
        show protagonist hmm at t11
        p "So what now?"
        hide protagonist

        menu:
            p "So what now?"
            "Travel back to present and forget about all this":
                jump chapter2_travelPast_home3
            "Destroying the costume made me hungry. I could have lunch now":
                jump chapter2_travelPast_cafe4


    # IF MAIN MISSION NOT COMPLETED
    if mission1timegod_success == 0:
        show timegod neutral at t11
        g "I see that you have disposed of the costume."
        show timegod creepy at t11
        g "In the future, you will accomplish my instructions before fulfilling your personal agenda."
        show timegod angry at t11
        g "DO NOT ABUSE MY GENEROSITY."
        show timegod at thide
        hide timegod

        show protagonist anxious at t11
        p "Jeez, alright. I’m going already."
        show protagonist hmm at t11
        p "Where should I go now?"
        hide protagonist

        menu:
            p "Where should I go now?"
            "Go to the office":
                jump chapter2_travelPast_office1
            "Go to the cafe":
                jump chapter2_travelPast_cafe1



####################################################
label chapter2_travelPast_home3:

    scene bg home

    show protagonist neutral at t11
    p "This is done. What's next?"
    hide protagonist

    menu:
        p "This is done. What's next?"
        "Deliver the pen":
            jump chapter2_returnPen
        "Destroy the costume" (disabled=False) if mission2personal_success==0:
            jump chapter2_failedDestruction
        "Destroy the costume" (disabled=True)  if mission2personal_success==1:
            jump chapter2_failedDestruction

####################################################
label chapter2_returnPen:

    scene bg home

    show timegod snap1 at t11
    g "Thank you for bringing me this pen."
    show timegod happy at t11
    g "This was truly a beneficial exchange."
    hide timegod

    menu:
        p "Ahhh.. What do I do now?"
        "Yeah, that went well.":
            show timegod neutral at t11
            g "Interesting. I trust you will continue to have such success in the future."
        "I feel like something is wrong here.":
            show timegod neutral at t11
            g "Interesting. It seems to me you performed splendidly. I trust you will continue to have such success in the future."

    show timegod at thide
    hide timegod

    jump chapter2_end









####################################################
label chapter2_EXAMPLE:

    scene bg home

    show protagonist neutral at t11
    p "xxxx"
    p "xxxx"
    p "xxxx"
    p "xxxx"
    p "xxxx"
    p "xxxx"
