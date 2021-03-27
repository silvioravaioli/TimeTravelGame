####################################################
label start_testingZone_BACKUP:
    # play music "funiculifunicula.mp3" fadeout 1       # ADD MUSIC
    scene bg restaurant room
    show eileen vhappy
    n "START TESTING ZONE."

    n "This part is currently empty"

    hide eileen
    scene black

    jump start







label start_testingZone:

    show monika serious zorder 2 at t11
    e "Sentence 1."
    show monika happy at t11
    e "Sentence 2."
    show monika at s11
    e "Sentence 1."
    show monika zorder 2 at t11
    e "Sentence 2."
    show monika zorder 1 at thide
    hide monika

    e "Sentence 1."

    show monika happy zorder 2 at t11
    e "Sentence 2."
    show monika happy at t11
    e "Sentence 1."
    show monika happy at t11
    e "Sentence 2."
    show monika happy at t11
    e "Sentence 1."
    show monika happy at t11
    e "Sentence 2."

    scene black
    jump start
