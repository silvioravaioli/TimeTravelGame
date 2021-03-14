####################################################
label start_chapter1:
    # play music "funiculifunicula.mp3" fadeout 1       # ADD MUSIC

    # TODO Location - (Home, intention was to use this as a hub in between levels):
    # TODO Open the door, first thing you see is the time god

    scene home
    p "Ah, I'm finally home..."
    g "Whoa you really messed that up! I see you’ve had a bad day."
    g "I have a proposition for you."
    g "Would you like a do over...a chance to undo your mistakes?"

    menu:
        "Ummm... okay":
            jump next_1
        "What are you?":
            g "Interesting question. A rather rude one. But interesting."
        "Haha nice costume. Please leave.":
            g "Interesting."
        "No":
            g "Interesting answer."

    label next_1:
        g "The rules are simple. You go back and complete a task for me, and you can fix your mistake."

    menu:
        "What task?":
            jump next_2
        "Seriously, what are you?":
            jump next_2

    label next_2:
        g "Interesting question. I simply need you to deliver this letter to the coffee shop across the street from your office."

    menu:
        "Let me read it.":
            n "Letter reads: \"Loved the date last night -T\""
        "Okay, sure. I'll do it.":
            jump next_3

    label next_3:
        g "Fantastic. I hope your journey is fruitful."

    scene black
    n "Time God snaps his fingers and you’re transported to one week into the past."

    scene home
    # TODO "1 week ago" fades in and out at corner of screen

    p "So...where should I go?"

    # TODO MAP to choose where to go
    # TODO if cafe is chosen, viewing map, don’t actually arrive at cafe yet
    menu:
        "Cafe":
            jump cafe
        "Office":
            jump office
        "Home":
            jump home_

    label cafe:
        scene cafe
        p "I need to teach my past self how to make coffee, maybe I should send him to deliver the letter instead."
        n "Where do you want to go?"
        menu:
            "Office":
                jump office
            "Cafe":
                jump cafe_2

    label cafe_2:
        p "Ok, who was I supposed to deliver this to? All that’s on here is the address."
        p "Maybe I’ll just leave this on the counter."
        menu:
            "Leave on the table":
                jump end
            "Might as well get some lunch while I’m at it":
                jump cafe_3

    label cafe_3:
        p "Can I get an egg salad sandwich with extra onions, extra pickles, extra garlic?"
        bar "Sure! Would you like to add a cup of coffee to that order? Promotion week, only 25 cents extra"
        p "I'm not actually a coffee person. But hey, sure, why not?"
        bar "Ok, egg salad sandwich with extra onions, extra pickles, extra garlic, and a cup of coffee coming right up!"
        # TODO SHOW [Barista is now standing in front of coffee machine]
        pp "So...that's how you make coffee. Wish I knew that earlier."
        bar "Oh where'd this letter come from?"
        # TODO Barista makes a face
        bar "Leave"
        jump end

    label office:
        scene office
        p "My desk is empty. Looks like he- or I am still on my bathroom break."
        p "Here’s what I'll do...write a delivery message on this letter and put it on my desk"
        n "(Holding letter and pencil)"
        n "Letter is now folded up nicely, with a post-it note on top that reads \"deliver to ___ cafe\" with address"
        n "(Toilet flushes)"
        p "HIDE!"
        n "(moves behind potted plant)"
        # TODO "Your past self reappears"
        # TODO past self confused
        s "What is this?? Hm...maybe it's from the boss. Guess I'll drop it off."
        menu:
            "Follow your past self to the cafe":
                p "Ok I need to see this through."
            "Return to the present":
                g "Nice try. Your job isn't finished yet."
                n "Time God snaps fingers and sends you back to the past"
    label home_:
        scene home
    label end:
        n "END OF CHAPTER 1"
        scene black
    return
