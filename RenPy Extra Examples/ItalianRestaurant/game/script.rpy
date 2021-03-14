# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Ella",color="#ffcccc")
define y = Character("You",color="#ccccff")

####################################################
# START

label start:
    play music "funiculifunicula.mp3" fadeout 1
    scene bg restaurant room
    show eileen happy

    # HOUSEKEEPING FOR THE WHOLE GAME
    $ dollars_bill = 0   # sum the cost of the meal
    $ number_loops = 1   # count how many times you eat
    $ count_starter = 0  # count the starters
    $ count_pasta   = 0  # count the pastas
    $ count_dessert = 0  # count the desserts

    e "Welcome to the Italian Restaurant."

    show eileen vhappy
    e "Today we have a great selection of Italian starters, pastas, and desserts."





####################################################
# STARTER CHOICE
label starter_choice:
    scene bg restaurant room
    hide eileen
    queue music "funiculifunicula.mp3"

    # HOUSEKEEPING FOR THE LOOP
    $ skip_starter = 0  # set to 1 if you skip the starter
    $ skip_pasta   = 0  # set to 1 if you skip the pasta
    $ skip_dessert = 0  # set to 1 if you skip the dessert

    menu:
        e "What do you want to order as a starter?"
        "delicate caprese":
            jump starter_caprese
        "juicy octopus":
            jump starter_octopus
        "tasty bruschetta":
            jump starter_bruschetta
        "healthy minestrone":
            jump starter_minestrone
        "skip the starter" (disabled=False) if count_starter>1:
            jump starter_skip
        "skip the starter" (disabled=True)  if count_starter<=1:
            jump starter_skip

# CHOICE STARTER CAPRESE
label starter_caprese:
    $ count_starter = count_starter+1
    $ dollars_bill  = dollars_bill+7
    show eileen vhappy
    e "A delicate caprese, excellent choice!"
    hide eileen
    "{i}The caprese melts in your mouth...{/i}"
    jump pasta_choice

# CHOICE STARTER OCTOPUS
label starter_octopus:
    $ count_starter = count_starter+1
    $ dollars_bill  = dollars_bill+11
    show eileen vhappy
    e "A juicy octopus, excellent choice!"
    hide eileen
    "{i}The octopus is cooked perfectly.{/i}"
    jump pasta_choice

# CHOICE STARTER BRUSCHETTA
label starter_bruschetta:
    $ count_starter = count_starter+1
    $ dollars_bill  = dollars_bill+5
    show eileen vhappy
    e "A tasty bruschetta, excellent choice!"
    hide eileen
    "{i}The bruschetta is crunchy and tasty.{/i}"
    jump pasta_choice

# CHOICE STARTER MINESTRONE
label starter_minestrone:
    $ count_starter = count_starter+1
    $ dollars_bill  = dollars_bill+9
    show eileen vhappy
    e "A healthy minestrone, excellent choice!"
    hide eileen
    "{i}The minestrone warms you up in a few seconds.{/i}"
    jump pasta_choice

# CHOICE STARTER SKIP
label starter_skip:
    $ skip_starter = 1
    show eileen concerned
    e "Oh, no starter. I see..."
    hide eileen
    "{i}I already regret not ordering anything.{/i}"
    jump pasta_choice





####################################################
# PASTA CHOICE

label pasta_choice:
    scene bg restaurant room
    show eileen happy
    e "We have so many pasta options!"
    hide eileen

    menu:
        e "What do you want to order as main dish?"
        "carbonara spaghetti":
            jump pasta_spaghetti
        "mushroom risotto":
            jump pasta_risotto
        "cheesy lasagna":
            jump pasta_lasagna
        "beef ragu ravioli":
            jump pasta_ravioli
        "skip the pasta" (disabled=False) if count_pasta>1:
            jump pasta_skip
        "skip the pasta" (disabled=True)  if count_pasta<=1:
            jump pasta_skip

# CHOICE PASTA SPAGHETTI
label pasta_spaghetti:
    $ count_pasta   = count_pasta+1
    $ dollars_bill  = dollars_bill+16
    show eileen vhappy
    e "Carbonara spaghetti - Sounds perfecty!"
    hide eileen
    "{i}The pieces of bacon are hidden in the spaghetti like a treasure.{/i}"
    jump dessert_choice

# CHOICE PASTA RISOTTO
label pasta_risotto:
    $ count_pasta   = count_pasta+1
    $ dollars_bill  = dollars_bill+20
    show eileen vhappy
    e "Mushroom risotto - I like it \"ben cotto\"!"
    hide eileen
    "{i}It is so creamy and balanced, I can really taste the mushrooms!{/i}"
    jump dessert_choice

# CHOICE PASTA LASAGNA
label pasta_lasagna:
    $ count_pasta   = count_pasta+1
    $ dollars_bill  = dollars_bill+14
    show eileen vhappy
    e "Cheesy lasagna - My grandma\'s favorite!"
    hide eileen
    "{i}Cheese and tomato balance each other perfectly...{/i}"
    jump dessert_choice

    # CHOICE PASTA RAVIOLI
label pasta_ravioli:
    $ count_pasta   = count_pasta+1
    $ dollars_bill  = dollars_bill+18
    show eileen vhappy
    e "Beef ragu ravioli - You have good taste!"
    hide eileen
    "{i}I never tried something as delicious as this...{/i}"
    jump dessert_choice

# CHOICE PASTA SKIP
label pasta_skip:
    $ skip_pasta = 1
    show eileen concerned
    e "Oh, no pasta. This hurts..."
    hide eileen
    "{i}I already regret not ordering anything.{/i}"
    jump dessert_choice





####################################################
# DESSERT CHOICE

label dessert_choice:
    scene bg restaurant room
    show eileen happy
    e "We have so many dessert options!"
    hide eileen

    menu:
        e "What do you want to order as dessert?"
        "tiramisu cake":
            jump dessert_tiramisu
        "coconut gelato":
            jump dessert_gelato
        "chocolate mousse":
            jump dessert_mousse
        "cannoli with ricotta":
            jump dessert_cannoli
        "skip the dessert" (disabled=False) if count_dessert>1:
            jump dessert_skip
        "skip the dessert" (disabled=True)  if count_dessert<=1:
            jump dessert_skip

# CHOICE DESSERT TIRAMISU
label dessert_tiramisu:
    $ count_dessert   = count_dessert+1
    $ dollars_bill  = dollars_bill+11
    show eileen vhappy
    e "Tiramisu cake with coffee - Beware, it\'s addictive!"
    hide eileen
    "{i}The spoon cuts the creamy tiramisu, revealing the aroma of coffee.{/i}"
    jump bill_choice

# CHOICE DESSERT GELATO
label dessert_gelato:
    $ count_dessert   = count_dessert+1
    $ dollars_bill  = dollars_bill+5
    show eileen vhappy
    e "Coconut gelato - Don\'t call it ice cream, or I scream!"
    hide eileen
    "{i}I can feel the flavor of the coconut... I want another one now!{/i}"
    jump bill_choice

# CHOICE DESSERT MOUSSE
label dessert_mousse:
    $ count_dessert   = count_dessert+1
    $ dollars_bill  = dollars_bill+9
    show eileen vhappy
    e "Chocolate mousse - In a Canadian restaurant, that would be a chocolate moouse!"
    hide eileen
    "{i}The finest dark chocolate was used for this, you can tell!{/i}"
    jump bill_choice

    # CHOICE DESSERT CANNOLI
label dessert_cannoli:
    $ count_dessert   = count_dessert+1
    $ dollars_bill  = dollars_bill+7
    show eileen vhappy
    e "Cannoli with ricotta - we follow the original recipe from Sicily!"
    hide eileen
    "{i}The cruncy cannoli protects the tender heart of sweet ricotta...{/i}"
    jump bill_choice

# CHOICE DESSERT SKIP
label dessert_skip:
    $ skip_dessert = 1
    show eileen concerned
    e "Oh, so no dessert for you? Life is sweeter when you have a dessert..."
    hide eileen
    "{i}I already regret not ordering anything.{/i}"
    jump bill_choice





####################################################
# BILL CHOICE

label bill_choice:
    scene bg restaurant room
    show eileen vhappy
    e "I am glad you enjoyed this!{p}Are you ready for the check?"
    hide eileen

    menu:
        e "I am glad you enjoyed this!{p}Are you ready for the check?"
        "bring the check" (disabled=False) if number_loops>1:
            jump ending_bill
        "bring the check" (disabled=True) if number_loops==1:
            jump ending_bill
        "eat something else":
            jump more_food


# CHOICE BILL MORE FOOD
label more_food:
    $ number_loops = number_loops+1
    show eileen vhappy
    e "Wow! You REALLY like our recipes!{p}I will be right back with the menu."
    hide eileen
    "{i}I am ready for another round...{\i}"
    jump starter_choice





####################################################
# ENDING BILL
label ending_bill:
    show eileen happy
    if number_loops==2:
        e "Most of our customers do not stop eating until they had the third dessert.{p}But I guess you have never been in Italy before..."
    else:
        e "You must be full! Our kitchen is empty anyways...{p}You ate all the food we had prepared for tonight!"
    hide eileen
    "The waitress leaves the check on the table and leaves."
    "How much  will it be? You open the check."
    "[count_starter] starters. {w}[count_pasta] pastas. {w}[count_dessert] desserts.{p}Total: [dollars_bill] dollars."

    if dollars_bill>100:
        "I was not expecting this to be so expensive..."
        "I have only 100 dollars with me. I cannot pay for it. What should I do?"
        menu:
            "I have only 100 dollars with me. I cannot pay for it. What should I do?"
            "run away without paying":
                jump ending_runaway
            "explain the situation":
                jump ending_apologize
    else:
        "It is even cheaper than I thought..."
        "How much should I give as tip (in percentage)?"
        $ tip_percentage = renpy.input("How much should I give as tip (in percentage)?", "20", allow="0123456789")
        if int(tip_percentage)<20:
            "I hope they don\'t think I am cheap because of the [tip_percentage]\% tip."
            jump ending_lowtip
        else:
            "A [tip_percentage]\% tip seems fair."
            jump ending_fairtip





# ENDING RUNAWAY
label ending_runaway:
    "{i}Nobody is around.{p}That\'s the perfect moment to sneak out...{\i}"
    show eileen concerned
    e "Where are you going???" with vpunch
    e "You cannot afford paying for this?" with hpunch
    e "This means you will pay the debt by cleaning dishes!"
    hide eileen
    "And that\'s how I started working at the Italian Restaurant (and I got a black eye)."
    return

# ENDING APOLOGIZE
label ending_apologize:
    show eileen concerned
    e "You cannot pay for this???{p}This means you will pay the debt by cleaning dishes!"
    hide eileen
    "And that\'s how I started working at the Italian Restaurant."
    return

# ENDING LOW TIP
label ending_lowtip:
    show eileen concerned
    e "Why such a low tip???{p}Is there anything wrong we did today?"
    hide eileen
    "{i}This is so embarassing... I should have tipped more!{\i}"
    "Ehm... nothing wrong, but I cannot afford more today.{p}I will be back after the next stipend and I will give a fair tip."
    "{i}And this is how I became a regular customer of the Italian Restaurant (because of shame).{\i}"
    return

# ENDING FAIR TIP
label ending_fairtip:
    show eileen vhappy
    e "Thank you for the generous tip!{p}Can I offer you some limoncello?{p}It\'s on the house, for our favorite customers!"
    hide eileen
    "{i}The sweet limoncello was the perfect ending for the perfect dinner.{\i}"
    "{i}And this is how I became a regular customer of the Italian Restaurant.{\i}"
    return
