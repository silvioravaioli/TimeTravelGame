####################################################
label start_chapter1:

    scene bg office
    n "{i}Just another day in the office..."

    show coworker talking at t33
    coworker "Hey newbie, the boss is mad at you. At least, I guess he was referring to you. You are the new idiot, right? {p}What is your name again?!?"
    show coworker neutral at s33

    show protagonist hmm at t31
    n "{i}This is me. I have just started this new job, but things are not going great..."
    n "{i}Nobody seems to remember my name."
    p "I am ..."

    $ protagonist_name = renpy.input("What is your name again?!?")
    $ protagonist_name = protagonist_name.strip()
    if protagonist_name == "":
        $ protagonist_name="Eli"
    show coworker talking at s33
    coworker "Right, [protagonist_name], the new idiot! Hurry up!"
    show coworker at thide
    hide coworker



    show protagonist talking at t31
    p "This is your coffee, Boss."
    show protagonist at s31

    show boss angry at t33
    show protagonist anxious
    boss "Why did it take you so long?"

    show protagonist at thide
    hide protagonist

    show boss coffee
    boss "This coffee..."
    show boss disgusted
    boss "THIS COFFEE IS DISGUSTING! {p}BLEAH!!!"
    show boss at s33

<<<<<<< HEAD
    show coworker neutral at t31
    coworker "Woah you really messed that up."
    show coworker at s31
=======
    show coworker talking at t31
    coworker "Woah you really messed that up"
    show coworker neutral at s31
>>>>>>> 69dad2aeddcf60dc949cb28ba73d6449c4954c51

    show boss angry at t33
    boss "[protagonist_name], out of my way!!!"
    show boss at s33


    show coworker laughing at t31
    coworker "I know it’s called bean water, but you don’t just directly put the beans in the water."
    coworker "HAHAHAHAHAHAHAHAHAHAHA"
    show coworker at thide
    hide coworker
    show boss at thide
    hide boss
    scene black with Dissolve(0.5)

####################################################
label chapter1_introdialogue0:

    scene bg home with Dissolve(0.5)
    show protagonist anxious at t11
    p "I'm finally home..."
    show protagonist at thide
    hide protagonist

####################################################
label chapter1_introdialogue1:

    show timegod neutral at t11
    g "Whoa you really messed that up! I see you’ve had a bad day."
    show timegod laugh at t11
    g "I have a proposition for you."
    show timegod creepy at t11
    g "Would you like a do over... {w}a chance to undo your mistakes?"
    #show timegod at thide
    hide timegod

    menu:
        g "Would you like a do over... a chance to undo your mistakes?"
        "Ummm... okay":
            show timegod neutral at t11
            g "I was sure you would have said so."
            jump chapter1_introdialogue2

        "What are you?":
            show timegod neutral at t11
            g "Interesting question. A rather rude one. But interesting."
            show timegod laugh at t11
            g "I will answer that question later (or maybe not)."
            g "But I think you should be more interested in what I can do for you."
            jump chapter1_introdialogue2

        "Haha nice costume. Please leave.":
            show timegod neutral at t11
            g "Interesting."
            show timegod laugh at t11
            g "Allow me to tell you some more..."
            jump chapter1_introdialogue2

        "No":
            show timegod neutral at t11
            g "Interesting answer."
            show timegod laugh at t11
            g "Allow me to tell you some more..."
            jump chapter1_introdialogue2


####################################################
label chapter1_introdialogue2:

    show timegod snap1 at t11
    g "The rules are simple. You go back and complete a task for me..."
    show timegod snap2 at t11
    g "...and in exchange you can fix your mistake!"
    $ timegod_name = "Time God"
    show timegod neutral at t11
    g "What would you say?"
    #show timegod at thide
    hide timegod

    menu:
        g "What would you say?"
        "What task?":
            show timegod creepy at t11
            g "Interesting question."
            jump chapter1_introdialogue3
        "Seriously, what are you?":
            show timegod angry at t11
            g "Interesting question."
            jump chapter1_introdialogue3


####################################################
label chapter1_introdialogue3:

    show timegod neutral at t11
    g "I simply need you to deliver this letter to the coffee shop across the street from your office."
    #show timegod at thide
    hide timegod

    menu:
        g "I simply need you to deliver this letter to the coffee shop across the street from your office."
        "Let me read it first.":
            n "{i}Letter reads: \"Loved the date last night -T\"{/i}"
            jump chapter1_introdialogue4
        "Okay, sure. I'll do it.":
            jump chapter1_introdialogue4


####################################################
label chapter1_introdialogue4:

    show timegod neutral at t11
    g "Fantastic. You will travel one week back in time."
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

    play music "timeTravelSound.mp3" fadeout 1
    scene black with Dissolve(1.0)
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

    scene bg cafeoutdoor with Dissolve(0.5)
    show protagonist neutral at t11
    p "I wish I had known how to brew coffee, maybe I should send my past self to deliver the letter instead of doing it myself."
    p "Where should I go now?"
    #show protagonist at thide
    hide protagonist

    menu:
        p "Where should I go now?"
        "Enter the cafe":
            scene black with Dissolve(0.5)
            jump chapter1_cafe_present2
        "Go to the office":
            scene black with Dissolve(0.5)
            jump chapter1_office



####################################################
label chapter1_cafe_present2:

    scene bg cafe with Dissolve(0.5)
    show protagonist neutral at t11
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
    show protagonist neutral at t31
    p "I am in a hurry, I will just leave this on the counter."

    show barista neutral at t33
    barista "What is...?"
    show barista shocked
    barista "What is...?"

    show protagonist at thide
    hide protagonist
    show barista at thide
    hide barista
    scene black with Dissolve(0.5)

    jump chapter1_end

####################################################
label chapter1_cafe_past2:

    # this is the only path that gives success in the personal mission
    $ mission1personal_success = 1   # SUCCEED PERSONAL MISSION

    scene bg cafeoutdoor with Dissolve(0.5)
    show pastprotagonist neutral at t11
    pp "This must be the Hourglass Cafe."
    pp "OK, who am I supposed to deliver this to?"
    pp "I guess I can simply leave it to anyone."
    show pastprotagonist at thide
    hide pastprotagonist
    scene black with Dissolve(0.5)

    scene bg cafe with Dissolve(0.5)
    show pastprotagonist talking at t11
    pp "The food smells really good."
    pp "I might as well get some lunch while I’m at it."

    jump chapter1_cafe_past3


####################################################
label chapter1_cafe_present3:

    show protagonist joy at t11
    p "Can I get an egg salad sandwich {w}with extra onions, {w}extra pickles, {w}and extra garlic?"
    show protagonist at t31

    show barista neutral at t33
    barista "Sure! Would you like to add a cup of coffee to that order? {w}Promotion week, only 25 cents extra."
    show barista at s33

    show protagonist talking at t31
    p "I'm not actually a coffee person. {w}But hey, sure, why not?"
    show protagonist at s31

    show barista at t33
    barista "Ok, egg salad sandwich with extra onions, extra pickles, extra garlic, and a cup of coffee coming right up!"
    show barista at thide
    hide barista

    n "{i}The barista stands in front of the coffee machine, and  brews the coffee quickly and with confidence."

    show protagonist hmm at t31
    p "So... that's how you make coffee. {w}Wish I knew that earlier."
    show protagonist at s31

    show barista neutral at t33
    barista "Oh, where'd this letter come from?"
    show barista shocked
    barista "Oh, where'd this letter come from?"
    show protagonist at thide
    hide protagonist
    barista "Oh, where'd this letter come from?"
    show barista at thide
    hide barista

    scene black with Dissolve(0.5)
    jump chapter1_end


####################################################
label chapter1_cafe_past3:

    show pastprotagonist joy at t11
    pp "Can I get an egg salad sandwich {w}with extra onions, {w}extra pickles, {w}and extra garlic?"
    show pastprotagonist at t31

    show barista neutral at t33
    barista "Sure! Would you like to add a cup of coffee to that order? {w}Promotion week, only 25 cents extra."
    show barista at s33

    show pastprotagonist talking at t31
    pp "I'm not actually a coffee person. {w}But hey, sure, why not?"
    show pastprotagonist at s31

    show barista at t33
    barista "Ok, egg salad sandwich with extra onions, extra pickles, extra garlic, and a cup of coffee coming right up!"
    show barista at thide
    hide barista

    n "{i}The barista stands in front of the coffee machine, and  brews the coffee quickly and with confidence."

    show pastprotagonist hmm at t31
    pp "So... that's how you make coffee. {w}Wish I knew that earlier."
    show pastprotagonist at s31

    show barista neutral at t33
    barista "Oh, where'd this letter come from?"
    show barista shocked
    barista "Oh, where'd this letter come from?"
    show pastprotagonist at thide
    hide pastprotagonist
    barista "Oh, where'd this letter come from?"
    show barista at thide
    hide barista

    show protagonist neutral at t11
    p "Oh, looks like I'm leaving. Better go so that I don't run into myself."

    scene black with Dissolve(0.5)
    jump chapter1_end



####################################################
label chapter1_office:

    scene bg office with Dissolve(0.5)
    show protagonist anxious at t11
    p "My desk is empty. Looks like he- or I am still on my bathroom break."

    show protagonist hmm
    p "Here’s what I'll do... {w}Write a delivery message on this letter and put it on my desk"

    #show protagonist excited
    hide protagonist
    n "{i}The letter is now folded up nicely, with a post-it note on top that reads"
    n "{i}\"URGENT: Deliver to Hourglass Cafe\" followed by the address"
    n "{i}You hear the sound of the toilet flushing..."

    show protagonist surprised at t11
    p "HIDE!"
    show protagonist at thide
    hide protagonist
    p "Better hide behind this potted plant"

    show pastprotagonist anxious at t11
    pp "What is this???"
    show pastprotagonist despair
    pp "Hm... Maybe it's from the boss. {p}Guess I'll drop it off."
    hide pastprotagonist

    menu:
        p "What should I do now?"

        "Follow the past self to the cafe":
            show protagonist hmm at t11
            p "Ok I need to see this through."
            show protagonist at thide
            hide protagonist
            scene black with Dissolve(0.5)
            jump chapter1_cafe_past2

        "Return to the present":
            show timegod laugh at t11
            g "Nice try. Your job isn't finished yet."
            hide timegod
            menu:
                p "What should I do now?"
                "Follow the past self to the cafe":
                    scene black with Dissolve(0.5)
                    jump chapter1_cafe_past2
                "Return to the present" (disabled=True):
                    show timegod laugh at t11






####################################################
label chapter1_home:
    scene bg home with Dissolve(0.5)

    show protagonist hmm at t11
    p "What just happened?"

    show protagonist surprised
    p "I am in the same place... but it is also different..."

    show protagonist hmm
    p "I was supposed to do something, but what?"
    p "My memory is foggy, maybe I should just take a nap."
    hide protagonist

    menu:
        p "What should I do?"
        "Go to the Cafe":
            scene black with Dissolve(0.5)
            jump chapter1_cafe_outdoor
        "Go to the Office":
            scene black with Dissolve(0.5)
            jump chapter1_office
        "Stay Home and take a nap":
            scene black with Dissolve(0.5)
            jump chapter1_restartmission



####################################################
label chapter1_restartmission:

    scene bg home with Dissolve(0.5)
    show timegod neutral at t11
    g "This is no time to nap!"
    show timegod angry at t11
    g "Have you already forgotten your mission???"
    hide timegod

    menu:
        g "Have you already forgotten your mission???"
        "Go to the Cafe":
            scene black with Dissolve(0.5)
            jump chapter1_cafe_outdoor
        "Go to the Office":
            scene black with Dissolve(0.5)
            jump chapter1_office
        "Stay Home and take a nap" (disabled=True):
            jump chapter1_restartmission






####################################################
label chapter1_end:

    scene bg home with Dissolve(0.5)

    show timegod neutral at t11
    g "So... how do you think it went?"
    hide timegod

    menu:
        g "So... how do you think it went?"
        "Not great":
            show timegod neutral at t11
            g "Hmm... You’ll get better next time!"
            show timegod snap1 at t11
            g "Hmm... You’ll get better next time!"
            show timegod snap2 at t11
            g "Hmm... You’ll get better next time!"

            scene black with Dissolve(0.5)
            n "{i}The Time God snaps their fingers and sends you back to the present.{\i}"
            scene bg home with Dissolve(0.5)
        "Went ok.":
            show timegod neutral at t11
            g "Good. Now you know what to expect next time!"
            show timegod snap1 at t11
            g "Good. Now you know what to expect next time!"
            show timegod snap2 at t11
            g "Good. Now you know what to expect next time!"

            scene black with Dissolve(0.5)
            n "{i}The Time God snaps their fingers and sends you back to the present.{\i}"
            scene bg home with Dissolve(0.5)

    show protagonist anxious at t31
    p "So... what happened when I was gone?"
    show protagonist at s31
    show timegod creepy at t33
    g "Interesting question. Guess you’ll have to find out..."
    show timegod at thide
    hide timegod
    show protagonist at thide
    hide protagonist

    scene black with Dissolve(0.5)
    n "The day after, in the office..."
    scene bg office with Dissolve(0.5)

    show boss neutral at t33
    boss "I need you to file these documents, and sign these things for me."
    show boss talking at t33
    boss "Also I need those progress reports done by the end of the day."
    show boss neutral at t33
    boss "Oh, and fix those UGLY bar charts! Who pairs neon green with hot pink?"
    show boss at s33

    show protagonist talking at t31
    p "Ok, anything else?"
    show protagonist neutral at s31

    show boss talking at t33
    boss "Oh, yeah. {w}Make me a cup of coffee."
    show boss at s33

    show protagonist anxious at t31
    p "You want ME to make you a cup of coffee?"
    show protagonist at s31

    if mission1personal_success==1:
        jump chapter1_end_success
    else:
        jump chapter1_end_failure


####################################################
label chapter1_end_success:
    show boss at t33
    boss "Yeah, a cup of coffee."
    show boss at s33

    show protagonist hmm at t31
    p "ME?????"
    show protagonist at s31

    show boss angry at t33
    boss "Yes. That’s what I SAID."
    show protagonist joy
    boss "And be fast, I need to run to the next meeting."
    show boss at thide
    hide boss

    show protagonist woohoo at t11
    p "It worked!"
    show protagonist at thide
    hide protagonist

    scene black with Dissolve(1.0)
    n "END OF MISSION 1"
    n "  "
    jump start_chapter2
    #return


####################################################
label chapter1_end_failure:
    show boss angry at t33
    boss "OF COURSE NOT!"
    show protagonist surprised
    boss "Actually after yesterday, you are banned from making coffee."
    show boss at s33

    n "He is not joking. Above the coffee machine, there’s a huge printout with my face and a stop sign over it."

    show boss disgusted at t33
    boss "Bean water. My god..."
    show boss at thide
    hide boss
    show protagonist at thide
    hide protagonist

    scene black with Dissolve(1.0)
    n "END OF MISSION 1"
    n "  "
    jump start_chapter2
    #return
