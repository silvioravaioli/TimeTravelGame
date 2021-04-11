####################################################
label start_chapter2:

    ### INITIALIZE MISSIONS
    $ mission2personal_success = 0
    $ mission2timegod_success  = 0

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
        g "Would you like a do over...a chance to undo your mistakes?"
        "You again!":
            g "Interesting statement."
        "What do you want me to do this time?":
            g "Interesting question."
        "Huh? I thought you were a dream?":
            g "Interesting question."

    g "I’m going to need you to pick something up for me."
    g "While you’re at it, feel free to destroy this abomination of a Bigfoot costume."
    g "Are you ready to go?"

    menu:
        g "Are you ready to go?"
        "So what do you need me to get?":
            g "Interesting question."
        "Are we in the past now? How did you do that?":
            g "Interesting question."
        "Shouldn’t you wait until I agree before sending me back in time?":
            g "Interesting question."


    g "Your boss has a particularly nice fountainhead pen which I have admired for quite a while."
    g "During work hours, he always maintained at most a 4 foot distance from this favorite object of his."
    g "Regrettably, this past Sunday he dropped this pen down the elevator shaft of your office building."
    g "I wish to rescue this prize before it becomes lost forever."

    menu:
        g "I wish to rescue this prize before it becomes lost forever."
        "Got it, I’ll bring it to you soon.":
            g "I was sure you would have accepted."
        "Why do you care so much about a pen?":
            g "Interesting question."


    show timegod laugh zorder 2 at t11
    g "I hope your journey is fruitful!"
    show timegod snap1 zorder 2 at t11
    g "Ready..."
    show timegod snap1 zorder 2 at t11
    g "Set..."
    show timegod snap1 zorder 2 at t11
    g "Go!"
    show timegod snap2 zorder 2 at t11
    g "Go!"

    scene black
    n "{i}The Time God snaps his fingers and you’re transported back to last Sunday.{\i}"



####################################################
label chapter2_travelPast1:

    scene bg home

    show protagonist neutral at t11
    p "I need to steal that pen and somehow get rid of my costume. What should I do first?"
    hide protagonist

    menu:
        p "I need to steal that pen and somehow get rid of my costume. What should I do first?"
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
    p "So I just have to go steal the boss's lucky pen."
    p "EASY!"

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

    show protagonist neutral at t11
    p "Hmmm"
    p "What if I pulled the fire alarm? That should empty the building"
    hide protagonist

    n "{i}P sprite turns into P sprite pulling fire alarm{\i}"
    n "Alternative (if it’s easier to draw): {i}full-screen image of fire alarm on wall, with hand pulling it{\i}"
    n "You hear the sound of the fire alarm"

    boss "Uhm?"
    boss "B {i}panicking, is either not holding the pen or is seen dropping it {\i}"
    boss "FIRE! FIRE! EVERYONE, GET OUTTA HERE!"

    p "OK, this is my chance."
    p "Go go go!"

    n "{i}P sneaks off screen in the direction of the pen{\i}"
    n "{i}P returns, triumphant, holding the pen{\i}"

    p "AH HA! I got it!"
    p "What should I do now?"

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

    show protagonist neutral at t11
    p "It’s 10am right now. I could just hide until the boss leaves work."

    n "{i}P hides behind potted plant, recycle that image from chapter 1{\i}"
    n "{i}Office transitions from day to night{\i}"
    n "{i}P emerges{\i}"



    p "Yes! Finally, everyone left!"
    #[Surprise ish? In pain?]
    p "Oh! My back! Crouching behind a potted plant really does things to your body."
    p "Ok, now I gotta get that pen"


    n "{i}P sneaks off screen in the direction of the pen{\i}"
    n "{i}P returns, triumphant, holding the pen{\i}"

    p "AH HA! I got it!"
    p "It is completely dark outside, but maybe there is time to do something else."
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

    n "P disappears from the screen, sounds of digging/shuffling around"
    n "P reappears with the costume"


    p "Here it is. What an amazing costume..."
    p "What should I do with this?"

    menu:
        p "What should I do with this?"
        "Burn it":
            jump chapter2_travelPast_home2_burn
        "Throw it away":
            jump chapter2_travelPast_home2_throw




####################################################
label chapter2_travelPast_home2_burn:

    scene bg home

    show protagonist neutral at t11
    p "I can’t believe I spent $300 on this"
    p "Well… goodbye Wookie costume. You will be missed."
    n "Show same P with Wookie, but the costume is now on fire"
    jump chapter2_travelPast_home2_end



####################################################
label chapter2_travelPast_home2_throw:

    scene bg home

    show protagonist neutral at t11
    p "I can’t believe I spent $300 on this"
    p "Well… goodbye Wookie costume. You will be missed."
    n "Show same P holding Wookie costume over trash can"
    jump chapter2_travelPast_home2_end



####################################################
label chapter2_travelPast_home2_end:
    # NOTE: NOW THIS PART BRANCHES OUT BASED ON WHETHER YOU COMPLETED ALREADY THE MAIN MISSION

    # IF MAIN MISSION COMPLETED
    if mission1timegod_success == 1:
        show protagonist neutral at t11
        p "I rescued the pen, destroyed my costume."
        p "Now I definitely won’t be showing up accidentally dressed as Wookie..."
        p "So what now?"
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
        g "In the future, you will accomplish my instructions before fulfilling your personal agenda."
        g "Do not abuse my generosity."

        p "Jeez, alright. I’m going already."
        p "Where should I go now?"
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

    show timegod neutral at t11
    g "Thank you for bringing me this pen."
    g "This was truly a beneficial exchange."

    p "xxxx"

    menu:
        p "Ahhh.. What do I do now?"
        "Yeah, that went well.":
            g "Interesting. I trust you will continue to have such success in the future."
        "I feel like something is wrong here.":
            g "Interesting. It seems to me you performed splendidly. I trust you will continue to have such success in the future."

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
