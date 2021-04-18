####################################################
label start_chapter4:
    # play music "funiculifunicula.mp3" fadeout 1       # ADD MUSIC

    scene bg office

    show boss neutral at t33
    boss "Tomorrow’s supposed to be the annual employee retreat. But budget cuts this year."
    boss "I was thinking of organizing a nice outdoor picnic for everyone instead. You want to take care of the grill?"
    show boss neutral at s33

    show protagonist excited at t31
    p "Oh yes, I’d love to! I am a master chef. Boss, I promise you"
    show protagonist joy
    p "Tomorrow you’re going to eat the best burgers you’ve ever had!"

    show protagonist at thide
    hide protagonist
    show boss at thide
    hide boss
    scene black with Dissolve(2.0)



label chapter4_office_start:

    n "The day after..."

    scene bg office

    show protagonist excited at t31
    n "Picture of the protagonist, happy, holding burger in plate"
    p "So... what does everyone think?"
    show protagonist excited at s31

    show boss neutral at t33
    n "The boss seems very happy"
    boss "Wow, I truly was not expecting this from you. This is truly the best burger I’ve ever had!"
    show boss neutral at s33

    show coworker neutral at t11
    coworker "MMM! The onion, the extra pickles, the garlic scent."
    show coworker neutral at s11

    show boss neutral at t33
    boss "It’s strong... but not overpowering. Really highlights the umami of the meat."
    boss "Speaking of, that is some REALLY good burger meat. Where did you get it from?"
    show boss neutral at s33

    show protagonist joy at t31
    p "Oh, just the grocery store here on the way here. I’m so happy you like it!"
    show protagonist joy at s31

    show boss neutral at t33
    n "The boss starts panicking"
    boss "Wait."
    boss "What is going on."
    boss "Oh, noooo. MY STOMACH!"
    n "image of boss throwing up"
    show boss neutral at s33

    show protagonist surprised at t31
    p "Are you ok? What’s going on?"
    show protagonist surprised at s31

    show boss neutral at t33
    boss "I’m... fine. You said the grocery store here? You know that place..."
    n "The boss vomits again"
    show boss neutral at s33

    show protagonist anxious at t31
    p "Oh dang. Oh geez. Oh dang. Did I just poison the boss?"
    show protagonist hmm
    p "Oh heck that’s a lot of throw-up. Are their guts coming out?"
    show protagonist anxious
    p "Oh no, are they going to die??? Did I just kill the boss?"
    show protagonist surprised at s31

    show coworker neutral at t11
    n "the coworker also start vomiting"

    show coworker at thide
    hide coworker
    show boss at thide
    hide boss

    show protagonist surprised at t31
    p "Did I just kill the entire office building?"
    show protagonist anxious
    p "What do I do? Can I save them?"
    hide protagonist

    menu:
        p "What do I do? Can I save them?"
        "Panic":
            show protagonist anxious at t11
        "Freak out":
            show protagonist anxious at t11
        "Lose your cool":
            show protagonist anxious at t11

    show protagonist anxious at t11
    n "image of dialing 911, ambulance arriving, and coworkers/boss being carried on a stretcher"
    show protagonist surprised
    p "Oh no. Oh no. Oh, no no no no."
    show protagonist hmm
    p "Ok, I gotta get out of here."
    show protagonist at thide
    hide protagonist
    scene black with Dissolve(2.0)


####################################################
label chapter4_home_meetTimeGod:

    scene bg home

    show protagonist anxious at t11
    p "Is there anything I can do to fix this?"
    p "If only I could travel back again."
    show protagonist suprised at s11
    p "If only I could travel back again."
    show protagonist suprised at s31

    show timegod creepy at t33
    g "I have a mission for you."
    show timegod at s33

    show protagonist anxious at t31
    p "Wonderful. Send me back now. I need to go back."
    p "I’ll do whatever, please just send me back."
    show protagonist at s31

    show timegod normal at t33
    g "Interesting. Very interesting."
    g "You have been performing quite satisfactorily. It is time to entrust you with a more important task."
    show laugh normal
    g "Although important, this task is not particularly difficult."
    g "You must simply place a certain object at a specific place at a particular time."
    show angry normal
    g "However, being off by even a minute could have disastrous consequences."
    g "If you fail in this mission, I will never appear before you again."
    show timegod happy
    g "On the other hand, success will yield great rewards."
    g "If you achieve this goal, you will have the opportunity to fix any mistake of your choosing."
    show timegod laugh
    g "Name a time, and I will send you there."
    g "Are you ready to accept this responsibility?"
    hide protagonist
    hide timegod

    menu:
        g "Are you ready to accept this responsibility?"
        "Yes. Yes, please send me back now":
            show timegod normal at t11
        "I am ready":
            show timegod normal at t11
        "I need to think about it":
            show timegod normal at t11

    g "Interesting answer. No time to waste!"
    show timegod happy
    g "Go to the intersection of Kronos Avenue with Fate Street."
    g "There will be a pile of rocks at a construction site on the southeast corner."
    g "Select the largest one."
    show timegod laugh
    g "You must place this stone exactly 47 inches to the east of the red bench on the median."
    g "It must be placed at exactly 9:00 am."
    show timegod angry
    g "Both the location and time are vitally important."
    g "A second later or an inch further, and your efforts will result in failure."
    show timegod creepy
    g "Remember carefully: 9:00 am on the dot. 47 inches to the east of the red bench."
    g "I wish you luck in your endeavour."
    show timegod snap1 at t11
    g "Ready..."
    show timegod snap1 at t11
    g "Set..."
    show timegod snap1 at t11
    g "Go!"
    show timegod snap2 at t11
    g "Go!"
    hide timegod

    scene black with Dissolve(1.0)

    n "{i}The Time God snaps his fingers and you are transported back in the past.{\i}"
    n "{i}It's 7:30am.{\i}"

    scene bg cafeoutdoor

    show protagonist neutral at t11
    p "I just need to do this task."
    p "Then I can save my boss and my coworkers as well."
    p "I have another chance. Let’s do this."
    p "OK it looks like it’s 7:30 am."
    p "I have to put the rock down at 9 exactly."
    p "Maybe I should head there early just to be safe?"
    hide protagonist

    # INITIALIZE VARIABLES FOR VISITED PLACES
    $ flag_visited_cafe = 0;
    $ flag_visited_office = 0;
    $ flag_visited_home = 0;

    menu:
        p "Maybe I should head there early just to be safe?"
        "Go to the Street":
            jump chapter3_street_early
        "Go to the Cafe":
            $ flag_visited_cafe = 1;
            jump chapter3_cafe_prelude
        "Go to the Office":
            $ flag_visited_office = 1;
            jump chapter3_office_prelude
        "Stay Home for a while":
            $ flag_visited_home = 1;
            jump chapter3_home_prelude



####################################################
label chapter3_street_early:

    scene bg home

    show protagonist neutral at t11
    p "Oof, finally made it here. What time is it?"
    p "Looks like it’s 8:05 am. I have plenty of time to kill."
    p "Guess I’ll wait at that bench."

    jump chapter3_street_decision


####################################################
label chapter3_street_decision:

    scene bg home

    show protagonist neutral at t11
    p "xxxx"
    p "xxxx"
    p "xxxx"
    p "xxxx"
    p "xxxx"
    p "It’s 9am now. Now what should I do with this giant rock?"

    menu:
        p "It’s 9am now. Now what should I do with this giant rock?"
        "Put the rock in the street":
            jump chapter3_street_missionSuccess
        "Don’t do it!":
            jump chapter3_street_missionFail



####################################################
label chapter3_cafe_prelude:

    scene bg cafe

    show protagonist neutral at t31
    p "This seems kinda ominous"
    p "You were the one who dropped that letter off, right?"
    p "Uhm..."

    show barista neutral at t33
    barista "Where did you get this? Do you realize what this did? I still don’t get how you even got a hold of this."
    barista "I don’t even know who you are really."

    p "Uhm... I uh..."

    barista "You know, I couldn’t work after that."
    barista "Do you know how hard it is to work in the place where you found out someone is cheating on you?"
    barista "Day in and day out being reminded of that."

    p "I don’t uh... suppose I would..."

    barista "It took quite a bit of confidence to come in today."
    barista "I don’t think you’d know that, dropping that letter off for someone else."

    p "Yeah uh I guess. I think that I’m gonna leave now."
    p "Probably not the best idea to eat."

    barista "Probably a good idea."
    hide barista

    p "Where should I go now?"
    hide protagonist

    menu:
        p "Where should I go now?"
        "Go to the Street":
            jump chapter3_street_decision
        "Go to the Office" (disabled=False) if flag_visited_office==0:
            $ flag_visited_office = 1;
            jump chapter3_office_prelude
        "Go to the Office" (disabled=True) if flag_visited_office==1:
            $ flag_visited_office = 1;
            jump chapter3_office_prelude
        "Go back Home" (disabled=False) if flag_visited_home==0:
            $ flag_visited_home = 1;
            jump chapter3_home_prelude
        "Go back Home" (disabled=True) if flag_visited_home==1:
            $ flag_visited_home = 1;
            jump chapter3_home_prelude
