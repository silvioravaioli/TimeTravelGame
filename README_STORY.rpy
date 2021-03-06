# BASIC EXAMPLE FOR STORY (DIALOGUES/DESIGN)

    # scene = background image
    scene bg room

    # show = character appears (one character can have several “moods” = sprites)
    # multiple characters can appear on the same page (we just need to place them right/left)
    show god angry

    # These display lines of dialogue [each character can be shown as one single letter].
    g "I am the antagonist of the game!"
    g "I am gonna leave the screen!"

    # hide = remove the character
    hide god

    show protagonist happy
    p "I am the protagonist of the game."
