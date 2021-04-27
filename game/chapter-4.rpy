####################################################
label start_chapter4:

    # INITIALIZE VARIABLES FOR VISITED PLACES
    $ flag_visited_cafe = 0;
    $ flag_visited_office = 0;
    $ flag_visited_home = 0;

    # play music "funiculifunicula.mp3" fadeout 1       # ADD MUSIC

    n "{i}At some point in time... {p}When you really do not expect to be surprised by anything..."
    scene bg office with Dissolve(0.5)

    show boss talking at t33
    boss "Tomorrow's supposed to be the annual employee retreat. {w}But budget cuts this year."
    show boss happy
    boss "I was thinking of organizing a nice outdoor picnic for everyone instead."
    show boss neutral
    boss "[protagonist_name], do you want to take care of the grill?"
    show boss neutral at s33

    show protagonist excited at t31
    p "Oh yes, I'd love to! I am a master chef. Boss, I promise you"
    show protagonist joy
    p "Tomorrow you're going to eat the best burgers you've ever had!"

    show protagonist at thide
    hide protagonist
    show boss at thide
    hide boss
    scene black with Dissolve(0.5)



label chapter4_office_start:

    n "The day after..." with Dissolve(0.5)

    scene bg office_grill

    show protagonist excited at t31
    n "Picture of the protagonist, happy, holding burger in plate"
    p "So... what does everyone think?"
    show protagonist excited at s31

    show boss happy at t33
    boss "Wow, I truly was not expecting this from you. This is truly the best burger I've ever had!"
    show boss neutral at s33

    show coworker neutral at t11
    coworker "MMM! The onion, the extra pickles, the garlic scent."
    show coworker neutral at s11

    show boss talking_happy at t33
    boss "It's strong... but not overpowering. Really highlights the umami of the meat."
    show boss talking
    boss "Speaking of, that is some REALLY good burger meat. Where did you get it from?"
    show boss neutral at s33

    show protagonist joy at t31
    p "Oh, just the grocery store here on the way here. I'm so happy you like it!"
    show protagonist joy at s31

    show boss panicking at t33
    boss "Wait."
    boss "What is going on."
    boss "Oh, noooo. MY STOMACH!"
    n "image of boss throwing up"
    show boss at s33

    show protagonist surprised at t31
    p "Are you ok? What's going on?"
    show protagonist surprised at s31

    show boss neutral at t33
    boss "I'm... fine. You said the grocery store here? You know that place..."
    n "The boss vomits again"
    show boss at s33

    show protagonist anxious at t31
    p "Oh dang. Oh geez. Oh dang. Did I just poison the boss?"
    show protagonist hmm
    p "Oh heck that's a lot of throw-up. Are their guts coming out?"
    show protagonist anxious
    p "Oh no, are they going to die??? Did I just kill the boss?"
    show protagonist surprised at s31

    show coworker neutral at t11
    n "The coworker also starts vomiting"

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
    scene black with Dissolve(0.5)


####################################################
label chapter4_home_meetTimeGod:

    scene bg home with Dissolve(0.5)

    show protagonist anxious at t11
    p "Is there anything I can do to fix this?"
    p "If only I could travel back again."
    show protagonist surprised at s31

    show timegod creepy at t33
    g "I have a mission for you."
    show timegod at s33

    show protagonist anxious at t31
    p "Wonderful. Send me back now. I need to go back."
    p "I'll do whatever, please just send me back."
    show protagonist at s31

    show timegod neutral at t33
    g "Interesting. Very interesting."
    g "You have been performing quite satisfactorily. It is time to entrust you with a more important task."
    show timegod laugh
    g "Although important, this task is not particularly difficult."
    g "You must simply place a certain object at a specific place at a particular time."
    show timegod angry
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
            show timegod neutral at t11
        "I am ready":
            show timegod neutral at t11
        "I need to think about it":
            show timegod neutral at t11

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

    scene black with Dissolve(0.5)

    n "{i}The Time God snaps his fingers and you are transported back in the past."
    n "{i}It's 7:30am."

    scene bg cafeoutdoor with Dissolve(0.5)

    show protagonist neutral at t11
    p "I just need to do this task."
    p "Then I can save my boss and my coworkers as well."
    p "I have another chance. Let's do this."
    p "OK it looks like it's 7:30 am."
    p "I have to put the rock down at 9 exactly."
    p "Maybe I should head there early just to be safe?"
    hide protagonist

    menu:
        p "Maybe I should head there early just to be safe?"
        "Go to the Street":
            jump chapter4_street_early
        "Go to the Cafe":
            $ flag_visited_cafe = 1;
            jump chapter4_cafe_prelude
        "Go to the Office":
            $ flag_visited_office = 1;
            jump chapter4_office_prelude
        "Stay Home for a while":
            $ flag_visited_home = 1;
            jump chapter4_home_prelude


####################################################
label chapter4_street_early:

    scene bg cafeoutdoor with Dissolve(0.5)

    show protagonist neutral at t11
    p "Oof, finally made it here. What time is it?"
    p "Looks like it's 8:05 am. I have plenty of time to kill."
    p "Guess I'll wait at that bench."

    jump chapter4_street_decision


####################################################
label chapter4_street_decision:

    scene bg cafeoutdoor

    show protagonist anxious at t11
    n "You are standing in front of the road."
    n "The road has a huge traffic..."

    p "So... I just have to find the biggest rock I can."
    p "Let's see..."
    show protagonist at thide
    hide protagonist

    show protagonist neutral at t11
    p "Ok, this should work."
    p "Now, I just have to lay this big rock in the middle of the street at exactly 9:00 am."
    p "..."
    show protagonist talking
    p "It's 8:58 right now."
    show protagonist neutral
    p "..."
    show protagonist talking
    p "...Soon..."

    n "A loud sound from the road distracts you"

    show protagonist surprised
    p "Wait!"
    show protagonist hmm
    p "This is a really huge rock..."
    p "And that's a busy road..."
    p "..."
    show protagonist anxious
    p "What if the rock causes a car accident?"
    show protagonist surprised
    p "No. What if I am causing a car accident?"
    show protagonist at t31
    show protagonist anxious at s31

    show timegod neutral at t33
    g "What is the matter here?"
    show timegod laugh
    g "Might I remind you, your time's almost up."
    g "You need to put down that rock in a minute."
    show timegod angry
    g "You need to put down that rock in a minute, or you will suffer the consequences."
    show timegod at s33

    show protagonist hmm at t31
    p "But..."
    show protagonist at s31

    show timegod angry at t33
    g "But what?"
    g "You've done plenty of missions for me before. This is the same idea!"
    show timegod at s33

    show protagonist anxious at t31
    p "But this seems... different. It... it just doesn't seem safe."
    show protagonist surprised at t31
    p "What if there's a car accident? What if we kill someone?"
    show protagonist anxious at s31

    show timegod neutral at t33
    g "Safe?! You know what's not safe?"
    show timegod laugh
    g "TIME TRAVEL! But here you are, doing it anyway."
    g "You've never been one to shrink from a challenge, have you?"
    show timegod at s33

    show protagonist anxious at t31
    p "I mean, I guess not."
    show protagonist at s31

    show timegod happy at t33
    g "Exactly! This mission though? Laying a rock in the middle of the intersection?"
    g "That's the safest thing you'll do today."
    show timegod at s33

    show protagonist neutral at t31
    p "Hmm..."
    show protagonist at s31

    show timegod happy at t33
    g "Everything will be fine! Look at that rock. It's tiny!"
    show timegod at s33

    show protagonist anxious at t31
    p "Well, not really. It's a pretty big rock."
    show timegod angry
    p "Well, not really. It's a pretty big rock."
    show protagonist at s31

    show timegod happy at t33
    g "It's not. Trust me."
    show timegod creepy
    g "After all, when have I ever led you astray?"
    show timegod at thide
    hide timegod

    show protagonist hmm at t31
    p "It's 9am now. Now what should I do with this giant rock?"
    hide protagonist

    menu:
        p "It's 9am now. Now what should I do with this giant rock?"
        "Put the rock in the street.":
            jump chapter4_street_missionSuccess
        "Don't do it!":
            jump chapter4_street_missionFail



####################################################
label chapter4_cafe_prelude:

    scene bg cafe with Dissolve(0.5)

    show protagonist neutral at t31
    p "This seems kinda ominous."
    show protagonist at s31

    show barista neutral at t33
    barista "You were the one who dropped that letter off, right?"
    show protagonist anxious at s31
    p "Uhm..."
    barista "Where did you get this? Do you realize what this did? I still don't get how you even got a hold of this."
    barista "I don't even know who you are really."
    show barista at s33

    show protagonist hmm at t31
    p "Uhm... I uh..."
    show protagonist at s31

    show barista at t33
    barista "You know, I couldn't work after that."
    barista "Do you know how hard it is to work in the place where you found out someone is cheating on you?"

    show protagonist surprised

    barista "Day in and day out being reminded of that."
    show barista at s33

    show protagonist anxious at t31
    p "I don't uh... suppose I would..."
    show protagonist at s31

    show barista at t33
    barista "It took quite a bit of confidence to come in today."
    barista "I don't think you'd know that, dropping that letter off for someone else."
    show barista at s33

    show protagonist at t31
    p "Yeah uh I guess. I think that I'm gonna leave now."
    p "Probably not the best idea to eat."
    show protagonist at s31

    show barista at t33
    barista "Probably a good idea."
    hide barista

    show protagonist hmm at t31
    p "Where should I go now?"
    hide protagonist

    menu:
        p "Where should I go now?"
        "Go to the Street":
            scene black with Dissolve(0.5)
            jump chapter4_street_decision
        "Go to the Office" (disabled=False) if flag_visited_office==0:
            $ flag_visited_office = 1;
            scene black with Dissolve(0.5)
            jump chapter4_office_prelude
        "Go to the Office" (disabled=True) if flag_visited_office==1:
            $ flag_visited_office = 1;
            scene black with Dissolve(0.5)
            jump chapter4_office_prelude
        "Go back Home" (disabled=False) if flag_visited_home==0:
            $ flag_visited_home = 1;
            scene black with Dissolve(0.5)
            jump chapter4_home_prelude
        "Go back Home" (disabled=True) if flag_visited_home==1:
            $ flag_visited_home = 1;
            scene black with Dissolve(0.5)
            jump chapter4_home_prelude

label chapter4_office_prelude:
    scene bg office
    show protagonist neutral at t31
    p "I was late to work today because I was buying food for the party. I wonder what was going on in the office."
    p "I have time, maybe I should check it out?"
    scene black with Dissolve(0.5)
    scene bg office
    show protagonist neutral at s31
    show coworker neutral at t33
    coworker "Hey! I see you are early as well. I think this is the first time ever that I've been here before the boss."
    show coworker at s33
    show protagonist neutral at t31
    p "The boss isn't here yet? Don't they usually get in at like 6?"
    show protagonist at s31
    show coworker at t33
    coworker "Yeah, no clue what's going on. Although yesterday it seemed like they only just got here when I arrived."
    show coworker at s33
    show protagonist at t31
    p "Maybe something is stressing them out? Is there a big meeting coming up that I forgot about?"
    show protagonist at s31
    show coworker at t33
    coworker "Nah you're good. This week is pretty light as far as I can tell."
    coworker "The only other thing I can think of that would stress them out to this extent is if they lost their lucky pen or something."
    coworker "No way that could happen though, they hardly ever let it out of their sight."
    coworker "Anyway, I'm going to use this chance to take a small break. You should too, chances like these are rare."
    coworker "See you tonight at the picnic!"
    show coworker at s33
    show protagonist at t31
    p "See you! Have a good one."
    show protagonist at s31
    scene black with Dissolve(0.5)
    p "Where should I go now?"
    menu:
        p "Where should I go now?"
        "Go to the street":
            jump chapter4_street_decision
        "Go to the cafe" if flag_visited_cafe == 0:
            $ flag_visited_cafe = 1
            jump chapter4_cafe_prelude
        "Go to the office" if flag_visited_office == 0:
            $ flag_visited_office = 1
            jump chapter4_home_prelude


label chapter4_home_prelude:
    scene bg home
    show protagonist joy at t11
    p "Ahh, home sweet home."
    p "And with time to spare. I've been working pretty hard and I'm pretty sure you aren't meant to time travel tired."
    if mission2personal_success == 1:
        p "Hopefully with all these bonuses I can buy another Wookie costume."
    scene black with Dissolve(0.5)
    n "Three hours later..."
    scene bg home
    show protagonist neutral at t11
    p "Welp, back to the grindstone."
    if mission1personal_success == 1:
        p "Glad I learned to make coffee. Heh, bean water."

    scene black with Dissolve(0.5)
    p "Where should I go now?"
    menu:
        p "Where should I go now?"
        "Go to the street":
            jump chapter4_street_decision
        "Go to the cafe" if flag_visited_cafe == 0:
            $ flag_visited_cafe = 1
            jump chapter4_cafe_prelude
        "Go to the office" if flag_visited_office == 0:
            $ flag_visited_office = 1
            jump chapter4_office_prelude

label chapter4_street_missionFail:
    scene bg road
    show protagonist anxious at t31
    p "I'm not so sure about this. I don't think I can."
    show protagonist at s31
    n "You see your boss driving by, waving to you."
    show protagonist surprised at t31
    p "Hey, that was my boss!"
    show protagonist at s31
    show timegod neutral at t33
    g "I'm aware."
    show timegod angry at t33
    g "Why didn't you follow my demands? Everything I have done has been for your benefit."
    show timegod at s33
    show protagonist anxious at t31
    p "But the rock in the road would have..."
    show protagonist at s31
    show timegod at t33
    g "Yes, I'm aware."
    show timegod neutral at t33
    g "You really shouldn't have done that. You've failed."
    show timegod at s33
    show protagonist hey at t31
    p "I've failed? You told me that this wouldn't do any damage! I'm pretty sure that would have caused a car accident. Why my boss?"
    show protagonist hey at s31
    show timegod angry at t33
    g "Events work themselves out. This would've been fine. I don't think you understand the intricacies of traveling through time."
    g "Sometimes, there is collateral damage. But in the end, it helps us all."
    show timegod at s33
    show protagonist hey at t31
    p "What!?"
    p "NONE of what I've done would have helped anyone! You lied to me this entire time!"
    show protagonist at s31
    show timegod creepy at t33
    g "Are you sure? Look across the street, see how you've failed."
    show timegod at s33
    scene black with Dissolve(0.5)
    scene bg road
    show pastprotagonist neutral at t11
    pp "Welp, I've got the burger meat. I got a good feeling about today. These last few weeks have been coming up all me. This grocery store never lets me down."
    scene black with Dissolve(0.5)
    show protagonist neutral at s31
    show timegod neutral at t33
    g "See? You've failed. Your entire office is going to suffer from this. Poisoning your coworkers isn't exactly beneficial. Do you realize what you've done?"
    show timegod at s33
    show protagonist at t31
    p "Yea, I saved my boss. I'm not sure either of these things outweigh the other."
    show protagonist at s31
    show timegod angry at t33
    g "You don't realize the repercussions of your actions. You do understand that I am a TIME GOD?"
    g "There is a perfectly good reason for why I tell you what I do."
    show timegod happy at t33
    g "It's to your benefit that I'm a kind lord. You have an opportunity here to undo your mistakes, although you're testing the limits of my kindness."
    g "Here, your reputation can be salvaged. Simply, complete this mission for me. Let us try this again."
    show timegod snap1 at s33
    show timegod snap2 at s33
    scene black with Dissolve(0.5)
    scene bg home
    # [Jumps to present (home), akin to beginning of mission]
    show timegod laugh at t33
    g "Hopefully that brief jump has allowed you to regain your sanity. My kindness can only go so far so please do not fail this again."
    show timegod at s33
    show protagonist hey at t31
    p "No! I don't know who's benefit this is for, but it certainly isn't mine. Or anyone's. In what world is dying better than food poisoning?"
    show protagonist neutral at t31
    p "I'm pretty sure one of those is treatable. Why are you doing this?"
    g "You wouldn't understand. I'm simply taking care of what is important."
    p "What could be this important?"
    show protagonist neutral at s31
    show timegod neutral at t33
    g "Interesting question, but I didn't come to you to respond to these questions."
    g "I came to you so you could complete these tasks for the benefit of all."
    show timegod at s33
    show protagonist hey at t31
    p "I can't do this! I'm not going to kill anyone! I'm done. Consider this working relationship terminated. I don't need time travel to improve myself."
    show protagonist hey at s31
    show timegod creepy at t33
    g "You're going to regret this."
    hide timegod creepy

    scene black with Dissolve(1.0)
    n "END OF MISSION 4"
    jump start_chapter5
    #return







label chapter4_street_missionSuccess:
    scene bg road
    show protagonist neutral at t31
    p "Whew. Ok, I did it. Now what?"
    # [fullscreen image of boss in car]
    # [return back to street background image with p in foreground]
    n "You see your boss in the car."
    show protagonist surprised at s31
    p  "OH! Oh no!"
    # [fullscreen image of boss in car]
    # [fullscreen image of boss's car hitting that giant rock, car kinda tipping forward]
    n "Your boss's car hits the giant rock, tipping forward."
    # [back to street background image with p in foreground]
    # p [still surprised, just watching in shock. No words]
    # [fullscreen image of boss in car. But now instead of neutral face, boss is PANICKING]
    n "You see your boss is panicking."
    n "The car crashes and you hear a cacophony of car horns."
    scene black with Dissolve(0.5)
    scene bg road_carcrash with Dissolve(0.5)
    n "The scene looks like the remnants of a car accident."
    # [crash sound]
    # [cacophony of car horns]
    # [back to street background image with p in foreground. But now there are remnants of a car accident in the street]
    show protagonist anxious at t31
    p "What... What did I just do?"
    show protagonist at s31
    show timegod happy at t33
    g "Oh, turn that frown upside down. You succeeded!"
    show timegod at s33
    show protagonist hey at t31
    p "SUCCEEDED?"
    p "What do you mean, SUCCEEDED?"
    p "I just killed my boss! For real this time!"
    p "You––You told me! You told me this was fine! That I wouldn't cause a car accident!"
    show protagonist at s31
    show timegod neutral at t33
    g "Well... I certainly told you the former. But the latter, I didn't make that promise."
    g "You see. When you travel back in time, accidents, disappearances, deaths... They happen sometimes."
    g "Collateral damage, one might say."
    show timegod at s33
    show protagonist at t31
    p "You misled me! You lied! How is anything even REMOTELY fine?"
    show protagonist at s31
    show timegod happy at t33
    g "On the contrary, actually. If you look across the street right about... now"
    hide protagonist hey
    hide timegod happy
    # TODO: past protagonist anxious assets
    show pastprotagonist neutral at t11
    pp "Oh no. Oh no. Oh no. It's 9:05. I'm late for work, again!"
    pp "AND I still have to get the burger meat."
    n "You notice the scene."
    pp "AND there's a car accident blocking traffic. Great."
    pp "Ok, you know what? Burger day can wait. The boss will understand. I gotta get to work."
    hide pastprotagonist neutral

    scene black with Dissolve(0.5)
    scene bg road

    show protagonist neutral at s31
    show timegod happy at t33
    g "See? What did I tell you? You avoided the burger situation. Everything's worked out just fine."
    show timegod at s33
    show protagonist at t31
    p "We killed him."
    show protagonist hey at t31
    p "This mission of yours... It killed him"
    show protagonist at s31
    show timegod neutral at t33
    g "Certainly an outcome you didn't expect. That happens."
    show timegod happy at t33
    g "Overall, still a win-win for the two of us."
    show timegod at s33
    show protagonist at t31
    p "WHY? Why are you doing this?"
    p "What are you trying to accomplish?"
    p "I killed my boss. Why in the WORLD did you involve me in this mess?"
    show protagonist at s31
    show timegod creepy at t33
    g "Because..."
    show timegod happy at t33
    g "I'm taking care of what's important."
    show timegod at s33
    show protagonist at t31
    p "WHAT? Taking care of what's important?"
    p "What does that even mean?!"
    show protagonist at s31
    show timegod laugh at t33
    g "That's an interesting question."
    show timegod at s33
    show protagonist hmm at t31
    p "Oh, great. Yet another non-answer."
    show protagonist at s31
    show timegod at t33
    g "Speaking of taking care... now that we've both gotten what we wanted, I'm sorry to inform you that our working relationship will be terminated."
    g "It was truly a pleasure working with you. I wish you the best luck in your future professional endeavors."
    show timegod at s33
    show protagonist hey at t31
    p "What in the WORLD are you saying?"
    show protagonist at s31
    show timegod at t33
    g "I'm saying my goodbyes."
    show timegod snap1 at t33
    show timegod snap2 at t33
    scene black with Dissolve(0.5)
    #jump chapter4_home_missionSuccess_present


label chapter4_home_missionSuccess_present:
    scene bg home with Dissolve(0.5)
    show protagonist anxious at t11
    p "What. What just happened?"
    p "What do I do now?"
    p "I should... I should be at work."
    n "You hear a ding message sound"
    n "You receive a text from your coworker. It reads:"
    n "WHERE ARE YOU? ARE YOU OK?"
    n "BOSS WAS IN A CAR ACCIDENT AT KRONOS. MULTI-CAR PILEUP. ISN'T THAT CLOSE TO WHERE YOU LIVE?"
    n "EVERYONE AT THE OFFICE IS PANICKING"
    n "TEXT ME"
    n "NOW"

    scene black with Dissolve(1.0)
    n "END OF MISSION 4"
    jump start_chapter5
    #return
