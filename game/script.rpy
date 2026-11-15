# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define V = Character("Vampire", color="#830303")
define P = Character("Priest", color="#114351")
define H = Character("Human", color="#d8caa1")
image bg room = "lamancha.webp"
image bg managerlamancha = "managerlamancha.webp"
image bg cantomeow = "cantomeow.webp"
image aumusement = "amusement.webp"
image railway = "railway.webp"
image church = "church.webp"
default menuset = set()

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

"V" "Another day.. Another act…. I don’t know if I can keep this charade up any longer…
A long time ago, I tried it: human blood, a satisfaction that can be matched by no other, yet every day, I cannot."
"You look at the bright artificial lights in the amusement park that surrounds you,"
"You walk around the amusement park."
label amusement:   
    scene amusement
    menu:
        "Will you visit an attraction?"

        "Yes":
            jump event

        "No":
            jump no

label event:
    menu:
        set menuset
        "Which attraction do you want to visit?"

        "Railway Ride":
            jump railwayride

        "Haunted House":
            jump hauntedhouse

        "Parade":
            jump parade

label railwayride:
    scene railway
    "You enter the railway ride."
    menu:
        'Continue':
            jump continue

        "Go back":
            jump amusement

label continue:
    "You sit on the ride next to a human, they talk to you, friendly. Yet, you still feel an urge"
    "You discuss the events of the amusement park with the human, but your mind is elsewhere."

    menu:
        "A dark thought crosses your mind, will you revert to your old ways, like a bouncing ball that always comes back to the ground?"

        "Commit the sin":
            jump railwaydeath

        "Hold back":
            jump afterrailway

#you teleport to end of railway and go back to options
label afterrailway:
    "You held back your urge and the ride ended."
    jump amusement

label railwaydeath:
    "In the dark of the ride, you feed on the human, and you feel a strong sense of satisfaction, but also a sense of guilt and shame for what you have done."
    jump amusement

label act:
    scene amusement
    "Walking around the park, you see a human. You feel a strong urge to feed on them."
    
    menu:
        "What will you do?"

        "Walk closer to the human":
            jump closer

        "Walk away from the human":
            jump away

label closer:
    "You walk closer to the human, and you feel your hunger grow stronger."
    "You feel a strong urge to feed on them."
    menu:
        "What will you do?"

        "Feed on the human":
            jump feed

        "Control your hunger and walk away":
            jump away
label feed:
    "You feed on the human, and you feel a strong sense of satisfaction, and an overwhelming urge for more"
    "However, you also feel a sense of guilt and shame for what you have done."
    menu:
        "Will you visit the priest to confess your sins?"

        "Yes":
            jump priest

        "No":
            jump no2

label no2:

label away:
    "As you walk away, you think about the consequences of your actions. You feel a sense of guilt and shame for even considering feeding on a human."
    scene amusement
    menu:
        "Will you visit the priest to confess your sins?"

        "Yes":
            jump priest

        "No":
            jump no3

label no3:
    "Your unsatisfaction grows as you walk around the amusement park, looking for something to quench your thirst."
    scene amusement
    menu: 
        "How do you want to act"

        "Act upon it":
            jump act

        "Ignore it":
            jump event

        "Visit the priest":
            jump priest

# label event

label parade:
    scene amusement
    "You walk around the amusement park, and hear a buzz of voices."
    "As walk closer, the voices grow louder, and you hear laughter, and unified voices."
    "As you turn a corner, the source of all the sound reveals itself, a parade of humans and vampires, dancing and singing in unison."
    "You take a moment to watch the parade, and a dark thought crosses your mind, nobody would notice if one of the many humans were to disappear"

    menu:
        "Will you act upon your thoughts?"

        "Yes":
            jump paradedeath
        
        "No":
            jump no3

label paradedeath:
    menu:
        "You think to yourself, are you sure you want to do this?"

        "Yes, go ahead with it":
            jump paradekill

        "No, I will not do it":
            jump no3

label paradekill:
    "You swiftly snatch a human from a parade into a dark alley."
    "Human" "Help! Somebody help me!"
    "You feed on the human, despite their cries, and you feel yourself getting more corrupted"
    jump no3

label hauntedhouse:
    "You enter the haunted house."
    "You walk around the haunted house, and you feel a sense of unease, with dripping running water disrupting your thoughts."
    "As you walk around, you see a human, and you feel a strong urge to feed on them."
    
    menu:
        "What will you do?"

        "Feed on the human":
            jump haunteddeath

        "Control your hunger and walk away":
            jump no3

label haunteddeath:
    "You gain a strong sense of satisfaction, reverting to your old ways"

    menu:
        "Will you visit the priest to confess your sins?"

        "Yes":
            jump priest

        "No":
            jump no3

label priest:
    scene Church
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
    scene Church
    "Priest" "I see, please tell me what you have done. First, how intense is your desire for blood today?"
    menu:
        "One for 'A little'":
            jump one

        "Two for 'A Lot'":
            jump two

        "Three for 'It's driving me insane'":
            jump three



label one:
    "Priest" "I see, this is normal for a vampire. But you still must control your urges."
    "After a discussion, the priest tells you that you must consume artifical blood to control your urges, and that you must not feed on humans again, or there will be consequences."
    jump no3

label two:
    "Priest" "I see, your state is not as bad as it could be. But you still must control your urges."
    "After a discussion, the priest tells you that you must consume artifical blood to control your urges, and that you must not feed on humans again, or there will be consequences."
    jump no3
    
label three:
    "Priest" "I see, you are in a very bad state. I will help you, but you must promise to control your urges and not feed on humans again."
    "Priest" "Have you consumed artifical blood today?"
    "After a discussion, the priest tells you that you must consume artifical blood to control your urges, and that you must not feed on humans again, or there will be consequences."
    jump no3

    

label guidance: 
    "Priest" "I see, please tell me what troubles you."

    # This ends the game.

    return
