####################################################
label start_chapter3:

    # INITIALIZE VARIABLES FOR VISITED PLACES IN PAST
    $ mission3visited_past1_Cafe = 0
    $ mission3visited_past1_Office = 0
    $ mission3visited_past1_Home = 0
    $ mission3visited_past1_Street = 0

    #INITIALIZE VARIABLES FOR VISITED PLACES IN PRESENT
    $ mission3visited_present_Cafe = 0
    $ mission3visited_present_Office = 0
    $ mission3visited_present_Home = 0
    $ mission3visited_present_Street = 0


    n "{i}Some days, hours, minutes, and seconds later..."

    scene bg office with Dissolve(0.5)

    show boss neutral at t33
    boss "Hey, [protagonist_name]! You busy?"
    show boss neutral at s33

    show protagonist neutral at t31
    p "Uh... Yeah, a little bit."
    show protagonist neutral at s31

    show boss neutral at t33
    boss "Yeah, sure."
    boss "I need you to take care of my dog."
    show boss neutral at s33

    show protagonist anxious at t31
    p "But I just said-"

    show boss neutral at t33
    boss "Our dog walker is sick today and there was nobody to take care of little Princess at home"
    show protagonist anxious at s31
    boss "And I have back-to-back meetings today, so I need you to take her"
    show boss neutral at s33

    show dog neutral at t11
    show boss happy at t33
    boss "Be good, little Princess girl ok?"
    show dog cool
    boss "Oh, you’re so cute."
    show dog cool at s11
    boss "Look at those eyes."
    show dog happy
    boss "Oh Princess, you are one adorable girl"
    show dog neutral
    boss "I love you! I love you!"

    show protagonist blush
    p "Uh..."

    show boss angry at t33
    boss "Mind your business!"
    show boss talking
    boss "And take good care of her ok?"
    hide boss

    show protagonist talking at t31
    p "Looks like it’s just you and me, Princess."
    show protagonist joy
    p "Huh, I guess you are kinda cute."
    hide protagonist

    scene black with Dissolve(0.5)
    n "{i}Two hours later"
    scene bg office with Dissolve(0.5)

    show protagonist talking at t11
    p "HA! I finally finished my work. Now, it’s time for my..."
    show protagonist joy
    p "LUNCH BREAK!"
    p "Egg salad sandwich, here I come!"

    show dog neutral at t33

    show protagonist anxious
    p "Oh... Shoot."
    p "I forgot. I can’t take you out to the cafe."
    p "I guess it’s going to be another office lunch then... Did I even bring anything?"
    p "Let me check in my bag."
    hide protagonist

    n "{i}You have a vague memory of something that has been in your bag for a while..."

    show protagonist joy at t11
    p "AHA! Found it! {p}This beef jerky looks delicious!"
    show protagonist hmm
    p "Oh... Wait... It did expire 5 year ago."
    show protagonist joy
    p "But what is life without a little bit of risk?"
    p "Plus, expiration dates are basically suggestions, right"
    p "Lunch!"

    show dog happy
    n "{i}Princess also wants her lunch! She is joyfully jumping around."
    n "{i}Princess grabs the beef jerky, and runs away..."
    hide dog

    show protagonist hey
    p "Hey! That’s my beef jerky!"
    p "Princess! Get back here!"
    p "Remember when I said you were kinda cute?"
    p "Well now I TAKE IT BACK!"
    p "PRINCESS!"
    p "PRINCESS! Princesssss!"
    p "PRINCESS, GIVE ME BACK MY LUNCH"

    show protagonist anxious
    p "Princess?"
    p "Oh... no.... Did I just lose the dog?"
    p "DANG IT! {w}Now I gotta go look for her... {w}And I’m still hungry."
    p "Where could she have possibly gone?"
    hide protagonist

    menu:
        p "Where could she have possibly gone?"
        "Cafe":
            scene black with Dissolve(0.5)
            jump chapter3_travel1DogSearch_Cafe
        "Street":
            scene black with Dissolve(0.5)
            jump chapter3_travel1DogSearch_Street
        "Home":
            scene black with Dissolve(0.5)
            jump chapter3_travel1DogSearch_Home



####################################################
label chapter3_travel1DogSearch_Cafe:

    scene bg cafe with Dissolve(0.5)
    $ mission3visited_present_Cafe = 1

    show protagonist neutral at t11
    p "Hmmm... {w}I don’t see the dog here either."
    p "Probably a bad time to order something as well."
    p "Princess could have eaten all of the beef jerky by now. {w}Can't possibly be good for a dog"
    p "Where could she have possibly gone?"
    hide protagonist

    if (mission3visited_present_Street == 0):
        menu:
            p "Where could she have possibly gone?"
            "Street":
                scene black with Dissolve(0.5)
                jump chapter3_travel1DogSearch_Street
            "Home":
                scene black with Dissolve(0.5)
                jump chapter3_travel1DogSearch_Home
    else:
        menu:
            p "Where could she have possibly gone?"
            "Home":
                scene black with Dissolve(0.5)
                jump chapter3_travel1DogSearch_Home

####################################################
label chapter3_travel1DogSearch_Street:

    scene bg road with Dissolve(0.5)

    $ mission3visited_present_Street = 1
    show protagonist neutral at t11
    p "Hmmm... {w}The dog is nowhere to be seen."
    p "Where could she have possibly gone?"
    hide protagonist

    if (mission3visited_present_Cafe == 0):
        menu:
            p "Where could she have possibly gone?"
            "Cafe":
                scene black with Dissolve(0.5)
                jump chapter3_travel1DogSearch_Cafe
            "Home":
                scene black with Dissolve(0.5)
                jump chapter3_travel1DogSearch_Home
    else:
        menu:
            p "Where could she have possibly gone?"
            "Home":
                scene black with Dissolve(0.5)
                jump chapter3_travel1DogSearch_Home


####################################################
label chapter3_travel1DogSearch_Home:

    scene bg home with Dissolve(0.5)

    show protagonist hmm at t31
    p "Eh, you usually find stuff where you least expect it. Might as well check home."

    show timegod neutral at s33
    show protagonist neutral at t31
    p "Oh hey, it’s you again. Guess I shouldn’t be surprised"

    show timegod laugh at t33
    g "Well, it seems yet again, you’ve had another bad day."
    show timegod laugh at s33

    show protagonist anxious at t31
    p "Was it that obvious? Have you seen a dog in there?"
    show protagonist anxious at s31

    show timegod neutral at t33
    g "I have a mission I need completed."
    show timegod neutral at s33

    show protagonist talking at t31
    p "Sounds good, the past is always pretty neat. Would definitely help"
    show protagonist talking at s31

    show timegod happy at t33
    g "Exquisite."
    show timegod neutral at t33
    g "The mission is fairly simple."
    g "You have probably seen a poster commemorating the birth date of one of your colleagues on a glass wall near the back of your workplace."
    g "The poster is quite out of date and needs to be removed. This needs to be done exactly two weeks ago."
    hide timegod
    hide protagonist

    menu:
        "Sounds good. You can count on me.":
            show timegod happy at t11
        "Why two weeks ago?":
            show timegod angry at t11

    g "That beef jerky has been in your backpack for five years. {w}But my task for you {i}needs{\i} to be completed two weeks ago."
    show timegod angry at t11
    g "Do not fail me."
    show timegod snap1
    g "Do not fail me."
    show timegod snap2
    g "Do not fail me."
    show timegod at thide
    hide timegod

    scene black with Dissolve(0.5)
    #jump chapter3_past1_Home


####################################################
label chapter3_past1_Home:

    # MARK THE LOCATION AS VISITED
    $ mission3visited_past1_Home=1

    scene bg home with Dissolve(0.5)
    show protagonist hmm at t11
    p "Wow, my house really doesn’t change that much."
    p "Alright, taking that poster down shouldn’t be too hard, I should have enough time to fix the whole dog issue as well."
    p "I don’t even think that beef jerky is safe for people."
    show protagonist anxious at t11
    p "Has it really been there for five years? I guess I haven't cleaned that backpack out since I found it."
    p "I probably could just take it out, although I wouldn’t have an emergency snack then."
    p "Where would I even be at this point? Guess I’ll start looking. I probably should get that poster down though."
    hide protagonist

    menu:
        p "Where would I even be at this point?"
        "Go to Cafe":
            scene black with Dissolve(0.5)
            jump chapter3_past1_Cafe
        "Go to Office":
            scene black with Dissolve(0.5)
            jump chapter3_past1_Office


####################################################
label chapter3_past1_Office:

    # MARK THE LOCATION AS VISITED
    $ mission3visited_past1_Office=1

    scene bg office with Dissolve(0.5)
    show protagonist hmm at t11
    p "I'm surprised I’m not in the office yet. Seems it's the wrong time..."

    if mission3visited_past1_Cafe==0:
        p "Oh jeez, was this the day I was late cause I set my alarm for 8 PM? Seriously?"
        p "If I remember correctly, I would either be at the Cafe for that donut-coffee deal or trying to get to work. Might as well just finish what I was brought to do."

    p "I guess I really don’t go back here that much, but that poster has been up for a while."
    p "Not sure why the custodians don’t just take it down, can’t even tell there is a glass wall here without it. They do a pretty good job."
    p "Seems kind of odd for a literal Time God to want me to take down a poster."
    p "Gotta be something here. At the same time, their words seemed pretty strong."
    show protagonist joy at t11
    p "Found it! What should I do now?"
    hide protagonist

    menu:
        p "Found it! What should I do now?"
        "Take down poster":
            jump chapter3_past1_OfficeMissionSuccess
        "Do not take down poster":
            jump chapter3_past1_OfficeMissionFail


####################################################
label chapter3_past1_OfficeMissionFail:

    show protagonist neutral at t11
    p "Well... I should take down that poster. But..."
    show protagonist anxious
    p "It is someone else’s birthday poster... What if they get mad at me?"
    p "Yeah, maybe I can come back to it later? After everyone’s left the office?"
    show protagonist neutral
    p "Either way, I gotta find that backpack. There’s a dog waiting on me here."
    p "Not sure if it’s considered waiting if it’s in the future though."

    if mission3visited_past1_Cafe==0:
        p "I can’t really remember where I was right now. Could be at the cafe or trying to book it to work."

    if mission3visited_past1_Cafe==1:
        p "Pretty sure my past self is trying to get to work right now"

    p "Where should I go next?"
    hide protagonist

    menu:
        p "Where should I go next?"
        "Go to Street":
            scene black with Dissolve(0.5)
            jump chapter3_past1_Street
        "Go to Cafe" (disabled=False) if mission3visited_past1_Cafe==0:
            scene black with Dissolve(0.5)
            jump chapter3_past1_Cafe
        "Go to Cafe" (disabled=True) if mission3visited_past1_Cafe==1:
            scene black with Dissolve(0.5)
            jump chapter3_past1_Cafe


####################################################
label chapter3_past1_OfficeMissionSucc:

    #[SET THE PERSONAL MISSION TO SUCCESS]
    $ mission3personal_success = 1

    show protagonist neutral at t11
    p "Sorry old friend, but your birthday celebrations will finally end. I’ve been sent back in time just to remove you. I kinda wonder why."
    p "Still need to find myself though, gotta get that jerky and save Princess."

    if mission3visited_past1_Office==0:
        p "I can’t really remember where I was right now. Could already be at the office or trying to book it to work. Still gotta remove that poster too."

    if mission3visited_past1_Office==1:
        p "Pretty sure my past self is trying to get to work right now."

    p "Where should I go next?"
    hide protagonist

    menu:
        p "Where should I go next?"
        "Go to Street":
            scene black with Dissolve(0.5)
            jump chapter3_past1_Street
        "Go to Cafe" (disabled=False) if mission3visited_past1_Cafe==0:
            scene black with Dissolve(0.5)
            jump chapter3_past1_Cafe
        "Go to Cafe" (disabled=True) if mission3visited_past1_Cafe==1:
            scene black with Dissolve(0.5)
            jump chapter3_past1_Cafe


####################################################
label chapter3_past1_Cafe:

    # MARK THE LOCATION AS VISITED
    $ mission3visited_past1_Cafe=1

    scene bg cafe with Dissolve(0.5)
    show protagonist neutral at t11

    if mission3visited_past1_Office==0:
        p "Oh, cool. The cafe’s doing that special deal for coffee and a donut."
        p "That really saved my morning vibe when I was late a few weeks ago."
        p "Guess that means I’m either at the office or trying to hustle to work."

    p "Hmmmm. I don’t see myself anywhere, my timing was a bit off."
    p "Was worth a shot though."

    if mission3visited_past1_Office==0:
        p "This is gonna be interesting. Should I go take that poster down or get the jerky?"
        p "Probably can’t doddle here too long."

    if mission3visited_past1_Office==1:
        p "Guess I got one option. I’ve gotta be near my house at this point."

    p "Where should I go next?"
    hide protagonist

    menu:
        p "Where should I go next?"
        "Go to Street":
            scene black with Dissolve(0.5)
            jump chapter3_past1_Street
        "Go to Office" (disabled=False) if mission3visited_past1_Office==0:
            scene black with Dissolve(0.5)
            jump chapter3_past1_Office
        "Go to Office" (disabled=True) if mission3visited_past1_Office==1:
            scene black with Dissolve(0.5)
            jump chapter3_past1_Office


####################################################
label chapter3_past1_Street:

    # MARK THE LOCATION AS VISITED
    $ mission3visited_past1_Street=1

    scene bg cafeoutdoor

    show pastprotagonist anxious at t33
    pp "Oh dear, oh dear, oh dear."
    show pastprotagonist at thide
    hide pastprotagonist


    show protagonist talking at t31
    p "Ah of course. Late to work. Why didn’t I think of that sooner?"
    p "Good. He– I mean, I am carrying that backpack too! So the beef jerky’s gotta be in there"
    p "Now, how do I get that backpack off my past self?"
    hide protagonist

    menu:
        p "Now, how do I get that backpack off my past self?"
        "Tackle past self":
            jump chapter3_past1_Street_tackle
        "Distract past self":
            jump chapter3_past1_Street_distract


####################################################
label chapter3_past1_Street_tackle:

    #scene bg home

    show protagonist hmm at t31
    p "I could knock out my past self, take the backpack, and bolt?"
    show protagonist joy
    p "Let’s do this!"
    show protagonist joy at t11

    show pastprotagonist hey at t33
    pp "HEY! Who just hit me??"

    show protagonist anxious
    p "Uh oh... that should’ve knocked me out"

    show pastprotagonist hey_left
    pp "What do you THINK you’re do––"
    show pastprotagonist surprise_left
    pp "What.... What? Are you?"

    show protagonist anxious at t11
    p "Well... that wasn’t supposed to happen."
    show protagonist anxious at s11

    show pastprotagonist hey_left at t33
    pp "Who are you and why do you look exactly like me?"
    show pastprotagonist hey_left at s33

    show protagonist at t11
    p "Uh...."
    p "I don’t even know how to answer that. Can you just forget you saw me?"
    show protagonist at s11

    show pastprotagonist at t33
    pp "NO??"
    show pastprotagonist at s33

    show protagonist despair at t11
    p "Please? I really have no time for this. If you could just... {w}Let me take your backpack for one sec"
    show protagonist despair at s11

    show pastprotagonist at t33
    pp "And let you steal my stuff? I don’t THINK so"
    show pastprotagonist at s33

    show protagonist anxious at t11
    p "I’m not a thief!"
    p "I just need to see your backpack!"
    p "There’s something in there that I need! Please!"
    show protagonist at s11

    show pastprotagonist at t33
    pp "No! Get away from me!"
    show pastprotagonist at s33

    show protagonist at t11
    p "I need you to just give me..."
    p "Please! Trust me."
    show protagonist at s11

    show pastprotagonist at t33
    pp "I don’t even know who you are! WHY DO YOU LOOK LIKE ME?"
    pp "Doppelganger? ARE YOU MY SECRET CLONE?"
    show pastprotagonist at s33

    show protagonist at t11
    p "Ok, ok fine! You leave me no choice"
    p "I’m you but from the future––"

    show pastprotagonist surprise_left at t33
    pp "YOU’RE WHAT?!"

    show timegod angry at t31
    g "That’s it. I’m taking you back"
    p "No! But––"
    show timegod snap1

    scene black with Dissolve(0.5)
    jump chapter3_present_Home_tackleOutcome


####################################################
label chapter3_past1_Street_distract:

    #scene bg home
    $ mission3personal_success=1

    show protagonist neutral at t11
    p "Gotta distract him somehow. It’s gonna be tough, I’m a fairly smart guy."
    p "Just need to get that backpack away from ‘em. Good thing I don’t fully wear my backpack, just sort of carry it. In hindsight, that’s probably an awful idea."
    p "Should be a pretty straightforward rouse, I’ll just get him to run and drop it. I enjoy puppies quite a bit, so that should work well."

    n "You hide in a bush"

    p "Hmmm. Definitely need to hide my voice. He’ll recognize me. I’m gonna be real surprised if this works."
    p "HEY YOU, [protagonist_name], there’s a puppy around the corner! Get there quick before it runs away!"

    pp "What? No way! I gotta see this!"
    n "{i}Past you runs to dog, abandoning the backpack as he runs"
    show pastprotagonist at thide
    hide pastprotagonist

    show protagonist at t11
    p "Wow, I'm surprised that worked. {w}Now I just gotta find that beef jerky"
    show protagonist at thide
    show protatonist joy at t11
    p "AHA! I got it! {w}Now that I've got the beef jerky, Princess for sure won't get lost!"
    show protagonist anxious
    p "But I'm a little bit hungry..."
    show protagonist talking
    p "Eh, eating a little bit can't hurt, right?"
    n "{i}Despite common sense, you eat the beef jerky that's been sitting in your backpack for the past 5+ years"
    p "MMMM! Delicious! {w}Wow, I am SO HUNGRY!"
    show protagonist anxious
    p "Oh wait... {w}Oh no..."
    show protagonist surprised at t11

    show timegod angry at t33
    g "This is a fairly interesting spot to find you considering your task was at your office-building."

    if mission3timegod_success == 0:
        jump chapter3_past1_street_distract_FailTG
    else:
        jump chapter3_past1_street_distract_SucceedTG


####################################################
label chapter3_past1_street_distract_FailTG:

    scene bg home

    show protagonist neutral at t11
    p "xxxx"
    p "xxxx"
    p "xxxx"
    p "xxxx"
    p "xxxx"
    p "xxxx"




####################################################
label chapter3_past1_street_distract_SucceedTG:

    scene bg home

    show protagonist neutral at t11
    p "xxxx"
    p "xxxx"
    p "xxxx"
    p "xxxx"
    p "xxxx"
    p "xxxx"




####################################################
label chapter3_past1_office_distract_Outcome:

    scene bg home

    show protagonist neutral at t11
    p "xxxx"
    p "xxxx"
    p "xxxx"
    p "xxxx"
    p "xxxx"
    p "xxxx"

    scene black with Dissolve(1.0)
    n "END OF MISSION 3"
    n "  "
    jump start_chapter4
    #return



####################################################
label chapter3_present_Home_tackleOutcome:

    scene bg home

    show protagonist neutral at t11
    p "xxxx"
    p "xxxx"
    p "xxxx"
    p "xxxx"
    p "xxxx"
    p "xxxx"




####################################################
label chapter3_present_Office_tackleOutcome:

    scene bg home

    show protagonist neutral at t11
    p "xxxx"
    p "xxxx"
    p "xxxx"
    p "xxxx"
    p "xxxx"
    p "xxxx"


    scene black with Dissolve(1.0)
    n "END OF MISSION 3"
    n "  "
    jump start_chapter4
    #return






label chapter3_EXAMPLE:

    scene bg home

    show protagonist neutral at t11
    p "xxxx"
    p "xxxx"
    p "xxxx"
    p "xxxx"
    p "xxxx"
    p "xxxx"
