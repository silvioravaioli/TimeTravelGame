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

    show protagonist neutral at t11
    p "Is there anything I can do to fix this?"
    show protagonist neutral
    p "If only I could travel back again."
    show protagonist neutral

    g "I have a mission for you."

    p "Wonderful. Send me back now. I need to go back. I’ll do whatever, please just send me back."

    g "Interesting. Very interesting."
    g "You have been performing quite satisfactorily. It is time to entrust you with a more important task."
    g "Although important, this task is not particularly difficult."
    g "You must simply place a certain object at a specific place at a particular time."
    g "However, being off by even a minute could have disastrous consequences."
    g "If you fail in this mission, I will never appear before you again."
    g "On the other hand, success will yield great rewards."
    g "If you achieve this goal, you will have the opportunity to fix any mistake of your choosing."
    g "Name a time, and I will send you there."
    g "Are you ready to accept this responsibility?"
    hide protagonist
    hide timegod

    menu:
        g "Are you ready to accept this responsibility?"
        "Yes. Yes, please send me back now":
            show protagonist anxious at t11
        "I am ready":
            show protagonist anxious at t11
        "I need to think about it":
            show protagonist anxious at t11


    g "Interesting answer. No time to waste!"
    n "holding rock"
    g "Go to the intersection of Kronos Avenue with Fate Street."
    p "There will be a pile of rocks at a construction site on the southeast corner."
    p "Select the largest one."
    p "You must place this stone exactly 47 inches to the east of the red bench on the median."
    p "It must be placed at exactly 9:00 am."
    p "Both the location and time are vitally important."
    p "A second later or an inch further, and your efforts will result in failure."
    p "Remember carefully: 9:00 am on the dot. 47 inches to the east of the red bench."
    p "I wish you luck in your endeavour."


    scene black with Dissolve(1.0)
    p "Time God snaps fingers and you’re transported to 7:30 am in the morning"


    p "I just need to do this task."
    p "Then I can save my boss and my coworkers as well."
    p "I have another chance. Let’s do this."
    p "OK it looks like it’s 7:30 am."
    p "I have to put the rock down at 9 exactly."
    p "Maybe I should head there early just to be safe?"

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
    p "xxxx"
    p "xxxx"
    p "xxxx"
    p "xxxx"
    p "xxxx"
    p "xxxx"



####################################################
label chapter3_street_decision:

    scene bg home

    show protagonist neutral at t11
    p "xxxx"
    p "xxxx"
    p "xxxx"
    p "xxxx"
    p "xxxx"
    p "xxxx"


####################################################
label chapter3_cafe_prelude:

    scene bg home

    show protagonist neutral at t11
    p "xxxx"
    p "xxxx"
    p "xxxx"
    p "xxxx"
    p "xxxx"
    p "xxxx"


####################################################
label chapter3_office_prelude:

    scene bg home

    show protagonist neutral at t11
    p "xxxx"
    p "xxxx"
    p "xxxx"
    p "xxxx"
    p "xxxx"
    p "xxxx"


####################################################
label chapter3_home_prelude:

    scene bg home

    show protagonist neutral at t11
    p "xxxx"
    p "xxxx"
    p "xxxx"
    p "xxxx"
    p "xxxx"
    p "xxxx"
