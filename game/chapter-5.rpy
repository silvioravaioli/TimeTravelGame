####################################################
label start_chapter5:

    menu:
        n "Which ending do you want to test?"
        "Final mission success":
            jump epilogue_finalMissionSuccess
        "Final mission failure":
            jump epilogue_finalMissionFailure




####################################################
label epilogue_finalMissionSuccess:

    scene bg home

    n "image of protagonist dressed in funeral shirt/tie, packing a box of his stuff at the office"
    n "images of protagonist being sad, in different places at home, same background but P is just in different locations on the screen"

    show protagonist anxious at t11
    p "I... I’m going crazy at home by myself!"
    p "The house is a mess, I am a mess!"
    p "I should start looking for a job again"
    show protagonist at thide
    hide protagonist

    n "image of computer screen, website of rival company with motto, protagonist’s mouse clicking on the Apply Now button"






####################################################
label epilogue_finalMissionSuccess_jobSearch:

    scene black with Dissolve(0.5)
    scene bg home with Dissolve(0.5)

    n "Two weeks later"
    n "Background: bulletin board, contains 1 picture of the time god somewhere on the board, the mission of the rival company is displayed somewhere"

    show protagonist neutral at t11
    p "First day of work! I need to make a good impression..."
    p "What if my boss is mean?"
    show protagonist anxious
    p "What if my coworkers hate me?"
    p "Oh dear. I better not mess up."
    p "Ok, I better get ready to meet my new boss"
    show protagonist at thide
    hide protagonist

    scene black with Dissolve(0.5)
    scene bg office with Dissolve(0.5)

    show timegod neutral at t33
    g "Oh, hello!"
    show protagonist shocked at s31
    g "You must be XXXXX, our new employee!"
    show timegod at s33

    show protagonist at t31
    p "You... You..."
    show protagonist hey
    p "You screwed up my life! What are you DOING here?!"

    show timegod laugh
    "Oh, XXXXX. You must be mistaken! I’m Tim. You’ll be working under me here."

    show protagonist shocked
    p "I’ll be WHAT?"
    p "You’re my BOSS?"
    show protagonist at thide
    hide protagonist

    show timegod happy
    g "Anyway, let’s get started. First of all, I want to warmly welcome you to the team."
    g "Here at TG Home Insurance, we think of our employees and our clients as one big family."
    g "Above all, we value providing the very best standard of service to our customers"
    g "In reflection of this attitude, our mission is ‘taking care of what’s important.’"
    g "Now that we’ve got the orientation spiel covered..."
    g "Let’s get to work!"
    return




####################################################
label epilogue_finalMissionFailure:

    scene bg home

    show boss neutral at t33
    boss "Hey! XXXXX! Get over here!"

    show protagonist anxious at t31
    p "Oh... Hi boss."
    show protagonist surprised
    p "Wait! You’re alive???"
    show protagonist anxious
    p "I... I mean, how are you feeling?"
    show protagonist happy

    boss "Really good actually! They checked me up at the ER and turns out I just had some bad food poisoning"
    boss "Oh man, I spent the night on the toilet. But now, I’m good as new!"
    boss "And, you know. Even though I was spewing stuff from both ends…"
    boss "By GOD, that was the BEST burger I’ve ever had!"

    show protagonist blushing
    p "Really? You liked my burgers that much?"

    b "Oh, absolutely! Worth the diarrhea."

    hide boss
    hide protagonist

    menu:
        n "Which ending do you want to test?"
        "High Reputation":
            jump label_epilogue_finalMissionFail_highRep
        "Low Reputation":
            jump label_epilogue_finalMissionFail_lowRep




####################################################
label epilogue_finalMissionFail_highRep:

    scene bg home

    boss "On the topic of great things, the work you’ve done these past few weeks has been incredible."
    boss "I’ve really been admiring all the great work you’ve done, and I believe it deserves some attention."

    # IF MISSION 1 SUCCESS
    boss "Bang-up job with the coffee."
    p "Yeah, that’s me! I’m pretty good at stuff."

    # IF MISSION 2 SUCCESS
    boss "Absolutely nailed that meeting as well. Made me proud to work in home insurance."

    boss "So, I’d like to offer you a promotion to my assistant. You’ll get all the great bits and bobs: experience, more time in the office, and a slightly higher salary!"
    p "Oh boy, that’s pretty swell."
    boss "Don’t use up all your enthusiasm! I’ve got a first job for ya now that you’re in the big leagues, great time to prove yourself again. As you know, we’ve got quite a bit of rivals, not just a bit, they number us pretty heavily. I’m going to need you to give me a full profile of each of these."
    boss "There’s no page requirement, but just make sure you include all the basics. There’s around 40 companies in the area, but I heard the Internet will be pretty good for this one."
    p "Uhh... doesn’t that seem to be..."
    boss "Don’t worry, you’ve been doing pretty good with this stuff. So much so, that I think you can get it done by next week."

    n "Jump to office at night (or just an indication it’s later, art team discretion)"
    n "Two options for this, up to art team: Either a montage of the Protagonist in various positions in the office (same scene)"
    n "or could just show a slumped version of him over a computer looking tired, disheveled"
    p "How long has it been? How much time do I have left? Went from coffee and burgers to this every night. Oh jeez..."
    p "Wait a minute..."
    n "Shows computer screen, is picture of Time God as representative for rival company, zooms in and TG is there"
    return



####################################################
label epilogue_finalMissionFail_lowRep:

    scene bg home

    show protagonist neutral at t11
    p "xxxx"
    p "xxxx"
    p "xxxx"
    p "xxxx"
    p "xxxx"
    p "xxxx"


    boss "On the topic of great things, the work you’ve done these past few weeks has been incredible."
    boss "This month’s promotion is going to ---insert coworker name----, but keep up the good work and you might just get lucky next time."
    p "You don’t think I’ve just been a huge doofus? The coffee... and the costume... not to mention the burger incident"
    boss "Everyone makes these kinds of mistakes. My first week on the job, I accidentally left the thermostat on -70 degrees instead of 70 degrees. We had to use ice skates to get around the office for an entire month."
    boss "But at least that’s one mistake I’ll never make again. With time, you’ll make more mistakes and learn from them as well. In a few years, you may even be running this place."
    p "I won’t let you down! Is there anything I can do to prove myself?"
    boss "Actually..."

    n "A new coworker stumbles into office, and trips while entering!"
    coworker2 "Hello boss. It’s nice to finally meet you in person!"
    boss "Welcome to the company, NC. You have impeccable timing, that will take you far."
    boss "I was just about to ask ---- here if he would be willing to show you around."


    p "Nice to meet you, NC. It’d be a pleasure to show off our exquisite linoleum flooring."
    n "P and NC walk out of office, pass old star wars day posted"
    coworker2 "OH SHOOT! YOU GUYS HAD STAR WARS DAY!"
    p "Are you a Star Wars fan?"
    coworker2 "Am I?! Heck yeah. If only I joined this company earlier you would have seen my sweet homemade wookie costume."
    p "Well good thing you weren’t here, because there’s no way you could have held a candle to mine. I even used wookie-scented paint to make the outfit truly authentic."
    coworker2 "What’s even the point of a wookie costume without wookie-scented paint? At that point it’s just a bigfoot costume."
    p "I know, right?"
    coworker2 "By the way, is there a place to get coffee around here?"
    p "Yeah, there’s a coffee machine right by the conference room."
    coworker2 "Umm..."
    coworker2 "This is pretty awkward, but I don’t actually know how to use a coffee machine. I’ve always gotten my coffee at Starbucks."
    coworker2 "Would you mind showing me how to use it?"
    p "Umm..."
    p "To be honest, I don’t know either. I don’t really drink coffee very often so I didn’t think I’d need to learn."
    p "You know what. There’s a pretty good cafe a few blocks from here. How about we take a short break and grab some coffee there. It’ll be my treat."
    coworker2 "I’m down. Show the way."
    n "image of protagonist and new coworker walking towards cafe with billboard of Time God company in front of them"
    p "(shocked): ..."
    coworker2 "(spitting): Ugh, I hate that guy so much."
    p "You know him????"
    coworker2 "Where do you think I worked before I came here? That guy’s my former boss."
    coworker2 "Absolute pill of a manager. He has no respect for anyone."
    coworker2 "You have no idea how happy I am to be out from under his thumb."
    p "Yeah, I know that feeling."
    n "image of protagonist and new coworker walking away from billboard"
    n "zoom on Time God’s face, frowning"

    return
