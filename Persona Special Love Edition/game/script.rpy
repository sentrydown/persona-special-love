# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"
image bg bedroom = "img/bedroom.png"
image bg yard = "img/yard.jpg"
image bg roof = "img/roof.png"
image bg cherry = "img/cherry.png"
image salt normal = "img/salt.png"
image alk normal = "img/alk.png"


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
    call opening
    return

label opening:
    scene bg yard
    with fade

    play music "img/newdays.mp3"
    k "What the fuck."
    k "Where the fuck am I going."
    
    menu:
        "Go up to the roof":
            jump roof
        "Go to the courtyard":
            jump courtyard
        "Go find Wynko":
            jump dream

label roof:
    scene bg roof
    with fade
    "I decide to spend my graduation day up on the roof."
    "The view up here is amazing, and to my luck it was a beautiful day outside."
    "As the rusty metal door opens with a creek, I am met with a gentle breeze."
    "The roof was empty with the exception of one --"
    show alk normal at right
    with easeinleft
    "Alkko leans against the fence, gazing below at the students passing by the school entrance."
    "My chest tightens at the thought of not being able to see her next year."
    alk "Ah, Kuki-kun, did you come to check out the view for one last time as well?"
    k "I guess so."
    alk "The past year has been a great experience for me. I’m really going to miss this town."
    "I recall that Alkko-senpai was planning on attending a college in America." 
    "I heard she wanted to become a teacher."
    "Suddenly, Alkko turns around and faces my direction, gazing deep into my eyes."
    alk "Kuki-kun, I love you."
    k "W-what?"
    "Taken aback by the sudden confession, I stare in awe, unable to meet her gaze."
    "What seemed like mere seconds lasted an eternity for me."
    "A gentle breeze rolls in, rustling Alkko’s hair. She brushes it off with her hand."
    "She looks at me, still determined."
    k "I’m… not sure what to say, to be honest. You’ve never said this to me before… so it came as a surprise."
    alk "I may not show it, but that doesn’t mean I’m in love with you."
    "She laughs with a gentle ‘Ufufu’, covering her mouth."
    "Then, as she steps closer, she motorboats the living shit out of me."
    with vpunch
    with hpunch
    "I can’t breathe."
    with hpunch
    with vpunch
    "I’m suffocating"
    with hpunch
    with vpunch
    scene black
    "oh shit fuck im dead"
    with hpunch
    ".:. Good Ending? .:."
    return
    
label courtyard:
    scene bg cherry
    with fade
    "What the fuck are you fucking doing here you fucking moron this isn't implemented yet!"
    return

label dream:
    scene bg bedroom
    with fade
    "I decide to spend my graduation day up on the roof."
    "The view up here is amazing, and to my luck it was a beautiful day outside."
    "As the rusty metal door opens with a creek, I am met with a gentle breeze."
    "The roof was empty with the exception of one --"
    show wynd normal
    with moveinright
    "Wynko leans against the fence, gazing below at the students passing by the school entrance."
    "My chest tightens at the thought of not being able to see her next year."
    wynd "Ah, Kuki-kun, did you come to check out the view for one last time as well?"
    k "I guess so."
    "Hours pass as neither of us say anything. It gets extremely awkward."
    "Suddenly, Wyndko turns around and faces my direction, gazing deep into my eyes."
    wynd "Kuki-kun, I love you."
    k "W-what?"
    "Taken aback by the sudden confession, I stare in awe, unable to meet her gaze."
    "She looks at me, still determined."
    k "I’m… not sure what to say, to be honest. You’ve never said this to me before… so it came as a surprise."
    wynd "I may not show it, but that doesn’t mean I’m in love with you."
    "We're both silent for another couple minutes."
    "It gets extremely awkward."
    "Extremely."
    "Wynko suddenly moves, startling me."
    "She looks into my eyes..."
    "...and then takes a step forward... "
    "...and then another step and then--"
    stop music
    jump good_end

