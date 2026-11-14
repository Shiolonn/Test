# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define I = Character("Ineesha")
define N = Character("Nia")
image bg room = "lamancha.webp"
image bg managerlamancha = "managerlamancha.webp"


# The game starts here.

label start: 
    
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.


    # These display lines of dialogue.

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

    menu:
        "Bounce Back":
            jump bgroom

        "Quit":
            jump managerlamancha

label bgroom:
    scene bg room
    "You enter the amusement park"
    return

label managerlamancha:
    scene bg managerlamancha
    "You enter the manager's room."
    return



    # This ends the game.

    return
