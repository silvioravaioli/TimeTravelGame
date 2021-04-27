####################################################
label start_chapter3:

    # INITIALIZE VARIABLES FOR VISITED PLACES
    $ mission3visited_past1_Cafe = 0
    $ mission3visited_past1_Office = 0


    n "{i}Some days, hours, minutes, and seconds later..."

####################################################
label chapter3_travel1DogSearch_Cafe:

    scene bg office with Dissolve(0.5)

    show boss neutral at t33
    boss "Hey, [protagonist_name]! You busy?"

    show protagonist neutral at t31
    P "Uh... Yeah, a little bit."

    boss "Yeah, sure."
    boss "I need you to take care of my dog."

    P "But I just said-"

    boss "Our dog walker is sick today and there was nobody to take care of little Princess at home"
    boss "And I have back-to-back meetings today, so I need you to take her"

    show dog neutral at t11
    show boss happy
    boss "Be good, little Princess girl ok?"
    show dog happy
    boss "Oh, you’re so cute."
    boss "Look at those eyes."
    show dog neutral
    boss "Oh Princess, you are one adorable girl"
    show dog happy
    boss "I love you! I love you!"

    show protagonist blushing
    p "Uh..."

    show boss angry
    boss "Mind your business!"
    show boss talking
    boss "And take good care of her ok?"
    hide boss

    show protagonist talking
    p "Looks like it’s just you and me, Princess."
    show protagonist happy
    p "Huh, I guess you are kinda cute."
    hide protagonist

    scene black with Dissolve(0.5)
    n "{i}Two hours later"
    scene bg office with Dissolve(0.5)

    show protagonist talking at t11
    p "HA! I finally finished my work. Now, it’s time for my..."
    show protagonist happy
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
    p "Remember when I said you were kinda cute?
    p "Well now I TAKE IT BACK!"
    p "PRINCESS!"
    p "PRINCESS! Princesssss!"
    p "PRINCESS, GIVE ME BACK MY LUNCH"

    show protagonist anxious
    p "Princess?"
    p "Oh... no.... Did I just lose the dog?"
    p "DANG IT!"
    p "Now I gotta go look for her..."
    p "And I’m still hungry."
    p "Where could she have possibly gone?"
    hide protagonist

    menu:
        p "Where could she have possibly gone?"
        "Cafe":
            scene black with Dissolve(0.5)
            label chapter3_travel1DogSearch_Cafe
        "Street":
            scene black with Dissolve(0.5)
            label chapter3_travel1DogSearch_Street
        "Home":
            scene black with Dissolve(0.5)
            label chapter3_travel1DogSearch_Home


####################################################
label chapter3_travel1DogSearch_Street:

    scene bg home with Dissolve(0.5)

    show protagonist neutral at t11
    p "Hmmm... I don’t see the dog here either."
    p "Probably a bad time to order something as well. Princess could have eaten that whole bag by now"
    p "Where could she have possibly gone?"
    hide protagonist

    menu:
        p "Where could she have possibly gone?"
        "Cafe":
            scene black with Dissolve(0.5)
            label chapter3_travel1DogSearch_Cafe
        "Home":
            scene black with Dissolve(0.5)
            label chapter3_travel1DogSearch_Home


####################################################
label chapter3_travel1DogSearch_Home:

    scene bg home with Dissolve(0.5)

    show protagonist hmm at t31
    p "Eh, you usually find stuff where you least expect it. Might as well check home."

    show timegod neutral at t33
    g "Oh hey, it’s you again. Guess I shouldn’t be surprised"

    show timegod laugh
    g "Well, it seems yet again, you’ve had another bad day."

    show protagonist anxious
    p "Was it that obvious? Have you seen a dog in there?"

    g "I have a mission I need completed."

    p "Sounds good, the past is always pretty neat. Would definitely help"

    g "Exquisite. The mission is fairly simple. You have probably seen a poster commemorating the birth date of one of your colleagues on a glass wall near the back of your workplace. The poster is quite out of date and needs to be removed. This needs to be done exactly two weeks ago."
    hide timegod
    hide protagonist

    menu:
	    "Sounds good. You can count on me.":
            show timegod happy at t11
	    "Why two weeks ago?":
            show timegod angry at t11

    g "That beef jerky has been in your backpack for five years. {w}But my task for you {i}needs{\i} to be completed two weeks ago."
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

    scene bg home with Dissolve(0.5)

    show protagonist neutral at t11
    p "xxxx"
    p "xxxx"
    p "xxxx"
    p "xxxx"
    p "xxxx"
    p "xxxx"

    p "Where could she have possibly gone?"
    hide protagonist

    menu:
        p "Where could she have possibly gone?"
        "Cafe":
            scene black with Dissolve(0.5)
            label chapter3_travel1DogSearch_Cafe
        "Street":
            scene black with Dissolve(0.5)
            label chapter3_travel1DogSearch_Street
        "Home":
            scene black with Dissolve(0.5)
            label chapter3_travel1DogSearch_Home





####################################################
label chapter3_past1_Office:

    scene bg home with Dissolve(0.5)

    show protagonist neutral at t11
    p "xxxx"
    p "xxxx"
    p "xxxx"
    p "xxxx"
    p "xxxx"
    p "xxxx"

    menu:
        "Cafe":
            scene black with Dissolve(0.5)
            label chapter3_travel1DogSearch_Cafe
        "Street":
            scene black with Dissolve(0.5)
            label chapter3_travel1DogSearch_Street
        "Home":
            scene black with Dissolve(0.5)
            label chapter3_travel1DogSearch_Home

####################################################
label chapter3_past1_OfficeMissionFail:

    scene bg home with Dissolve(0.5)

    show protagonist neutral at t11
    p "xxxx"
    p "xxxx"
    p "xxxx"
    p "xxxx"
    p "xxxx"
    p "xxxx"

    menu:
        "Cafe":
            scene black with Dissolve(0.5)
            label chapter3_travel1DogSearch_Cafe
        "Street":
            scene black with Dissolve(0.5)
            label chapter3_travel1DogSearch_Street
        "Home":
            scene black with Dissolve(0.5)
            label chapter3_travel1DogSearch_Home


####################################################
label chapter3_past1_OfficeMissionSucc:

    scene bg home with Dissolve(0.5)

    show protagonist neutral at t11
    p "xxxx"
    p "xxxx"
    p "xxxx"
    p "xxxx"
    p "xxxx"
    p "xxxx"

    menu:
        "Cafe":
            scene black with Dissolve(0.5)
            label chapter3_travel1DogSearch_Cafe
        "Street":
            scene black with Dissolve(0.5)
            label chapter3_travel1DogSearch_Street
        "Home":
            scene black with Dissolve(0.5)
            label chapter3_travel1DogSearch_Home


####################################################
label chapter3_past1_Cafe:

    scene bg home

    show protagonist neutral at t11
    p "xxxx"
    p "xxxx"
    p "xxxx"
    p "xxxx"
    p "xxxx"
    p "xxxx"


####################################################
label chapter3_past1_Street:

    scene bg home

    show protagonist neutral at t11
    p "xxxx"
    p "xxxx"
    p "xxxx"
    p "xxxx"
    p "xxxx"
    p "xxxx"


####################################################
label chapter3_past1_Street_tackle:

    scene bg home

    show protagonist neutral at t11
    p "xxxx"
    p "xxxx"
    p "xxxx"
    p "xxxx"
    p "xxxx"
    p "xxxx"



####################################################
label chapter3_past1_Street_distract:

    scene bg home

    show protagonist neutral at t11
    p "xxxx"
    p "xxxx"
    p "xxxx"
    p "xxxx"
    p "xxxx"
    p "xxxx"



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
