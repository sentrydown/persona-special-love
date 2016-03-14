# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"
image bg bedroom = "bedroom.png"
image salt normal = "salt.png"


# Declare characters used by this game.

define e = Character('Eileen', color="#c8ffc8")
define k = Character('Kuki', color="#ff3333")
define zack = Character('Zacko', color="#2653d9")
define wynd = Character('Wynko', color="#4d66b3")
define kev = Character('Kekko', color="#80ff00")
define alk = Character('Alkko', color="#b30000")
define salt = Character('Saltko', color="#ffffff")
define sanv = Character('Sanko', color="#993366")
define maid = Character('Meido', color="#00cc99")
define idol = Character('Geoffko', color="#ff66ff")



# The game starts here.
label start:
    call scene1
    return

label scene1:
    scene bg bedroom
    with fade

    play music "velvet.mp3"
    k "Where the fuck am I."

    show salt normal
    with dissolve
    "Who is that?"

    menu:
        "Boobs":
            jump rightaway
        "Ass":
            jump later

label rightaway:

    salt "Get the fuck out of my way."
    ".:. Bad Ending .:."

    return

label later:

    scene black
    with dissolve
    "And then I went home."
    ".:. Neutral Ending .:."

    return
