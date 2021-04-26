####################################################
label start_chapter2:

    ### INITIALIZE MISSIONS
    $ mission2personal_success = 0
    $ mission2timegod_success  = 0

    ### CAFE TRACKER
    $ mission2cafe = 0

    # TO BE REMOVED LATER
    $ mission1personal_success = 0

    scene bg office

    show protagonist neutral at t11
    p "Ok it's almost 5pm. I'm heading out."
    n "{i}You walk past and see a poster on the wall{\i}"
    show protagonist hmm at t11
    p "Hmm... I wonder what that is?"
    n "{i}Poster says \"STAR WARS DAY\"{\i}"
    show protagonist excited at t11
    p "Oh YES! OH YES OH YES! Next Monday is STAR WARS DAY! I am going to absolutely SMOKE the competition."
    show protagonist anxious at t11
    p "What should I be? Princess Leia? Stormtrooper? I do a mean Darth Vader impression too. Wookiee? Hmm...."

    scene black with Dissolve(2.0)
    jump chapter2_office_StarWarsDay1


####################################################
label chapter2_office_StarWarsDay1:

    scene bg office

    n "{i}One week later...{\i}"
    show boss neutral at t33
    boss "What the HELL are you wearing?"

    show protagonist wookie_normal at t31
    p "I'm a Wookiee! Star Wars day? Said so on the poster on the wall?"

    show boss angry at t33
    boss "That's NEXT Monday! Not TODAY! Today's our investor meeting! You're presenting and you show up dressed as Bigfoot?"

    show protagonist wookie_anxious at t31
    p "Oh..."
    scene black with Dissolve(2.0)

    n "TODO - image of poster and scene with people in suits, protagonist and boss reactions"
    # [Image of Wookie P with a chart he's presenting. We see the backs of a bunch of people wearing suits in the foreground.
    # B is standing off to the side, facepalming. P is visibly freaking out]
    jump chapter2_home_meetTimeGod



####################################################
label chapter2_home_meetTimeGod:

    scene bg home

    show timegod neutral at t11
    g "Whoa you really messed that up. I see you've had a bad day...again."
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

    g "I'm going to need you to pick something up for me."
    show timegod laugh at t11
    g "While you're at it, feel free to destroy this abomination of a Bigfoot costume."
    show timegod neutral at t11
    g "Are you ready to go?"
    show timegod snap1 at t11
    g "Are you ready to go?"
    show timegod snap2 at t11
    g "Are you ready to go?"
    hide timegod

    scene black with Dissolve(1.0)
    scene bg home with Dissolve(1.0)

    menu:
        "So what do you need me to get?":
            show timegod neutral at t11
            g "Interesting question."
        "Are we in the past now? How did you do that?":
            show timegod neutral at t11
            g "Interesting question."
        "Shouldn't you wait until I agree before sending me back in time?":
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
        "Got it, I'll bring it to you soon.":
            show timegod neutral at t11
            g "I was sure you would have accepted."
        "Why do you care so much about a pen?":
            show timegod neutral at t11
            g "Interesting question."

    show timegod laugh at t11
    g "I hope your journey is fruitful!"
    scene bg home with Dissolve(1.0)



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
    # starting the office part always completes the main mission
    $ mission2timegod_success = 1

    show protagonist neutral at t11
    p "So I just have to go get the boss's lucky pen."
    show protagonist excited at t11
    p "EASY!"
    show protagonist at thide
    hide protagonist

    n "{i}B pops into view but not talking to P or anything. and B is holding his pen{\i}"

    show protagonist anxious at t11
    p "Oh. Shoot. He's literally in his office holding his pen."
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
    n "Alternative (if it's easier to draw): {i}full-screen image of fire alarm on wall, with hand pulling it{\i}"
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

    if mission2personal_cafe == 0:
        menu:
            p "What should I do now?"
            "Go home":
                if mission2personal_success == 0:
                    jump chapter2_travelPast_home1
                else:
                    jump chapter2_travelPast_home3
            "Go to the cafe":
                jump chapter2_travelPast_cafe2
    else:
        menu:
            p "What should I do now?"
            "Go home":
                if mission2personal_success == 0:
                    jump chapter2_travelPast_home1
                else:
                    jump chapter2_travelPast_home3



####################################################
label chapter2_travelPast_office2hide:

    #scene bg home

    show protagonist hmm at t11
    p "It's 10am right now. I could just hide until the boss leaves work."
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
label chapter2_travelPast_home1:

    scene bg home
    # visiting home on time completes the personal mission
    $ mission2personal_success = 1

    show protagonist neutral at t11
    p "Now, I need to make sure I don't wear that costume to work."
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
    p "I can't believe I spent $300 on this"
    show protagonist wookie_throw at t11
    p "Well... goodbye Wookiee costume. You will be missed."
    show protagonist at thide
    hide protagonist

    jump chapter2_travelPast_home2_end



####################################################
label chapter2_travelPast_home2_throw:

    scene bg home

    show protagonist surprised at t11
    p "I can't believe I spent $300 on this"
    show protagonist wookie_throw at t11
    p "Well... goodbye Wookiee costume. You will be missed."
    show protagonist at thide
    hide protagonist

    jump chapter2_travelPast_home2_end



####################################################
label chapter2_travelPast_home2_end:
    # NOTE: NOW THIS PART BRANCHES OUT BASED ON WHETHER YOU COMPLETED ALREADY THE MAIN MISSION

    # IF MAIN MISSION COMPLETED
    if mission2timegod_success == 1:
        show protagonist talking at t11
        p "I rescued the pen, destroyed my costume."
        show protagonist anxious at t11
        p "Now I definitely won't be showing up accidentally dressed as Wookiee..."
        show protagonist hmm at t11
        p "So what now?"
        hide protagonist

        if mission2cafe == 0:
            menu:
                p "So what now?"
                "Travel back to present and forget about all this":
                    jump chapter2_returnPen_snap
                "Destroying the costume made me hungry. I could have lunch now":
                    jump chapter2_travelPast_cafe4
        else:
            menu:
                p "So what now?"
                "Travel back to present and forget about all this":
                    jump chapter2_returnPen_snap


    # IF MAIN MISSION NOT COMPLETED
    if mission2timegod_success == 0:
        show timegod neutral at t11
        g "I see that you have disposed of the costume."
        show timegod creepy at t11
        g "In the future, you will accomplish my instructions before fulfilling your personal agenda."
        show timegod angry at t11
        g "DO NOT ABUSE MY GENEROSITY."
        show timegod at thide
        hide timegod

        show protagonist anxious at t11
        p "Jeez, alright. I'm going already."
        show protagonist hmm at t11
        p "Where should I go now?"
        hide protagonist

        if mission2cafe == 0:
            menu:
                p "Where should I go now?"
                "Go to the office":
                    jump chapter2_travelPast_office1
                "Go to the cafe":
                    jump chapter2_travelPast_cafe1
        else:
            menu:
                p "Where should I go now?"
                "Go to the office":
                    jump chapter2_travelPast_office1



####################################################
label chapter2_travelPast_home3:

    scene bg home

    show protagonist neutral at t11
    p "This is done. What's next?"
    hide protagonist

    menu:
        p "This is done. What's next?"
        "Deliver the pen":
            jump chapter2_returnPen_snap
        "Destroy the costume" (disabled=False) if mission2personal_success==0:
            jump chapter2_failedDestruction
        "Destroy the costume" (disabled=True)  if mission2personal_success==1:
            jump chapter2_failedDestruction

####################################################
label chapter2_returnPen:

    scene bg home

    show timegod happy at t11
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
label chapter2_returnPen_snap:

    scene bg home

    show timegod happy at t11
    g "Thank you for bringing me this pen."
    show timegod happy at t11
    g "This was truly a beneficial exchange."
    hide timegod

    menu:
        p "Ahhh.. What do I do now?"
        "Yeah, that went well.":
            show timegod neutral at t11
            g "Interesting. I trust you will continue to have such success in the future."
            show timegod snap1 at t11
            g "Interesting. I trust you will continue to have such success in the future."
            show timegod snap2 at t11
            g "Interesting. I trust you will continue to have such success in the future."
            show timegod at thide
            hide timegod
            scene black with Dissolve(2.0)
        "I feel like something is wrong here.":
            show timegod neutral at t11
            g "Interesting. It seems to me you performed splendidly. I trust you will continue to have such success in the future."
            show timegod snap1 at t11
            g "Interesting. It seems to me you performed splendidly. I trust you will continue to have such success in the future."
            show timegod snap2 at t11
            g "Interesting. It seems to me you performed splendidly. I trust you will continue to have such success in the future."
            show timegod at thide
            hide timegod
            scene black with Dissolve(2.0)

    jump chapter2_end


####################################################
### TODO: replace some narrator lines with animations / correct images
label chapter2_failedDestruction:
    scene bg home
    show protagonist neutral at t31
    p "Now, I just gotta get rid of that costume..."
    n "You hear loud bangs in the background"
    show protagonist anxious at t31
    p "Oh dang."
    p "My past self is home..."
    show pastprotagonist neutral at t33
    pp "Hey...Hey!"
    p "HIDE!"
    n "(You hide under the table)"
    hide protagonist anxious
    pp "Hmm...Huh?? Was that... me???"
    pp "What did I just witness?"
    n "Smoke alarm rings."
    show pastprotagonist surprised
    # TODO show pp SURPRISED
    n "TODO: show past self is surprised"
    pp "SHOOT! Did I burn my pot roast?"
    n "Your past self disappears from where he came from."
    hide pastprotagonist neutral
    n "With anxiety, you peek out from under the table"
    show protagonist anxious at t31
    p "What do I do now?? How am I supposed to destroy my costume with my past self in the house?"
    hide protagonist anxious
    show timegod laugh at t11
    g "Well... Looks like you're not going to get anything done. Im bringing you back."
    p "Wait! But –– but my costume!"
    show timegod snap1 at t11
    show timegod snap2 at t11
    scene black with Dissolve(2.0)
    jump chapter2_returnPen


####################################################
label chapter2_travelPast_cafe1:
    $ mission2cafe = 1
    show bg cafe
    show protagonist neutral at t11
    p "Is that Time God even real? I need to clear my mind. Maybe I should grab something to eat."
    p "Oh, looks like there's a new barista around. I wonder what happened to the old one."
    p "I will grab a quick lunch."
    scene black with Dissolve(2.0)
    show bg cafe with Dissolve(2.0)
    p "Now that I've eaten, I think I'm ready to complete the Time God's task."
    if mission2personal_success == 0:
        menu:
            "Go home":
                jump chapter2_travelPast_home1
            "Go to the office":
                jump chapter2_travelPast_office1
    else:
        menu:
            "Go to the office":
                jump chapter2_travelPast_office1


####################################################
label chapter2_travelPast_cafe2:
    $ mission2cafe = 1
    show bg cafe
    show protagonist excited at t11
    p "YES! I GOT THE PEN!"
    hide protagonist excited
    show protagonist anxious at t11
    p "Oh dang. I stole a pen."
    p "Am I going to be arrested?"
    p "Oh dang."
    hide protagonist anxious
    show protagonist neutral at t11
    p "No it's fine. The pen was going to be lost anyway."
    p "But maybe he could find it again?"
    p "I need to clear my mind. Maybe I should grab something to eat."
    menu:
        "Grab some food":
            jump chapter2_travelPast_cafe3
        "Go home":
            jump chapter2_travelPast_home3


####################################################
label chapter2_travelPast_cafe3:
    scene bg cafe
    show protagonist neutral at t11
    p "Oh, looks like there's a new barista around. I wonder what happened to the old one."
    p "Hmm... I'll have an egg salad sandwich."
    p "Oh, also extra onions."
    p "And extra pickles."
    p "And extra garlic."
    n "TODO: Image of protagonist eating, followed by the same image but with darker sky. (That is, it becomes night while eating)."
    jump chapter2_failedDestruction


####################################################
label chapter2_travelPast_cafe4:
    $ mission2cafe = 1
    scene bg cafe
    show protagonist anxious at t11
    p "Oh dang. I stole a pen."
    p "Am I going to be arrested?"
    p "Oh dang."
    hide protagonist anxious
    show protagonist neutral at t11
    p "No it's fine. The pen was going to be lost anyway."
    hide protagonist neutral
    show protagonist hmm at t11
    p "But maybe he could find it again?"
    p "Is that Time God even real?"
    hide protagonist hmm
    show protagonist neutral at t11
    p "Oh, looks like there's a new barista around. I wonder what happened to the old one."
    p "Hmm... I'll have an egg salad sandwich."
    p "Oh, also extra onions."
    p "And extra pickles."
    p "And extra garlic."
    n "TODO Image of protagonist eating, followed by the same image but with darker sky. (That is, it becomes night while eating)."
    hide protagonist neutral
    show timegod angry at t11
    g "Where in the world have you been?"
    hide timegod angry
    show timegod laugh at t11
    g "Oh! You're still eating?"
    g "I'm bringing you back."
    scene black with Dissolve(2.0)
    jump chapter2_end



####################################################
label chapter2_end:
    scene bg office
    # Boss is either talking w/ P or asks him to come in
    show protagonist anxious at t31
    p "Jeez, I guarantee this isn't gonna be good."
    p "You wanted to see me?"
    if True:
    # if mission2personal_success == 1:
        jump chapter2_end_success
    else:
        jump chapter2_end_failure



####################################################
label chapter2_end_success:
    # 6.2 - Lose Costume
    show boss neutral at t33
    boss "I'd like to congratulate you for your work yesterday, really knocked it out of the park on this one."

    # (If personal mission from level 1 passed)
    if mission1personal_success == 1:
        boss "You've been showing real improvement since you made coffee that last meeting."
    show protagonist joy at t31
    p "OH YEAH! Well, how did it work out afterwards?"
    boss "Uh, less stellar than expected unfortunately. There was a slight issue..."
    n "Flashback graphic of the same scene except protagonist in normal clothing, looking fairly confident in presenting. Boss shown to be fairly panicked."
    p "Oh, okay. Well, thank you for the compliment! I'm a great worker, haha!"
    boss "That is all, also, let me know if you have seen a personalized fountainhead pen with my initials. Please, it would mean quite a lot to me."
    return


####################################################

label chapter2_end_failure:
    # 6.1 - Doesn't Lose Costume (Similar to original)
    show boss angry at t33
    boss "I don't think this needs to be said, but yesterday was a disaster."
    # (If personal mission from level 1 failed)
    if mission1personal_success == 0:
        boss "First, the 'bean water' saga and now this."
    boss "That meeting was ridiculous, went as awful as possible for both of us."
    n "Flashback graphic akin to prior (Image of Wookiee P with a chart he's presenting. We see the backs of a bunch of people wearing suits in the foreground. B is standing off to the side, facepalming. P is visibly freaking out] albeit this time also shows the boss slightly panicking)"
    boss "I still don't get how you missed the date on this one. The poster was quite clear on dates."
    p "Uhm, accidents happen? Was it at least a good costume? I spent around 300 dollars on it."
    boss "No, it really wasn't, now please leave. On another note, if you've seen a personalized pen with my initials, PLEASE return it."
    return

label chapter2_EXAMPLE:

    scene bg home

    show protagonist neutral at t11
    p "xxxx"
    p "xxxx"
    p "xxxx"
    p "xxxx"
    p "xxxx"
    p "xxxx"
