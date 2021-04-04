####################################################
label start_chapter1:
    # play music "funiculifunicula.mp3" fadeout 1       # ADD MUSIC

    # TODO Location - (Home, intention was to use this as a hub in between levels):
    # TODO Open the door, first thing you see is the time god
    $ mission1personal_success = 0   # DEFAULT: FAIL PERSONAL MISSION


    scene bg office

    show protagonist neutral zorder 2 at t31
    p "This is your coffee, Boss."
    show protagonist at s31

    show boss neutral zorder 2 at t33
    boss "Why did it take you so long?"

    show protagonist zorder 1 at thide
    hide protagonist

    boss "---THE BOSS MAKES FUNNY FACES---"
    show boss at s33

    show coworker neutral zorder 2 at t31
    coworker "Woah you really messed that up"
    show coworker at s31

    # [See angry boss spitting out coffee]
    show boss neutral zorder 2 at t33
    boss "DISGUSTING!!!"
    show boss at s33


    show coworker neutral zorder 2 at t31
    coworker "I know it’s called bean water, but you don’t just directly put the beans in the water."
    coworker "HAHAHAHAHAHAHAHAHAHAHA"
    show coworker zorder 1 at thide
    hide coworker
    show boss zorder 1 at thide
    hide boss

####################################################
label chapter1_introdialogue0:

    scene bg home
    show protagonist neutral zorder 2 at t11
    p "I'm finally home..."
    show protagonist zorder 1 at thide
    hide protagonist

####################################################
label chapter1_introdialogue1:

    show timegod neutral zorder 2 at t11
    g "Whoa you really messed that up! I see you’ve had a bad day."
    show timegod laugh zorder 2 at t11
    g "I have a proposition for you."
    show timegod creepy zorder 2 at t11
    g "Would you like a do over...a chance to undo your mistakes?"
    #show timegod zorder 1 at thide
    hide timegod

    menu:
        g "Would you like a do over...a chance to undo your mistakes?"
        "Ummm... okay":
            show timegod neutral zorder 2 at t11
            g "I was sure you would have said so."
            jump chapter1_introdialogue2

        "What are you?":
            show timegod neutral zorder 2 at t11
            g "Interesting question. A rather rude one. But interesting."
            show timegod laugh zorder 2 at t11
            g "I will answer that question later (or maybe not)."
            g "But I think you should be more interested in what I can do for you."
            jump chapter1_introdialogue2

        "Haha nice costume. Please leave.":
            show timegod neutral zorder 2 at t11
            g "Interesting."
            show timegod laugh zorder 2 at t11
            g "Allow me to tell you something more..."
            jump chapter1_introdialogue2

        "No":
            show timegod neutral zorder 2 at t11
            g "Interesting answer."
            show timegod laugh zorder 2 at t11
            g "Allow me to tell you something more..."
            jump chapter1_introdialogue2


####################################################
label chapter1_introdialogue2:

    show timegod snap1 zorder 2 at t11
    g "The rules are simple. You go back and complete a task for me..."
    show timegod snap2 zorder 2 at t11
    g "...and in exchange you can fix your mistake!"
    $ timegod_name = "Time God"
    show timegod neutral zorder 2 at t11
    g "What would you say?"
    #show timegod zorder 1 at thide
    hide timegod

    menu:
        g "What would you say?"
        "What task?":
            show timegod creepy zorder 2 at t11
            g "Interesting question."
            jump chapter1_introdialogue3
        "Seriously, what are you?":
            show timegod angry zorder 2 at t11
            g "Interesting question."
            jump chapter1_introdialogue3


####################################################
label chapter1_introdialogue3:

    show timegod neutral zorder 2 at t11
    g "I simply need you to deliver this letter to the coffee shop across the street from your office."
    #show timegod zorder 1 at thide
    hide timegod

    menu:
        g "Interesting question. I simply need you to deliver this letter to the coffee shop across the street from your office."
        "Let me read it first.":
            n "{i}Letter reads: \"Loved the date last night -T\"{/i}"
            jump chapter1_introdialogue4
        "Okay, sure. I'll do it.":
            jump chapter1_introdialogue4


####################################################
label chapter1_introdialogue4:

    show timegod neutral zorder 2 at t11
    g "Fantastic. You will travel one week back in time."
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
    n "{i}The Time God snaps his fingers and you’re transported to one week into the past.{\i}"

    # TODO "1 week ago" fades in and out at corner of screen
    # TODO MAP to choose where to go

    p "So...where should I go now?"

    menu:
        p "So...where should I go now?"
        "Cafe":
            jump chapter1_cafe_outdoor
        "Office":
            jump chapter1_office
        "Home":
            jump chapter1_home








####################################################
label chapter1_cafe_outdoor:

    scene bg cafeoutdoor
    show protagonist neutral zorder 2 at t11
    p "I wish I had known how to brew coffee, maybe I should send my past self to deliver the letter instead of doing it myself."
    n "Where should I go now?"
    #show protagonist zorder 1 at thide
    hide protagonist

    menu:
        n "Where should I go now?"
        "Enter the cafe":
            jump chapter1_cafe_present2
        "Go to the office":
            jump chapter1_office



####################################################
label chapter1_cafe_present2:

    scene bg cafe
    show protagonist neutral zorder 2 at t11
    p "This is the place, the food smells really good."
    p "It should be enough if I leave the letter on the counter, but I am getting hungry now!"
    hide protagonist

    menu:
        "Leave the letter on the counter and leave":
            jump chapter1_cafe_table
        "Might as well get some lunch":
            jump chapter1_cafe_present3

####################################################
label chapter1_cafe_table:

    scene bg cafe
    show protagonist neutral zorder 2 at t33
    p "I am in a hurry, I will just leave this on the counter."

    show barista neutral zorder 2 at t31
    barista "What is...?"
    show barista shocked
    barista "What is...?"

    show protagonist zorder 1 at thide
    hide protagonist
    show barista zorder 1 at thide
    hide barista

    jump chapter1_end

####################################################
label chapter1_cafe_past2:

    # this is the only path that gives success in the personal mission
    $ mission1personal_success = 1   # SUCCEED PERSONAL MISSION

    scene bg cafeoutdoor
    show pastprotagonist neutral zorder 2 at t11
    p "This must be the Hourglass Cafe."
    p "OK, who am I supposed to deliver this to?"
    p "I guess I can simply leave it to anyone."
    show pastprotagonist zorder 1 at thide
    hide pastprotagonist

    scene bg cafe
    show pastprotagonist neutral zorder 2 at t11
    p "The food smells really good."
    p "I might as well get some lunch while I’m at it."

    jump chapter1_cafe_past3


####################################################
label chapter1_cafe_present3:

    show protagonist neutral zorder 2 at t11
    p "Can I get an egg salad sandwich with extra onions, extra pickles, extra garlic?"
    show protagonist at s33

    show barista neutral zorder 2 at t31
    barista "Sure! Would you like to add a cup of coffee to that order? Promotion week, only 25 cents extra"
    show barista at s31

    show protagonist at t33
    p "I'm not actually a coffee person. But hey, sure, why not?"
    show protagonist at s33

    show barista at t31
    barista "Ok, egg salad sandwich with extra onions, extra pickles, extra garlic, and a cup of coffee coming right up!"
    show barista at s31

    n "The barista stands in front of the coffee machine, and  brews the coffee quickly and with confidence."
    # TODO SHOW [Barista is now standing in front of coffee machine]

    show protagonist at t33
    p "So...that's how you make coffee. Wish I knew that earlier."
    show protagonist at s33

    show barista at t31
    barista "Oh, where'd this letter come from?"
    show barista shocked
    barista "Oh, where'd this letter come from?"
    show barista zorder 1 at thide
    hide barista
    show protagonist zorder 1 at thide
    hide protagonist

    jump chapter1_end



####################################################
label chapter1_cafe_past3:

    show pastprotagonist neutral zorder 2 at t11
    pp "Can I get an egg salad sandwich with extra onions, extra pickles, extra garlic?"
    show pastprotagonist at s33

    show barista neutral zorder 2 at t31
    barista "Sure! Would you like to add a cup of coffee to that order? Promotion week, only 25 cents extra"
    show barista at s31

    show pastprotagonist at t33
    pp "I'm not actually a coffee person. But hey, sure, why not?"
    show pastprotagonist at s33

    show barista at t31
    barista "Ok, egg salad sandwich with extra onions, extra pickles, extra garlic, and a cup of coffee coming right up!"
    show barista at s31

    n "The barista stands in front of the coffee machine, and  brews the coffee quickly and with confidence."
    # TODO SHOW [Barista is now standing in front of coffee machine]

    show pastprotagonist at t33
    pp "So...that's how you make coffee. I never really paid attention to it."
    show pastprotagonist at s33

    show barista at t31
    barista "Oh where'd this letter come from?"
    # TODO Barista makes a face
    barista "LEAVE."
    barista "LEAVE. NOW!"
    show barista zorder 1 at thide
    hide barista
    show pastprotagonist zorder 1 at thide
    hide pastprotagonist

    jump chapter1_end



####################################################
label chapter1_office:

    scene bg office
    show protagonist neutral zorder 2 at t11
    p "My desk is empty. Looks like he- or I am still on my bathroom break."
    p "Here’s what I'll do...write a delivery message on this letter and put it on my desk"
    n "(Holding letter and pencil)"
    n "Letter is now folded up nicely, with a post-it note on top that reads"
    n "\"URGENT: Deliver to Hourglass Cafe\" followed by the address"
    n "(Toilet flushes)"
    p "HIDE!"
    show protagonist zorder 1 at thide
    hide protagonist

    n "(moves behind potted plant)"

    show pastprotagonist neutral zorder 2 at t11
    pp "What is this???"
    # TODO past self confused
    pp "Hm...maybe it's from the boss. Guess I'll drop it off."
    hide pastprotagonist

    menu:
        p "What should I do now?"

        "Follow the past self to the cafe":
            show protagonist neutral zorder 2 at t11
            p "Ok I need to see this through."
            show protagonist zorder 1 at thide
            hide protagonist
            jump chapter1_cafe_past2

        "Return to the present":
            show timegod laugh zorder 2 at t11
            g "Nice try. Your job isn't finished yet."
            g "You should make sure the mission is completed before you can come back!"
            show timegod snap1 zorder 2 at t11
            g "You should make sure the mission is completed before you can come back!"
            show timegod snap2 zorder 2 at t11

            scene black
            n "The Time God snaps fingers and sends you back to the past"
            jump chapter1_cafe_past2





####################################################
label chapter1_home:
    scene bg home

    show protagonist neutral zorder 2 at t11
    p "What just happened?"
    p "I am in the same place... but it is also different..."
    p "I was supposed to do something, but what?"
    p "My memory is foggy, maybe I should just take a nap."
    hide protagonist

    menu:
        p "What should I do?"
        "Go to the Cafe":
            jump chapter1_cafe_outdoor
        "Go to the Office":
            jump chapter1_office
        "Stay Home and take a nap":
            jump chapter1_restartmission



####################################################
label chapter1_restartmission:

    show timegod neutral zorder 2 at t11
    g "This is no time to nap!"
    show timegod angry zorder 2 at t11
    g "Have you already forgotten your mission???"
    jump chapter1_introdialogue3






####################################################
label chapter1_end:
    scene black
    n "The mission is completed, and the mysterious Time God disappeared."
    n "The day after, in the Office..."

    scene bg office
    show boss neutral zorder 2 at t11
    boss "I need you to file these documents, and sign these things for me."
    boss "Also I need those progress reports done by the end of the day."
    boss "Oh, and fix those UGLY bar charts! Who pairs neon green with hot pink?"
    show boss at s31

    show protagonist neutral zorder 2 at t33
    boss "Ok, anything else?"
    show protagonist at s33

    show boss at t31
    boss "Oh, yeah. Make me a cup of coffee"
    show boss at s31

    show protagonist at t33
    p "You want me to make you a cup of coffee?"
    show protagonist at s33

    if mission1personal_success==1:
        jump chapter1_end_success
    else:
        jump chapter1_end_failure


####################################################
label chapter1_end_success:
    show boss at t31
    boss "Yeah, cup of coffee."
    show boss at s31

    show protagonist at t33
    #show protagonist incredulous
    p "Me???"
    show protagonist at s33

    show boss at t31
    #show boss irritated
    boss "Yes. That’s what I SAID."
    boss "And be fast, I need to run to the next meeting."
    show boss zorder 1 at thide
    hide boss

    show protagonist at t11
    p "It worked! (whispered/italics)"
    show protagonist zorder 1 at thide
    hide protagonist

    scene black
    n "END OF CHAPTER 1"
    return


####################################################
label chapter1_end_failure:
    show boss at t31
    boss "OF COURSE NOT!"
    #show boss pointingAtCoffeeStation
    boss "Actually after yesterday, you are banned from making coffee."
    show boss at s31

    show protagonist at t33
    #show protagonist incredulous
    p "Me???"
    show protagonist at s33

    #scene bg coffeeMachineBanned
    n "Pan to coffee machine, there’s a huge printout sign with the protagonist’s face on it and a huge prohibited sign over it"

    show boss at t31
    #show boss irritated
    boss "Bean water. My god..."
    show boss zorder 1 at thide
    hide boss
    show protagonist zorder 1 at thide
    hide protagonist

    scene black
    n "END OF CHAPTER 1"
    return
