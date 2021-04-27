####################################################
label start_chapter2:

    # INITIALIZE VARIABLES FOR VISITED PLACES
    $ mission2cafe = 0


    n "{i}A few weeks later... {p}At the end of another exciting day in the office..."
    scene bg office with Dissolve(0.5)

    show protagonist neutral at t11
    p "Ok it's almost 5pm. I'm heading out."
    n "{i}You walk past and see a poster on the wall"
    show protagonist hmm
    p "Hmm... I wonder what that is?"
    n "{i}There are a bunch of stormtroopers forming the words {p}\"STAR {w}- WARS {w}- DAY\" "
    show protagonist excited
    p "Oh YES! OH YES OH YES! Next Monday is STAR WARS DAY! {p}I am going to absolutely SMOKE the competition."
    show protagonist anxious
    p "What should I be? {w}Princess Leia? {w}Stormtrooper? {p}I do a mean Darth Vader impression too. {w}Wookiee? Hmm...."

    scene black with Dissolve(0.5)
    jump chapter2_office_StarWarsDay1


####################################################
label chapter2_office_StarWarsDay1:

    n "{i}One week later..."
    scene bg office with Dissolve(0.5)

    show boss neutral at t33
    boss "What the HELL are you wearing?"

    show protagonist wookie_normal at t31
    p "I'm a Wookiee! Star Wars day? Said so on the poster on the wall?"

    show boss facepalm at t33
    boss "That's NEXT Monday! Not TODAY! {w}Today's our investor meeting! You're presenting and you show up dressed as Bigfoot?"

    show protagonist wookie_anxious at t31
    p "Oh..."
    p "I'm actually a Wookiee... {w}Not Bigfoot... {w}They're different!!!"

    scene black with Dissolve(1.0)
    n "{i}In the meeting, you are the only one wearing a costume, while everyone else has a nice suit. The boss is facepalming while looking at you. It's an utter disaster.{\i}"
    # n "TODO - image of poster and scene with people in suits, protagonist and boss reactions"

    jump chapter2_home_meetTimeGod



####################################################
label chapter2_home_meetTimeGod:

    scene bg home with Dissolve(0.5)

    show timegod neutral at t11
    g "Whoa you really messed that up. {p}I see you've had a bad day... {w}AGAIN!"
    show timegod laugh
    g "I have a proposition for you."
    show timegod creepy
    g "Would you like a do over... a chance to undo your mistakes?"
    hide timegod

    menu:
        g "Would you like a do over... a chance to undo your mistakes?"
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
    show timegod laugh
    g "While you're at it, feel free to destroy this abomination of a Bigfoot costume."

    menu:
        "So what do you need me to get?":
            show timegod neutral at t11
            g "Interesting question."
        "Why me?":
            show timegod neutral at t11
            g "Interesting question."
        "Can I say no?":
            show timegod neutral at t11
            g "Interesting question."

    show timegod happy
    g "Your boss has a particularly nice fountainhead pen which I have admired for quite a while."
    g "During work hours, he always maintained at most a 4 foot distance from this favorite object of his."
    show timegod angry
    g "Regrettably, this past Sunday he dropped this pen down the elevator shaft of your office building."
    show timegod happy
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

    show timegod neutral at t11
    g "Are you ready to go?"
    show timegod snap1
    g "Are you ready to go?"
    show timegod snap2
    g "Are you ready to go?"
    show timegod at thide
    hide timegod

    scene black with Dissolve(0.5)


####################################################
label chapter2_travelPast1:

    scene bg home with Dissolve(0.5)

    show protagonist neutral at t11
    p "I need to obtain that pen and somehow get rid of my costume. {w}What should I do first?"
    hide protagonist

    menu:
        p "I need to obtain that pen and somehow get rid of my costume. What should I do first?"
        "Go to the office":
            scene bg home with Dissolve(0.5)
            jump chapter2_travelPast_office1
        "Go to the cafe":
            scene bg home with Dissolve(0.5)
            jump chapter2_travelPast_cafe1
        "Stay home":
            jump chapter2_travelPast_home1



####################################################
label chapter2_travelPast_office1:

    scene bg office
    # starting the office part always completes the main mission
    $ mission2timegod_success = 1

    show protagonist neutral at t11
    p "So I just have to go get the boss's lucky pen."
    show protagonist talking
    p "Easy."
    show protagonist at thide
    hide protagonist

    scene bg office with Pause(1.0)
    show boss pen at t11
    n "{i}The boss is really here, even if it's Sunday. He really cannot take a break from work."
    n "{i}So focused, so motivated, he is really impressive!"
    n "{i}But, he still has the pen..."
    show boss at thide
    hide boss

    n "{i}Oh shoot, he went back to his office!!!"

    show protagonist anxious at t11
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
    p "Hmmm..."
    p "What if I pulled the fire alarm? That should empty the building."
    show protagonist at thide
    hide protagonist

    # n "{i}P sprite turns into P sprite pulling fire alarm{\i}"
    # n "Alternative (if it's easier to draw): {i}full-screen image of fire alarm on wall, with hand pulling it{\i}"
    n "{i}You do what needs to be done. A few seconds later, you hear the sound of the fire alarm{\i}"

    show boss neutral at t11
    boss "Uhm?"
    show boss panicking
    boss "FIRE! FIRE! EVERYONE, GET OUTTA HERE!"
    show boss at thide
    hide boss

    show protagonist joy at t11
    p "OK, this is my chance."
    show protagonist woohoo
    p "Go go go!"
    show protagonist at thide
    hide protagonist with Pause(1.5)

    show protagonist joy at t11
    p "AH HA! I got it!"
    show protagonist neutral
    p "What should I do now?"
    hide protagonist

    if mission2cafe == 0:
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

    show protagonist hmm at t11
    p "It's 10am right now. I could just hide until the boss leaves work."
    show protagonist at thide
    hide protagonist

    p "..."
    p "...."
    p "....."
    p "......"
    scene bg office_dark with dissolve
    #p "......."

    show protagonist joy at t11
    p "Yes! Finally, everyone left!"
    show protagonist surprised at t11
    p "Oh! My back! Crouching behind a potted plant really does things to your body."
    show protagonist talking at t11
    p "Ok, now I gotta get that pen!"
    show protagonist at thide
    hide protagonist

    scene bg office_dark with Pause(1.5)

    # n "{i}P sneaks off screen in the direction of the pen{\i}"
    # n "{i}P returns, triumphant, holding the pen{\i}"

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
        "Go to the cafe" (disabled=True) if mission2cafe == 1:
            scene bg cafeoutdoor_dark
        "Go to the cafe" (disabled=False) if mission2cafe == 0:
            scene bg cafeoutdoor_dark
            n "{i}The cafe is closed.{\i}"
            n "{i}It makes sense. It is almost 11 pm...{\i}"

            if mission2personal_success == 0:
                show protagonist hmm at t11
                p "Shoot... {w}I should go prevent the Wookie fiasco!"
                jump chapter2_failedDestruction
            else:
                show timegod laugh at t11
                g "Oh, you amuse me so much. {w}Getting hungry at 11 pm?. {w}I'm taking you back"
                show timegod snap1 at t11
                show timegod snap2 at t11
                scene black with Dissolve(2.0)
                jump chapter2_returnPen



####################################################
label chapter2_travelPast_home1:

    scene bg home
    # visiting home on time completes the personal mission
    $ mission2personal_success = 1

    show protagonist neutral at t11
    p "Now, I need to make sure I don't wear that costume to work."
    show protagonist at thide
    hide protagonist with Pause(1.5)

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

    show protagonist anxious at t11
    p "I can't believe I spent $300 on this"
    show protagonist wookie_fire at t11
    p "Well... goodbye Wookiee costume. You will be missed."
    show protagonist at thide
    hide protagonist

    jump chapter2_travelPast_home2_end



####################################################
label chapter2_travelPast_home2_throw:

    scene bg home

    show protagonist anxious at t11
    p "I can't believe I spent $300 on this"
    show protagonist wookie_throw at t11
    p "Well... Goodbye Wookiee costume. You will be missed."
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
    #jump chapter2_returnPen_snap

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
        g "This was truly a beneficial exchange."
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
        g "This was truly a beneficial exchange."
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
    scene bg home_dark
    show protagonist neutral at t31
    p "Now, I just gotta get rid of that costume..."
    n "{i}You hear loud bangs in the background.{\i}"
    show protagonist anxious at t31
    p "Oh dang."
    p "My past self is home..."
    show pastprotagonist hey_left at t33
    pp "Hey you!"
    p "HIDE!"
    show protagonist at thide
    hide protagonist
    n "{i}You hide under the table.{\i}"
    show pastprotagonist hmm at t33
    pp "Hmm...Huh?? Was that... me???"
    pp "What did I just witness?"
    n "{i}The smoke alarm rings.{\i}"
    show pastprotagonist surprise
    # TODO show pp SURPRISED
    pp "SHOOT! Did I burn my pot roast?"
    n "{i}Your past self disappears from where he came from.{\i}"
    hide pastprotagonist neutral
    n "{i}With anxiety, you peek out from under the table.{\i}"
    show protagonist anxious at t31
    p "What do I do now?? How am I supposed to destroy my costume with my past self in the house?"
    hide protagonist anxious
    show timegod laugh at t11
    g "Well... Looks like you're not going to get anything done. Im bringing you back."
    p "Wait! But –– but my costume!"
    show timegod snap1 at t11
    p "Wait! But –– but my costume!"
    show timegod snap2 at t11
    scene black with Dissolve(0.5)
    jump chapter2_returnPen


####################################################
label chapter2_travelPast_cafe1:

    $ mission2cafe = 1

    show bg cafe with Dissolve(0.5)

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

    show bg cafe with Dissolve(0.5)

    show protagonist excited at t11
    p "YES! I GOT THE PEN!"
    show protagonist anxious at t11
    p "Oh dang. I stole a pen."
    p "Am I going to be arrested?"
    p "Oh dang."
    show protagonist neutral at t11
    p "No it's fine. The pen was going to be lost anyway."
    p "But maybe he could find it again?"
    p "I need to clear my mind. Maybe I should grab something to eat."
    hide protagonist

    menu:
        "Grab some food":
            scene black with Dissolve(0.5)
            jump chapter2_travelPast_cafe3
        "Go home":
            scene black with Dissolve(0.5)
            jump chapter2_travelPast_home1


####################################################
label chapter2_travelPast_cafe3:

    scene bg cafe with Dissolve(0.5)

    show protagonist neutral at t11
    p "Oh, looks like there's a new barista around. I wonder what happened to the old one."
    show protagonist joy
    p "Hmm... I'll have an egg salad sandwich."
    p "Oh, also extra onions."
    p "And extra pickles."
    p "And extra garlic."
    scene black with Dissolve(0.5)
    scene bg cafe with Dissolve(0.5)
    show protagonist neutral at t11
    p "Mmm. This is delicious."
    p "It's so nice here, I think I'll stay for a while."
    scene black with Dissolve(1.0)
    n "{i}You thoroughly enjoy your meal, and a long time passes. By the time you leave, the sun has fallen below the horizon.{\i}"

    if mission2personal_success == 0:
        jump chapter2_failedDestruction
    else:
        jump chapter2_travelPast_home3


####################################################
label chapter2_travelPast_cafe4:
    $ mission2cafe = 1

    scene bg cafe with Dissolve(0.5)

    show protagonist anxious at t11
    p "Oh dang. I stole a pen."
    p "Am I going to be arrested?"
    p "Oh dang."
    show protagonist neutral
    p "No it's fine. The pen was going to be lost anyway."
    show protagonist hmm
    p "But maybe he could find it again?"
    p "Is that Time God even real?"
    show protagonist neutral
    p "Oh, looks like there's a new barista around. I wonder what happened to the old one."
    show protagonist joy
    p "Hmm... I'll have an egg salad sandwich."
    p "Oh, also extra onions."
    p "And extra pickles."
    p "And extra garlic."
    scene black with Dissolve(0.5)
    scene bg cafe with Dissolve(0.5)
    show protagonist neutral at t11
    p "Mmm. This is delicious."
    p "It's so nice here, I think I'll stay for a while."
    scene black with Dissolve(1.0)
    scene black with Pause(1.0)
    scene bg cafe with Dissolve(1.0)
    show timegod angry at t11
    g "Where in the world have you been?"
    show timegod laugh
    g "Oh! You're still eating?"
    g "I'm bringing you back right now!"
    show timegod snap1
    g "I'm bringing you back right now!"
    show timegod snap2
    g "I'm bringing you back right now!"
    show timegod at thide
    hide timegod

    scene black with Dissolve(0.5)
    jump chapter2_end



####################################################
label chapter2_end:

    show black with Dissolve(0.5)
    n "One day later"
    scene bg office with Dissolve(0.5)
    show protagonist anxious at t31
    p "Jeez, I guarantee this isn't gonna be good."
    p "Hi boss, you wanted to see me?"

    # if True:
    if mission2personal_success == 1:
        jump chapter2_end_success
    else:
        jump chapter2_end_failure



####################################################
label chapter2_end_success:
    # 6.2 - Lose Costume

    show boss happy at t33
    boss "I'd like to congratulate you for your work yesterday, {w}really knocked it out of the park on this one."

    # (If personal mission from level 1 passed)
    if mission1personal_success == 1:
        boss "You've been showing real improvement since you made coffee that last meeting."
    show boss at s33

    show protagonist blush at t31
    p "OH YEAH! Well, how did it work out afterwards?"
    show protagonist at s31

    show boss sad at t33
    boss "Uh, less stellar than expected unfortunately. There was a slight issue..."
    scene black with Dissolve(1.0)
    n "{i}As the boss recaps the meeting, you can somehow exactly picture the scene.{\i}"
    n "{i}You were wearing a suit, and were quite confident in your presentation. The investors all seemed impressed.{\i}"
    n "{i}The boss, however, seemed to be a bit anxious. Perhaps he was distracted by something?{\i}"
    scene bg office with Dissolve(1.0)
    show protagonist talking at t31
    show boss neutral at t33
    p "Oh, okay. Well, thank you for the compliment! I'm a great worker, haha!"
    show protagonist neutral at t31
    boss "That is all, also, let me know if you have seen a personalized fountainhead pen with my initials. {w}Please, it would mean quite a lot to me."

    show boss at thide
    hide boss
    show protagonist at thide
    hide protagonist

    scene black with Dissolve(1.0)
    n "END OF MISSION 2"
    n "  "
    jump start_chapter3
    #return


####################################################

label chapter2_end_failure:
    # 6.1 - Doesn't Lose Costume (Similar to original)

    show boss angry at t33
    boss "I don't think this needs to be said, but yesterday was a disaster."

    # (If personal mission from level 1 failed)
    if mission1personal_success == 0:
        boss "First, the 'bean water' saga and now this."

    show boss neutral
    boss "That meeting was ridiculous, went as awful as possible for both of us."
    scene black with Dissolve(1.0)
    n "{i}As the boss recaps the meeting, you can somehow exactly picture the scene.{\i}"
    n "{i}In the meeting, you were the only one wearing a costume, while everyone else had a nice suit. The boss was facepalming while looking at you. It was an utter disaster.{\i}"
    n "{i}Not only that, but the boss seemed to be quite panicked about something. What could have been going on?{\i}"
    scene bg office with Dissolve(1.0)
    show protagonist anxious at t31
    show boss angry at t33
    boss "I still don't get how you missed the date on this one. The poster was quite clear on dates."
    show boss at s33

    show protagonist anxious at t31
    p "Uhm, accidents happen? {w}Was it at least a good costume? I spent around 300 dollars on it."
    show protagonist at s31

    show boss neutral at t33
    boss "No, it really wasn't, now please leave."
    show boss sad
    boss "On another note, if you've seen a personalized pen with my initials, PLEASE return it. {w}It would mean quite a lot to me."
    show boss at thide
    hide boss
    show protagonist at thide
    hide protagonist

    scene black with Dissolve(1.0)
    n "END OF MISSION 2"
    n "  "
    jump start_chapter3
    #return
