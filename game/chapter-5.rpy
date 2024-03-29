####################################################
label start_chapter5:

    # CHOOSE THE ENDING
    if testing_mode:
        menu:
            n "Which ending do you want to test?"
            "Final mission success":
                jump epilogue_finalMissionSuccess
            "Final mission failure":
                jump epilogue_finalMissionFailure

    # ENDING FROM THE STORY
    if not testing_mode:
        if mission4timegod_success == 1:
            jump epilogue_finalMissionSuccess
        else:
            jump epilogue_finalMissionFailure




####################################################
label epilogue_finalMissionSuccess:

    scene black with Dissolve(0.5)
    n "One month later"
    scene bg home with Dissolve(0.5)
    n "{i}It has been a tough month. It all started with the funeral of the boss."
    n "{i}Then the situation at work started collapsing. Last week, you had to pack your stuff and leave the office, {w}forever."
    n "{i}Even basic things like waking up in the morning seem impossible."

    show protagonist anxious at t11
    p "I... I’m going crazy at home by myself!"
    p "The house is a mess, I am a mess!"
    p "I should start looking for a job again..."
    show protagonist at thide
    hide protagonist

    n "{i}While you scroll idly the news, something catches your attention."
    n "{i}You click on an ad, and you are on the website of your old rival company. Can you have a second chance there?"
    n "{i}In a flawless movement of the mouse, you click on the Apply Now button..."

    jump epilogue_finalMissionSuccess_jobSearch


####################################################
label epilogue_finalMissionSuccess_jobSearch:

    scene black with Dissolve(0.5)
    n "Two weeks later"
    scene bg home with Dissolve(0.5)

    #n "Background: bulletin board, contains 1 picture of the time god somewhere on the board, the mission of the rival company is displayed somewhere"

    show protagonist neutral at t11
    p "First day of work! I need to make a good impression..."
    p "What if my boss is mean?"
    show protagonist anxious
    p "What if my coworkers hate me?"
    p "Oh dear. I better not mess up."
    p "Ok, I better get ready to meet my new boss."
    show protagonist at thide
    hide protagonist

    scene black with Dissolve(0.5)
    scene bg office_timegod with Dissolve(0.5)

    show timegod neutral at t33
    g "Oh, hello!"
    show protagonist surprised at s31
    g "You must be [protagonist_name], our new employee!"
    show timegod at s33

    show protagonist at t31
    p "You... You..."
    show protagonist hey
    p "You screwed up my life! What are you DOING here?!"
    show protagonist at s31

    show timegod laugh at t33
    $ timegod_name = "Tim (your new Boss)"
    g "Oh, [protagonist_name]. You must be mistaken! I’m Tim. You’ll be working under me here."
    show timegod at s33

    show protagonist surprised at t31
    p "I’ll be WHAT?"
    p "You’re my BOSS?"
    show protagonist at thide
    hide protagonist

    show timegod happy at t33
    g "Anyway, let’s get started. First of all, I want to warmly welcome you to the team."
    show timegod happy at t11
    g "Here at TG Home Insurance, we think of our employees and our clients as one big family."
    g "Above all, we value providing the very best standard of service to our customers"
    g "In reflection of this attitude, our mission is {p}‘‘taking care of what’s important.’’"
    g "Now that we’ve got the orientation spiel covered..."
    show timegod snap1
    g "Let’s get to work!"
    show timegod snap2

    scene black with Dissolve(1.0)
    n "ENDING 1 OUT OF 3 {p}You can change your choices to discover other endings."
    return




####################################################
label epilogue_finalMissionFailure:

    scene bg office

    show boss neutral at t33
    boss "Hey! [protagonist_name]! Get over here!"
    show boss at s33

    show protagonist anxious at t31
    p "Oh... Hi boss..."
    show protagonist surprised
    p "Wait! You’re alive???"
    show protagonist anxious
    p "I- I mean, how are you feeling?"
    show protagonist joy

    show boss happy at t33
    boss "Really good actually! They checked me up at the ER and turns out I just had some bad food poisoning"
    show boss talking
    boss "Oh man, I spent the night on the toilet. But now, I’m good as new!"
    boss "And, you know. Even though I was spewing stuff from both ends..."
    show boss talking_happy
    boss "By GOD, that was the BEST burger I’ve EVER had!"
    show boss at s33

    show protagonist blush at t31
    p "Really? You liked my burgers that much?"
    show protagonist at s31

    show boss happy at t33
    boss "Oh, absolutely! Worth the diarrhea."
    show boss neutral at s33


    # CHOOSE THE ENDING
    if testing_mode:
        hide boss
        hide protagonist
        menu:
            n "Which ending do you want to test?"
            "High Reputation":
                jump epilogue_finalMissionFail_highRep
            "Low Reputation":
                jump epilogue_finalMissionFail_lowRep

    # ENDING FROM THE STORY
    if not testing_mode:
        if (mission1personal_success + mission2personal_success + mission3personal_success) == 0:
            jump epilogue_finalMissionFail_lowRep
        else:
            jump epilogue_finalMissionFail_highRep




####################################################
label epilogue_finalMissionFail_highRep:

    show protagonist neutral at s31

    show boss neutral at t33
    boss "On the topic of great things, the work you’ve done these past few weeks has been incredible."
    boss "I’ve really been admiring all the great work you’ve done, {p}and I believe it deserves some attention."

    # IF MISSION 1 SUCCESS
    if mission1personal_success == 0:
        show boss neutral at t33
        boss "Bang-up job with the coffee."
        show boss at s33
        show protagonist talking at t31
        p "Yeah, that’s me! {w}I’m pretty good at stuff."
        show protagonist at s31

    # IF MISSION 2 SUCCESS
    if mission2personal_success == 0:
        show boss talking at t33
        boss "Absolutely nailed that meeting as well. {p}Made me proud to work in home insurance."
        show boss at s33
        show protagonist joy at t31
        p "I know how to be professional when we have important clients!"
        show protagonist at s31

    # IF MISSION 3 SUCCESS
    if mission3personal_success == 0:
        show boss happy at t33
        boss "You took good care of Princess."
        show dog cool at t11
        boss "I trust you will take care of our company with the same level of attention."
        show boss at s33
        show protagonist talking at t31
        p "I never lose sight of what is important."
        show protagonist at s31
        show dog at thide
        hide dog

    show boss neutral at t33
    boss "So, I’d like to offer you a promotion to my assistant. {p}You’ll get all the great bits and bobs: {w}experience, {w}more time in the office, {w}and a slightly higher salary!"
    show boss at s33

    show protagonist joy at t31
    p "Oh boy, that’s pretty swell."
    show protagonist at s31

    show boss neutral at t33
    boss "Don’t use up all your enthusiasm!"
    show protagonist neutral
    boss "Don’t use up all your enthusiasm! {w}I’ve got a first job for ya now that you’re in the big leagues, great time to prove yourself again."
    show boss happy
    boss "As you know, we’ve got quite a bit of rivals, not just a bit, they number us pretty heavily."
    boss "I’m going to need you to give me a full profile of each of these."
    show boss talking
    boss "There’s no page requirement, but just make sure you include all the basics."
    boss "There’s around 40 companies in the area, {p}but I heard the Internet will be pretty good for this one."
    show boss at s33

    show protagonist anxious at t31
    p "Uhh... You want me to compile a report about 40 different companies... {w}All on my own? {w}Doesn’t that seem to be..."
    show protagonist at s31

    show boss talking_happy at t33
    boss "Don’t worry, you’ve been doing pretty good with this stuff. {p}So much so, that I think you can get it done by next week."
    show protagonist surprised at t31
    p "NEXT WEEK?!"
    boss "I'll leave you to it!"
    show boss at thide

    hide boss
    show protagonist at thide
    hide protagonist

    scene black with Dissolve(0.5)
    n "Two weeks later"
    scene bg office_dark with Dissolve(0.5)
    #n "Jump to office at night (or just an indication it’s later, art team discretion)"
    #n "Two options for this, up to art team: Either a montage of the Protagonist in various positions in the office (same scene)"
    #n "or could just show a slumped version of him over a computer looking tired, disheveled"

    show protagonist despair at t11
    p "Oh dear... How long have I been sitting in front of this computer?"
    show protagonist surprised at t11
    p "What?! It's already 11pm!"
    show protagonist despair at t11
    p "And I still have so much more to get done... {w}So much for a 9 to 5 job..."
    p "Went from making coffee and burgers to this garbage every night. {w}Oh jeez..."
    p "I'm so tired..."
    n "{i}Something on the corner of the screen catches your attention. {w}It is an ad for the rival company.{w} You click it without even thinking why you are doing that."
    p "Guess I'll start looking at rival company number 27..."
    show protagonist hmm at t11
    p "Hm... Motto, \"taking care of what's important...\""
    show protagonist surprised at t11
    p "Oh my god!! Wait a minute!"
    show protagonist at thide
    hide protagonist

    scene black with Dissolve(0.5)
    scene bg ending2_image1 with Dissolve(0.5)
    n "{i}You see a picture of the best representatives for the rival company, and one of them looks a little familiar..."
    scene bg ending2_image2 with Dissolve(0.5)
    n "{i}You got your second chance."
    scene bg ending2_image3 with Dissolve(0.5)
    n "{i}You got your second chance. You fixed your mistakes. {p}This is what you always wanted{w}, right?"

    scene black with Dissolve(1.0)
    n "ENDING 2 OUT OF 3 {p}You can change your choices to discover other endings."
    return



####################################################
label epilogue_finalMissionFail_lowRep:

    show protagonist neutral at s31

    show boss neutral at t33
    boss "On the topic of great things, the work you’ve done these past few weeks has been incredible."
    boss "This month’s promotion is going to [coworker_name]"
    show protagonist despair
    show boss talking_happy
    boss "But keep up the good work and you might just get lucky next time."
    show boss at s33

    show protagonist anxious at t31
    p "You don’t think I’ve just been a huge doofus? {w}The coffee... {w}and the costume... {w}not to mention the burger incident!"
    show protagonist anxious at s31

    show boss neutral at t33
    boss "Everyone makes these kinds of mistakes."
    show boss facepalm
    boss "My first week on the job, I accidentally left the thermostat on -70 degrees instead of 70 degrees."
    show boss talking_happy
    boss "We had to use ice skates to get around the office for an entire month."
    show boss happy
    boss "But at least that’s one mistake I’ll never make again. With time, you’ll make more mistakes and learn from them as well."
    show boss talking
    boss "In a few years, you may even be running this place."
    show boss at s33

    show protagonist joy at t31
    p "I won’t let you down! Is there anything I can do to prove myself?"
    show protagonist at s31

    show boss talking at t33
    boss "Actually..."
    show boss at s33


    show coworker2 neutral at t11
    n "{i}A new coworker stumbles into office, {w}she trips over nothing, and just barely catches herself."
    show protagonist blush

    show coworker2 happy_right at t11
    coworker2 "Hello boss. It’s nice to finally meet you in person!"
    show coworker2 neutral_right at s11

    show boss happy at t33
    boss "Welcome to the company, [new_coworker_name]. You have impeccable timing, that will take you far."
    boss "I was just about to ask [protagonist_name] here if he would be willing to show you around."
    show boss at thide
    hide boss
    show coworker2 neutral at t33

    show protagonist talking at t31
    p "Nice to meet you, [new_coworker_name]. It’d be a pleasure to show off our exquisite linoleum flooring."
    show protagonist neutral at s31

    n "{i}As you are leaving the office, you pass the old Star Wars day poster."

    show coworker2 excited at t33
    coworker2 "OH SHOOT! YOU GUYS HAD STAR WARS DAY!"
    show coworker2 at s33

    show protagonist talking at t31
    p "Are you a Star Wars fan?"
    show protagonist neutral at s31

    show coworker2 happy at t33
    coworker2 "Am I?! HECK YEAH!!! If only I joined this company earlier you would have seen my sweet homemade Wookiee costume."
    show coworker2 excited at s33

    show protagonist joy at t31
    p "Well good thing you weren’t here, because there’s no way you could have held a candle to mine."
    p "I even used Wookiee-scented paint to make the outfit truly authentic."
    show protagonist neutral at s31

    show coworker2 hmm at t33
    coworker2 "What’s even the point of a Wookiee costume without Wookiee-scented paint? {p}At that point it’s just a bigfoot costume."
    show coworker2 neutral at s33

    show protagonist talking at t31
    p "I know, right?"
    show protagonist neutral at s31

    show coworker2 happy at t33
    coworker2 "By the way, is there a place to get coffee around here?"
    show coworker2 neutral at s33

    show protagonist talking at t31
    p "Yeah, there’s a coffee machine right by the conference room."
    show protagonist neutral at s31

    show coworker2 hmm at t33
    coworker2 "Umm..."
    coworker2 "This is pretty awkward, but I don’t actually know how to use a coffee machine. I’ve always gotten my coffee at Starbucks."
    coworker2 "Would you mind showing me how to use it?"
    show coworker2 neutral at s33

    show protagonist anxious at t31
    p "Umm..."
    p "To be honest, I don’t know either. I don’t really drink coffee very often so I didn’t think I’d need to learn."
    p "You know what? There’s a pretty good cafe a few blocks from here."
    p "How about we take a short break and grab some coffee there. It’ll be my treat."
    show protagonist neutral at s31

    show coworker2 happy at t33
    coworker2 "I’m down. Show the way!"
    show coworker2 neutral at s33

    show coworker2 at thide
    hide coworker2
    show protagonist at thide
    hide protagonist
    scene black with Dissolve(0.5)
    scene bg office_grill with Dissolve(0.5)

    n "{i}It is a beautiful day, and you do not mind so much the fact you did not get the promotion you wanted."
    n "{i}While you are headed to the cafe with [new_coworker_name], an image on the billboard catches your attention."

    scene black with Dissolve(0.5)
    scene bg ending3_image1 with Dissolve(0.5)
    n "IMAGE ON THE BILLBOARD OF THE TIME GOD COMPANY - SHOW CLEARLY IT IS A BILLBOARD"
    n "{i}Is it...???"
    scene black with Dissolve(0.5)
    scene bg office_grill with Dissolve(0.5)


    show protagonist surprised at t31
    p "..."
    show protagonist neutral at s31

    show coworker2 hmm at t33
    coworker2 "Ugh, I hate that guy so much!"
    show coworker2 hmm at s33

    show protagonist surprised at t31
    p "You know him????"
    show protagonist neutral at s31

    show coworker2 neutral at t33
    coworker2 "Where do you think I worked before I came here? That guy’s my former boss."
    show coworker2 hmm
    coworker2 "Absolute pill of a manager. He has no respect for anyone."
    show coworker2 happy
    coworker2 "You have no idea how happy I am to be out from under his thumb."
    show coworker2 neutral at s33

    show protagonist talking at t31
    p "Yeah, I know that feeling. {w}Now, you get your second chance!"
    show coworker2 excited at t33
    coworker2 "I do! {w}Also, is this coffee place far away? {w}For some reason, I'm really craving some egg salad."
    show coworker2 at s33
    show protagonist joy at t31
    p "Oh yes! I love egg salad sandwiches too! We're really close by."
    show protagonist at s31
    show coworker2 happy at t33
    coworker2 "Great! {w}Forget about stupid ex-boss Tim, let's go!"
    coworker2 "Egg salad awaits!"
    show coworker2 at thide
    hide coworker2
    show protagonist at thide
    hide protagonist

    scene black with Dissolve(0.5)
    scene bg ending3_image1 with Dissolve(0.5)
    n "--- SAME IMAGE AS BEFORE, TIME GOD NEUTRAL/SMILING ---"
    scene black with Dissolve(1.0)
    scene bg ending3_image2 with Dissolve(1.0)
    n "--- ZOOM IN, THE TIME GOD IS ACTUALLY FROWNING ---"

    scene black with Dissolve(1.0)
    n "ENDING 3 OUT OF 3 {p}You can change your choices to discover other endings."
    return
