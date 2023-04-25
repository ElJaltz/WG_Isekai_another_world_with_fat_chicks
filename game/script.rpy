# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define a = Character("Aria", color="#6b42d1", ctc="ctc_anchored", ctc_position="fixed")
define n = Character("Nora", color="#ffcb8f", ctc="ctc_anchored", ctc_position="fixed")
define k = Character("Kaiya", color="#478c45", ctc="ctc_anchored", ctc_position="fixed")
define b = Character("Beruka", color="#c16d87", ctc="ctc_anchored", ctc_position="fixed")
define v = Character("Vira" )
define s = Character("Shinigami", color="#eb2f2f", ctc="ctc_anchored", ctc_position="fixed")
define d = Character("Demon", color="#cf4047", ctc="ctc_anchored", ctc_position="fixed")
define u = Character("[name]")
define t = Character("Aisha", color="#40cfc1", ctc="ctc_anchored", ctc_position="fixed")
define v = Character("Vira")

define fadehold = Fade(0.5, 1.0, 0.5)
define flashhold = Fade(0.5, 1.0, 0.5, color="#fff")
define flash = Fade(0.1, 0.0, 0.5, color="#fff")
define redout = Fade(0.5, 1.0, 0.5, color="#8B0000")

default galleryList = ["bg city","bg tavern", "bg hell", "bg bedroom"]
default Lightbox_image = ""

default female = False
default shokupanfemale = False
default nb = False
default rest = False
default submissivep = False
default assman = False


# The game starts here.
label splashscreen:

    $ renpy.movie_cutscene('')
    

    return


label start:


    scene bg room
    with fadehold

    

    # These display lines of dialogue.

    "Disclaimer! This game is intended for those who are 18+ or older!"

    show shinigami neutral
    s "This is a fetish game containing NSFW content, fat chicks, suggestive dialogue, fat chicks, and mature themes."
    s "And fat chicks."
    s "Before this story can begin, I’ll need to ask a few simple questions about you. Is that alright?"
    s "I apologize if this is a personal question, but I’d simply like to know your pronouns."

    menu:
        s "So, could you tell me your gender and preferred pronouns?"

        "Male, he/him.":
            jump male

        "Female, she/her.":
            jump female

        "Nonbinary, just use they/them.":
            jump enby

    label male:
        scene bg room
        show shinigami neutral
        s "Not all that surprising, have you ever TRIED using Feabie?"
        s "This community is a sausage fest, and not the delicious kind."
        s "Well unless you're into that, which, like, fair play to you then."
        s "But thanks for the support anyway!"
        jump question3

    label female:
        $ female = True
        $ shokupanfemale = True
        scene bg room
        show shinigami neutral
        s "Right on! Thanks for the support!."
        s "I sure hope you're into other chicks..."
        s "Otherwise I have bad news about the content of this video game."
        jump question3

    label enby:
        $ nb = True
        scene bg room
        show shinigami neutral
        s "Right on! Thanks for the support!"
        s "Though I do have one more question for you, if that's okay."
        jump question2

    label question2:
        scene bg room
        show shinigami neutral
        s "Your player character will have pretty limited appearances, what for the purpose of self-inserting and all."
        s "That being said, they may make appearances in certain scenes."
        s "Our resources are limited, so we've only got two main designs for our intrepid hero."
        s "Which of these two appearances would you prefer for your character to have?"
        show shokupanM
        s "This design, with shorter hair and a more scrawny build?"
        hide shokupanM
        show shokupanF
        s "Or this design here, with longer hair and... assets"
        
        menu:
            s "So, ahem, which do you prefer to play as?"

            "The first design, with shorter hair.":
                jump question3

            "The second design, with longer hair and honky honkers.":
                $ shokupanfemale = True
                jump question3
            
    label question3:
        scene bg room
        show shinigami neutral
        s "Thank you for your answer, it helps a lot with the writing process."

        s "You’ll be entering the world of a dumb fetishy Isekai in just a moment, inserted into a milk-toast protagonist that YOU can live vicariously through."

        s "With that spiel out of the way, one final question..."
        python:
            name = renpy.input("Please type your name below:", length=16)
            name = name.strip() or "Shokupan"

        s "So, that's your name? [name]?"

        s "Is it too cliché of me to say that that is an “interesting” or “weird” name, despite having no way of knowing what name you typed?"

        s "Oh well, this game is half-satire and half-cliches as-is."

        s "Please note! This is a very early version of the game! Writing, art, and basically everything is subject to change!"

        s "Even yours truly could be edited, changed drastically, or removed entirely!"

        s "I hope Muffin and Jaltz don't delete me, though. I quite like existing."

        s "Most art you see right now is broken and scattered, needs to be reworked or resized for this project, or is a placeholder asset."

        s "Despite the tremendous talent of our main artist, Jaltz."

        s "Disregard most of it for now, though, please."

        s "Oh! Also, we'll be adding sound effects and music hopefully! Bets are off if we can afford voice acting, though."

        s "Whatever, it’s time for your amazing adventure to begin!"

        s "You… you might want to close your eyes for this part."

        scene bg crash
        with hpunch

        u "Ahhhh!"

        scene bg heaven
        with fadehold

        show shinigami neutral

        s "Greetings mortal, it is my unfortunate duty to report that you have passed away!"

        s "Rather violently, at that."

        s "Sorry dude, RIP."

        s "Ahem, Yeah, uh..."
        
        s "I’m sorry to report that your time in the world of the living is up… in THAT world, I mean."

        s "For you see, you have been given the chance for a second life!" 
        
        s "Not in your previous world, THAT You is super-mega-dead."
        
        s "But you can live on in a world of magic!"
        
        s "A world of elves, swords, dragons and kingdoms! Where you have the potential to be its greatest hero, villain, or supporting character!"

        s "You’ll have all your previous memories and your previous body, but you’ll be completely cut off from your old life."
        
        s "Ya know, cuz the old you died and you're in another world entirely."
        
        s "And you'll be thrust into the dangers and pleasures of a new one!"

        s "Alternatively, I can just weigh your sins now and send you off to Heaven or Hell, if you’d like to just pass on."

    menu:
        s "So, what'll it be?"
        "I'd like a second chance at life!":
            jump isekai

        "Just let me die in peace.":
            jump rest


    label rest:
        $ rest = True
        scene bg heaven
        show shinigami surprised

        s "Oh, shit, really? Uh, okay then."
        s "Lemme just tally up your sinful thoughts, words, and actions throughout your life..."
        s "This isn't looking too good. Apparently, you've consumed a metric ton of weight gain fetish porn."
        s "I can't even comprehend how much time you've spent playing weight gain fetish games even..."
        s "I like a chubby gal as much as the next goddess, but the big dude upstairs has a no tolernace policy on coomer entrances."
        s "So, it's off to eternal damnation!"
        s "Sorry."
        s "It was nice meeting you though! I'll come visit you in Hell sometime! Maybe..."

        scene bg hell
        with redout

        u "I fucked up."

        "{b}Worst Ending Possible.{/b}"

        show demon

        d "Sup? Welcome to Hell."
        d "I'm a demon."
        d "I'm gonna eat you by the way." 
        d "Swallow you whole... feet first, probably."
        d "Not that I'm into feet or anything, it's just easier for me, I guess."
        d "But first uhhh...."
        d "you wanna have sex or something?"
        d "That usually works up my appetite."
        d "It's gonna be like some mind-breaking cosmic horror-level pleasure sex though."
        d "Since I'm a demon."
        d "Oh and tomorrow you'll be reborn, fully healed."
        d "So you can suffer it all again for eternity."
        d "Unless you're into this, I guess."
        d "I'm good with it either way. Dating in Hell is literally the worst."

        "{b}Worst Ending Possible?{/b}"

    return

    label isekai:
        scene bg heaven
        show shinigami neutral
        s "Great, I was hoping you’d say that!"

        s "To be honest, I wasn't sure if you'd make it to the big house up top or not."

        s "I mean, you selflessly sacrificed yourself to push that girl out of the way of that truck..."

        s "But it kinda looked like you were just staring at her ass and got hit accidentally."

        scene bg crash
        with dissolve

        u "Oof! Sorry about bumping into you! I uh wasn't paying attention because..."
        
        u "{i}Oh, she can't hear me with those airpods in...{/i}"

        u "{i}Though it didn't feel too bad, with all that extra padding back there...{/i}"

        u "{i}Wait what's that sound?{/i}"

        u "IS THAT A FUCKING SEMI TR-"

        scene bg heaven
        with dissolve

        show shinigami neutral
        
        u "Oh yeah… that’s what happened to me"

        s "Regardless of your motives, your selfless deed lead to your death."
        
        s "Thus earning you the Afterlife's Isekai package."

        s "Yeah, I picked that name. I'm really into Re: Zero right now..."

    menu:
        s "Any other questions before you’re sent off into another world?"

        "What is an isekai? I'm just going into some fantasy world, leaving my friends and family forever? Is this some kind of weeb thing?":
            jump weebout

        "Oh man, I'm getting Isekai'd??? This is awesome! Reminds me of Konosuba!":
            jump weebin

        "Isn't this a fetish game? When does the weird kinky shit start? I wanna see some fat chicks!":
            jump shinifatty

    label weebout:
        scene bg heaven
        show annoyed shinigami
        s "Are you deadass? Have you never seen anime or something?"
        s "Fucking cringe!" 
        s "I hate normies. I hate normies. I hate normies. I hate normies. I hate normies. I hate normies. I hate normies. I hate normies. I hate normies. I hate normies. I hate normies. I hate normies."
        s "Whatever, you'll pick it up eventually..."
        jump adventure
        
    label weebin:
        scene bg heaven
        show annoyed shinigami
        s "Niiiice! That's the spirit, dude!"
        s "Thought I'm not a big Konosuba fan, myself."
        s "That goddess is such a bitch, and a total airhead..."
        s "So unrealistic."
        jump adventure

    label shinifatty:
        scene bg heaven
        show shinigami annoyed

        s "Yeah, yeah, don't get your panties in a twist."

        hide shinigami annoyed
        show shinigami belly

        s "There, here's your first chubby tummy scene, you happy?"
        s "Press H to hide the Ui for a bit, then take a screenshot why don't you!"
        s "It'll last longer."
        hide shinigami belly
        show shinigami annoyed

        s "The nerve of some people..."

        jump adventure


    label adventure:
        scene bg heaven
        show shinigami excited
        s "Now then, your adventure is about to begin! Goodbye and good luck!"

        scene bg black
        with fade

        a "Ooh oh my god, did it just move?"

        n "Shhh, be quiet Aria!"

        scene bg fields
        with flashhold

        show aria excited at left

        a "Welcome to our world! Aren't you just the coolest thing? Did you come through a portal on your end? Were you ascended up in a pillar of light? Were you completely de-atomized and reassembled here instantly? Ooh ooh what if you fell from the sky like a falling star? Maybe you can open rifts by tearing holes in reali-"

        show nora annoyed at right

        n "Aria, give our guest a moment to breathe!"

        n "I'm so verysorry about her." 

        hide nora annoyed
        show nora neutral at right 

        n "Are you alright?"
        n "I assume you may be a bit confused about all this... other world talk..."
        n "I know I sure am..."

        a "Our world has been ravaged by the vicious demon king for centuries. He and his army of monsters rule this world with a deadly iron fist!"
        a "Man and monster have been locked in war for centuries, as the demon king threatens to take more and more of our lands!"
        a "No hero alone has been been powerful enough to stop him, most died tragically against lower-level monsters when they tried fighting alone." 
        a "So, heroes have been forming parties to work together to stop him and save the world!"

        hide aria excited
        show aria frustrated
        a "However, our party, like every other party we've ever met, is still too weak to survive most monsters, let alone the demon king!"

        hide aria frustrated
        show aria excited
        a "So, I decided we needed a super weapon, to boost our party up by 1 Million Levels!"
        a "I heard stories about this library full of summoning rituals, all about extradimensional entities with world-changing power!"
        a "So we broke into it!"

        n "I begged her not to, for the record."
        n "I didn't even go along, she literally went by herself..."

        a "Anyway, in one of the books, I found a prophecy about a legendary hero born in another world, ascended to the beyond after a brave and noble death! When the hero was summoned to our world, they would be ready to face the ultimate evil!"
        a  "So, naturally, I followed the guide in the text, creating a summoning circle that breached a hole in our reality, bringing you into our plane of existence!"
        a "I might have also burnt my fingerprints off in the process, oops!"

        hide aria excited
        show aria smug at left

        a "TL;DR, I summoned you using a weird ritual I found in an old book! And you're probably the savior of the world or something!"

        hide nora neutral
        show nora annoyed at right

        n "Despite me repeatedly warning her that summoning a powerful being from another world could be a stupid and foolish idea!"
        
        hide nora annoyed
        show nora embarassed at right

        n "Um, no offense! You seem lovely so far..."

        hide aria smug at left
        show aria excited at left

        a "BUT! Since you're here anyway, you can help us slay the demon king! Ooh, and you can meet our friends!"

        u "I might be a little overwhelmed here... who are you people?"

        n "How could we forget to introduce ourselves! I'm so sorry!"

        hide aria excited
        show aria neutral at left
        hide nora embarassed
        show nora neutral at right

        n "My name is Nora. I'm a cleric of the Church of the West, a servant to the beneveloent goddess."

        a "My name is Dr. Aria Lomanteau, but you can just call me Aria."

        hide aria neutral
        show aria annoyed at left

        a "And yes, I DO have a doctorate! I'm a mage, researcher, and scientist from the mage's academy."

        a "And I'd be a professor too if those cowards trusted me to teach a class..."

        u "I didn't even say anything!"

        u "But, uh, my name is [name]."

        hide aria annoyed
        show aria excited at left

        a "What a peculiar name! You're definetly not from around here."

        n "Well I think it's a lovely name, [name]. It is wonderful to meet you."

        u "Thank you, I really appreciate the warm welcome. What was that about meeting your friends though?"

        n "Ah, yes. Aria was just mentioning-"

        a "The other two assholes that make up our party! The four of us are unstoppable at fighting household rats and causing minor-to-major property damage!"

        hide nora neutral
        show nora nervous at right

        n "Which might explain why Aria desperately wanted to recruit an extra-dimensional MVP to our party."

        u "Fair enough, I guess."

        n "It’s rude to talk about our friends so much without them being here, and to try to drag you into our party without meeting everyone else."

        hide nora nervous
        show nora excited at right

        n "Let’s get going back to town!"

        a "You’re gonna love it! It’s seems like a quaint town at first, but something is always happening to liven the pace up!"

        hide aria excited
        show aria evil at left

        a "But if nothing happens for a while, we can find a condemned building or something and blow it up!"

        hide nora excited
        show nora tired at right

        n "It’s a wonder no one ever hires us."

        u "{i}So, this was the start of my new life, huh?{/i}"
        
        u "{i}Being woken up in a field by two beautiful, if a little quirky, women? Drafted into a failing adventure party to help them on quests, despite my lack of any noteworthy skills or experience?{/i}"

        u "{i}Maybe I know magic, already, and haven’t realized it yet? Or I’ll pick up a sword or bow and be a natural prodigy?{/i}"

        s "{i}No, you’re not the greatest mage or warrior that has ever lived. Not without training at least{/i}."

        show shinigami neutral

        u "Ahh! Shinigami? What’re you doing here? Can you hear my thoughts?"

        hide nora tired
        show nora concerned at right

        n "Are you alright? You’re yelling... odd things at thin air, [name]..."

        show aria excited at left

        a "Is this some kind of psychosis brought on by the cosmic travel among dimensions? Or are you communicating with some kind of being only you can percieve here? Fascinating!"

        s "{i}The shortstack redhead is basically right, only you can see or hear me right now.{/i}"
        
        s "{i}So, just think instead of talking, because, yes, I can read your thoughts, and you’ll look crazy if you talk to empty space all the time.{/i}"

        menu:
            u "{i}Great... so, I've got a...{/i}"

            "smoking hot goddess in my head?":
                jump hotdeath

            "snarky goddess in my head?":
                jump rudedeath

            "adorable girl in my head?":
                jump cutedeath



    label hotdeath:
        hide shinigami neutral
        show shinigami smug

        s "{i}You’re damn right that I’m smoking hot!{/i}"
        s "{i}Thanks though!{/i}"
        s "{i}I always appreciate a bit of worship, being a goddess and all.{/i}"

        jump fantasyshow

    label rudedeath:
        hide shinigami neutral
        show shinigami annoyed

        s "{i}Watch who you call snarky buster! I could smite you with a single thought.{/i}"

        s "{i}But whatever, at least you’re honest.{/i}"

        jump fantasyshow

    label cutedeath:
        hide shinigami neutral
        show shinigami shy

        s "{i}Adorable??{/i}"
        
        s "{i}I’m not c-cute! I’m a sexy and terrifying goddess of death and desire!{/i}"

        hide shinigami shy

        show shinigami angry

        s "{i}I break kings and kingdoms, and I make proud warriors beg for mercy! I reap souls and judge the damned!{/i}"

        s "{i}W-whatever!{/i}"

        hide shinigami angry

        show shinigami shy

        s "{i}Thank you, though.{/i}"

        jump fantasyshow

    label fantasyshow:

        scene bg fields
        show shinigami excited

        s "{i}Back to my new favorite fantasy show, you’re almost to town!{/i}"

        s "{i}See you around cutie! Try not to get killed in the Prologue!{/i}"

        hide shinigami excited

        u "{i}I guess she’s leaving... somehow? She’s never a boring conversation partner at least.{/i}"

        show nora concerned at right

        n "Excuse me, [name]..."

        show aria annoyed at left

        a "Get your head out of those dimensional clouds and pay attention! We’re here!"

        scene bg city
        with dissolve

        u "Woah!"

        u "{i}This place is huge… I expected a quaint little village since I’m just at the start of this adventure, but this is a sizable city!{/i}"

        u "{i}Just from the entrance, here, I can see a dozen or so shops, a few bars and taverns, a sizable cathedral, and a huge castle just a few miles ahead.{/i}"

        u "{i}They've even got a postal system here!{/i}"

        show nora excited at right

        n "Welcome, to Middriff, the capital city of Adiposia!"

        n "The political, economic, and religious hub of the entire kingdom!"

        show aria neutral at left

        a "And home of the Eastern branch of the Adventurer’s Guild!"

        hide aria neutral
        show aria smug at left

        a "That’s the group that pays us to blow stuff up."

        hide nora excited
        show nora neutral at right

        n "There’s a lot to take in, I know, but before we give you the grand tour..."
        n "How about we introduce you to the rest of our team?"

        hide aria smug
        show aria excited at left

        a "You’ll like them, probably!"

        hide aria excited
        show aria thinking at left

        a "Though Kaiya might try to kill you or something."

        u "Kaiya might what now?"

        hide nora neutral
        show nora nervous at right

        n "Oh, don’t mind her! Kaiya’s just a bit… antisocial, at times. Shy, even. It’ll be fine!"
        n "Trust me, she's a sweetheart!"
        n "Well, usally. Unless she's in a bad mood. Or nervous. Or self-conscious. Or tired."
        n "She might try to kill you."

        hide nora nervous
        hide aria thinking

        u "{i}Putting my worries about being killed, again, aside, we approached a rustic tavern & inn with an inviting sign, depicting a plush feminine figure.{/i}"

        u "The Hefty Queen? Really?"

        show shinigami neutral

        s "{i}Hey, I think it's a pretty good name for a fantasy tavern! It's got the whole adjective-noun combo thing from Skyrim! And modern Britain for some reason...{/i}"

        hide shinigami neutral
        show shinigami annoyed

        s "{i}So shut your mouth and appreciate all the consideration that is going into appeasing your weird kinks in your magical fantasy adventure!{/i}"

        hide shinigami annoyed

        u "{i}That aside, the Queen was a comfortable and inviting-looking place... Which made me wonder how we could afford it.{/i}"

        scene bg tavern
        with move

        u "{i}It wasn’t brand new and sparkling or anything, but the place was warm and home-y, with drunkards singing and drinking by the bar, as beautiful barmaids serve drinks.{/i}"

        show aisha neutral

        t "Oh! Lady Nora! Miss Aria!"

        show aria annoyed at left

        a "Doctor."

        a "It’s Dr. Aria."

        hide aisha neutral
        show aisha nervous

        t "My mistake! I’m sorry miss!"

        hide aisha nervous
        show aisha scared

        t "Er- doctor! I'm sorry! EEP!"

        hide aria annoyed
        show aria neutral at left

        a "It's fine."

        hide aisha nervous
        show aisha confused

        t "And hello to you, uh, whatever your name is."

        show nora neutral at right

        n "This is [name]."

        a "I summoned them from another dimension or space or heaven or something."

        t "Well…"

        hide aisha confused
        show aisha nervous

        t "I hope our humble tavern is accommodating enough to someone of your unknown… origin."

        u "I’m still human, you know. Don't worry too much."

        u "As long as you’ve got cold drinks, hot food, good conversations, and a warm bed, I’ll be fine."

        hide asiha nervous
        show aisha excited

        t "What about hot drinks and cold food?"

        hide aisha excited
        show aisha nervous

        t "Sorry, bit of um, uh, tavern... humor."

        hide aisha nervous
        show aisha neutral

        t "Well we can happily provide the drinks, food, and the bed! For a price, as usual."

        t "And… I hope I can provide that good conversation for someone as..."

        hide aisha excited
        hide nora neutral
        hide aria neutral
        show aisha flirt

        t "Mysterious and charming as you..."

        show aria smug at left

        a "Speaking of warm bed!"

        hide aisha flirt
        show aisha scared

        t "Eep!"

        hide aria smug
        show aria neutral

        a "Our friend here will be bunking with us, as a new member of our party."

        u "I will be?"

        hide aisha scared
        show aisha excited

        t "A new party member! That’s so exciting!"

        hide aisha excited
        show aisha frustrated

        t "Off saving the world… fighting monsters… rescuing pretty girls... bathing in adoration and fangirls..."

        hide aisha frustrated
        show aisha nervous

        t "Um, uh, anyway!"

        t "I’ll go get a room key for you then, [name], so you can go home without having to wait for the girls to let you inside."

        hide aisha nervous
        show aisha neutral

        t "Let me go get the boss."

        hide aisha neutral
        show nora happy at right

        n "She’s so adorable when she’s flustered. Such a sweet girl."
        hide aria neutral
        show aria smug at left

        a "That little bird is crushing hard, and you’ve only been here five minutes. Nice!"

        hide aria smug
        show aria thinking at left

        menu:
            a "You better not be some interdimensional pervert sent here to seduce us all and devastate our world."

            "That’s literally exactly what I am":
                jump spaceperv

            "I’ve actually never been all that good with the... um... ladies":
                jump sykkuno

            "You know me, absolute pussy destroyer!":
                jump eww

    label spaceperv:
        hide nora neutral
        show nora concerned at right
        n "Good heavens! I hope you’re joking…"

        hide aria annoyed
        show aria excited at left

        a "I hope you’re not. I wanna see some otherworldly chaos! What kind of sick and twisted thoughts lay in that cosmic cranium of yours?"

        u "Rude, hurtful even."

        a "Debauch-away o' mighty Chaos God!"

        n "Goddess guide her..."
        jump innkeeper
        
        
    label sykkuno:
        hide aria thinking
        hide Nora happy
        show aria seductive

        a "Aww, got a little cutie on our hands! A ladykiller in the making? Well, I can give you some... experience."
        
        hide aria seductive
        show aria laughing
        a "Sorry, I am legally obligated to tease you, often. It's my nature."

        show nora neutral
        n "I for one respect your choices of celibacy and encourage you to continue this path, if it is what you choose to do."
        
        hide nora neutral
        show nora hug
        n "But if you ever need a cuddle buddy, you know where to find me."
        jump innkeeper 


    label eww:
        hide aria annoyed
        show aria disgusted at left
        a "I believe you, ugh."
        a "Please never call yourself that again"

        hide nora neutral
        show nora disgusted at right

        n "I’m… inclined to agree."

        hide nora disgusted
        show nora neutral at right

        n "Don’t worry! You’ll find a girl who accepts you, despite the wretch you are!"

        hide nora sweet
        show nora tired at right

        n "Despite your flaws."

        show shinigami neutral

        s "For the record, I say shit like that all the time! Babes love that stuff!"

        hide shinigami neutral
        show shinigami embarassed

        s "Granted, I say the word \"babes\" unironically, so..."

        hide shinigami embarassed
        show shinigami excited

        s "Oh well!"
        hide shinigami excited
        jump innkeeper

    label innkeeper:
        scene bg tavern2
        with dissolve
        v "Would you two ladies back-off the newbie long enough for me to get a look at them?"

        show vira annoyed

        u "{i}Oh wow… if the girl before was cute, this lady is… gorgeous.{/i}"

        u "{i}Terrifyingly beautiful, like a goddess, your friend's hot mom, and a legendary warrior all rolled into one chick.{/i}"

        u "{i}She could definetly kick my ass, and I’d probably thank her.{/i}"

        hide vira annoyed
        show vira motherly

        v "Well, aren’t you a cute little thing? Aisha said your name was, [name], right?"

        v "Nice to make your acquaintance. I hear you’re our \"visitor from beyond the stars.\""

        u "Something to that effect, yeah, that's an Aria way of explaining it..."

        v "I like your attitude, kiddo."

        hide vira motherly
        show vira neutral

        v "Anyone who can roll with Aria's antics is a respectful enough soul for me to trust, at least a little bit."

        show aria annoyed at left
        a "Standing right here, by the way."
        hide aria annoyed
    
        v "Welcome to the Hefty Queen family."

        v "The name's Vira."

        v "And no, I’m not the Queen from the name."

        hide vira neutral
        show vira belly

        v "Though I guess i do match the Hefty part, I guess ha ha!"

        "{i}You watch as Vira gives her plush beer belly a playful pat, the exposed flesh jiggling for a few solid seconds.{/i}"

        u "{i}Please tell me there's a Vira route, Shinigami.{/i}"

        show shinigami smug at left

        s "{i}Don’t worry, even some of the supporting cast have pretty big roles in the game.{/i}"

        hide shinigami smug
        show shinigami embarassed

        s "{i}I mean world!{/i}"

        hide shinigami embarassed

        u "Thanks! It’s really nice to meet you too."

        hide vira belly

        show vira serious

        v "Make no mistake, however."

        v "You slip up, once, you hurt these girls, or heaven forbid you hurt my girls like little Aisha, or otherwise take advantage of our good will, and you’ll learn what this “Heft” and two decades of brawling, boxing, and mixed-martial arts can do to a human skull."
        
        v "Got it?"
        
        u "Yes ma’m!"

        hide vira serious
        show vira happy
        v "Good lad! Keep on the straight and narrow, hun, and we’ll get along fine."

        hide vira happy
        show vira neutral

        v "I’ve got to get back to work, but I look forward to spending more time getting to know my newest customer."

        v "Need any drinks, food, or gossip? Just find me or one of the girls."

        v "Enjoy your stay!"
        hide vira neutral
        jump theothers

    label theothers:
        scene bg tavern
        with dissolve
        show aria neutral at left

        a "Well, you’ve certainly made an impression on Ms. Vira."

        show nora neutral at right

        n "She’s been very kind to us…"

        hide aria neutral
        show aria smug at left

        a "Despite our constant failures, late rent, and property damage-"

        hide nora neutral
        show nora tired at right

        n "So please, try to give her as much respect as you can."

        hide aria smug
        show aria excited at left

        a "Now, without any further ado, let’s get back to our room so we can show off our new pet to the girls!"

        hide nora tired
        show nora annoyed at right

        n "Our new FRIEND, you mean, right, Aria?"

        a "Yeah, yeah, that’s what I said!"

        hide aria excited
        show aria smug

        a "I'll get you some treats when we get inside, okay?"

        hide nora annoyed
        show nora hungry

        n "Ooh I hope its butterscotch!"

        u "{i}These girls are insane, right?{/i}"

        u "{i}With how chaotic, quirky, and smoking hot Aria and Nora are, I can only imagine what sexy nightmare I’m about to walk into.{/i}"
        jump meetkaiya

    label meetkaiya:

        scene bg bedroom

        show kaiya annoyed at left

        show beruka neutral at right

        b "You don’t even care about how you look half-the-time, why is this bugging you so much?"

        b "Kai, you literally turn invisible and can disguise yourself as other people."

        k "I’m just saying, Bee."
        
        k "It’s not fair that I’m still so… small."

        k "You’re built like a brick shithouse and even you have more fat on your tits than I do."

        hide kaiya annoyed
        show kaiya butt at left

        k "It just all goes to my big fat bu-"

        u "{i}My life fucking rules.{/i}"

        s "{i}Correction, your afterlife \"fucking rules\" and I made it, so you’re welcome, by the way.{i}"

        hide kaiya butt
        show kaiya panic at left
        with vpunch
        k "Kyaaaaaah!"

        hide kaiya panic
        show kaiya angry at left

        k "Who are you and how much did you hear?"

        show aria excited

        a "I summoned them from an extradimensional plane! They’re gonna help us kick demon ass! They're the harbinger of the end and the ultimate hero!"

        hide aria excited

        show nora neutral

        n "This is our new roommate and teammate, [name], and they appear to have come from another world."

        menu:

            n "Well, go on, say something [name]!"

            "Uh hi! I’m [name] and I hope we can work well together!":
                jump polite

            "Yeah, I’m [name], and I’m ready to kick some demon ass!":
                jump toughguy

            "For the record, tits are overrated. Big fat asses are way better!":
                jump flirtkaiya

    label polite:
        hide nora neutral
        show beruka happy at right
        b "Aww, well aren’t you a polite little thing?"

        hide kaiya angry
        show kaiya annoyed at left

        k "If you were polite, you would have KNOCKED before entering!"

        show nora concerned

        n "Fair point, but that’s on us, apologies Kai."

        hide nora concerned
        show nora smug

        a "I regret nothing. Our friend would have to see your big fat butt being weird and huge eventually."
        
        hide kaiya annoyed
        show kaiya angry
        k "Shut it, red dwarf!"

        hide aria smug
        show kaiya annoyed

        u "I'm real sorry about that, but I hope we can still get off on the right foot?"

        hide beruka happy
        show beruka neutral at right

        b "Oh, you’re alright sweetheart!"

        b "Welcome to the team, I’m Beruka!"

        hide kaiya annoyed
        show kaiya neutral at left

        k "You’re on thin ice, but I can tolerate you for the good of the party. I'm Kaiya."
        jump tourtime

    label toughguy:
        hide nora neutral
        hide kaiya angry
        show beruka excited at right
        b "I respect that attitude! I’m Beruka, and we’re gonna be good pals I think. "

        b "I expect to see that cute butt on the training field for an ass whooping ASAP!"

        show aria excited

        a "Ooh this is gonna be good! Blast her with your umbral rays! Show her the might of the infinite galaxies! Let her know how strong you really are!"

        show kaiya annoyed at left

        k "Great, another idiot to add to my collection."

        hide beruka excited
        show beruka tired

        b "Lay off Kaiya, give them a chance!"

        hide kaiya annoyed
        show kaiya neutral

        k "Fine, but you're on thin ice, newbie."
        jump tourtime

    label flirtkaiya:
        $ assman = True
        hide nora neutral
        hide kaiya angry
        show kaiya shocked at left
        k "What??"
        hide kaiya shocked
        show kaiya angry at left
        k "How dare you say that to me! Fuck you! P-pervert! Weirdo! Freak! Peeping Tom! Don't ever talk about my butt!"
        show kaiya shy at left
        k "Not that that’s what we were talking about! Pervert!"
        hide beruka neutral
        show beruka excited at right

        b "Fortune favors the bold kiddo, but I'm not sure if Kaiya does."

        b "Regardless, I’m Beruka, nice to meetcha."

        hide kaiya shy
        show kaiya annoyed at left

        k "Everyone shut up, oh my god this is Hell."

        k "I'm Kaiya, you're all the worst, now let's move on."
        jump tourtime

    label tourtime:
        scene bg bedroom
        show berukahappy
        b "Kai’s shit at talking feelings and stuff, just give her time to get comfortable with you."
        b "But otherwise, welcome to the team, [name]!"

        show kaiya neutral at left

        k "Yeah, yeah, friendship wins, can I go for a walk now?"

        hide kaiya neutral
        show kaiya tired at left

        k "Need to walk this headache off in the woods."

        show nora neutral

        n "Well, we were hoping you two would help us take our recruit on a tour of the city"

        show aria annoyed at right

        a "If the first being I ever summon dies because they can’t find the markets, I’ll probably have to retire as a summoner."

        hide kaiya tired
        show kaiya annoyed at left

        k "Fiiine! Ugh, I cannot stand any of you. The deer never drag me into stupid stuff like this..."

        hide aria annoyed
        show aria smug at right

        a "Love you too, Kai."

        hide kaiya annoyed
        show beruka excited at left

        b "You can count me in! I'd love to show our new pal around town."

        hide nora neutral
        show nora excited

        n "With that settled, then, where to first?"
        jump enddemo

    label enddemo:

        scene bg room

        show shinigami neutral

        s "Unfortunately, that's as far as this version of the game goes!"

        s "I sincerely hope you've enjoyed this rough demo!"

        s "I really appreciate your support, and hope this demo got you interested in the project!"

        s "If you'd like to help the project in any way, you can find us on weightgaming, itch.io, and on discord."

        s "Thanks for playing!"

    # This ends the game.

    return
