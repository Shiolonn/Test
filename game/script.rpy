# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define I = ("Ineesha")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.


    # These display lines of dialogue.

    "I" "Ben?"
    "B" "What?"
    "I" "I like you.."
    "B" "What...?"

    “Bounce Back”:
		<Bounce Back>

	“Quit”:
		<Quit>


    # This ends the game.

    return
