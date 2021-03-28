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
    e "Position t11."
    show monika happy at t21
    e "Position t21."
    show monika happy at t31
    e "Position t31."
    show monika happy at t22
    e "Position t22."
    show monika happy at t33
    e "Position t33."
    show monika happy at t44
    e "Position t44."

    scene black
    jump start
