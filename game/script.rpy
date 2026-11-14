# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define * = Character("Vampire", color="#830303")
define P = Character("Priest", color="#114351")
image bg room = "lamancha.webp"
image bg managerlamancha = "managerlamancha.webp"
image bg cantomeow = "cantomeow.webp"
image amusement
image bg railway

# The game starts here.

label start: 
    
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.


    # Line of dialogue: our intro

    "A long long time ago…"
    "Vampires feasted on humans in the dark."
    "Years went by as this process repeated over and over." 
    "humans feared vampires more than ever, but one was the cause for a major change in the life of the predator, and the prey."
    "Both parties stepped into the light, paving way for many generations to come."
    "Sick of being feared, the Vampires built a massive sanctuary for themselves, an amusement park, where they could live, alongside humans."
    "And the final piece of the puzzle..."
    "Artifical blood bags were created, allowing vampires to feed and fufill their hunger without harming humans."
    "Life was finally coming together,"
    "But there was one problem..."
    "The artifical blood bags may have fufilled their hunger, but it did not satisfy them."
    "The Vampires were growing restless with unsatisfaction..."

"*" "Another day.. Another act…. I don’t know if I can keep this charade up any longer…
A long time ago, I tried it: human blood, a satisfaction that can be matched by no other, yet every day, I cannot."
"You look at the bright artificial lights in the amusement park that surrounds you,"

label amusement:   
    menu:
        "Will you go on a ride?"

        "Yes":
            jump ride

        "No":
            jump walkaround

label ride:
    menu:
        "Which ride do you want to go on?"

        "Railway Ride":
            jump railwayride

        "Haunted House":
            jump hauntedhouse

label railwayride:
    scene bg railway
    "You enter the railway ride."
    menu:
        'Continue':
            jump continue

        "Go back":
            jump goback

label goback:
    scene amusement
        jump amusement

label no:

    menu: 
        "How do you want to act"

        "Act upon it":
            jump bgroom

        "Ignore it":
            jump managerlamancha

        "Visit the priest":
            jump bgcantomeow


label bgroom:
    scene bg room
    "You enter the amusement park"
    return

label managerlamancha:
    scene bg managerlamancha
    "You enter the manager's room."
    return

label bgcantomeow:
    scene bg cantomeow
    "You enter the church"
    "Priest" "Hello, I am the priest of this church, how may I help you?"
    "Priest" "I can see you are troubled, are you here to confess your sins?"

    menu:
        "How do you respond"
        "Yes.. I am here to confess my sins":
            jump confession

        "No, I am here to seek guidance":
            jump guidance

label confession:
    "Priest" "I see, please tell me what you have done."
    "You confess your sins to the priest."

label guidance: 
    "Priest" "I see, please tell me what troubles you."

    # This ends the game.

    return
