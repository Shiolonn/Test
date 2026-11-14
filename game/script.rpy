# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define I = Character("Ineesha")
define B = Character("Ben")
image bg room = "lamancha.webp"
image bg managerlamancha = "managerlamancha.webp"


# The game starts here.

label start: 
    
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.


    # These display lines of dialogue.

    I "Ben?"
    B "What?"
    I "I like you.."
    B "What...?"

    menu:
        "Bounce Back":
            scene bg room

        "Quit":
            jump managerlamancha

if 'boun'

label managerlamancha:
    scene bg managerlamancha
    "You enter the manager's room."
    return


    # This ends the game.

    return
