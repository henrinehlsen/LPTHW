from random import randint
from sys import exit

class Level(object):
    pass

class PhoneCall(Level):
    def enter(self):
        print "'Ring, Ring, Ring'"
        print "Who could that be?"
        print "Oh, it\'s the girl from last night."
        print "Damn it, what was her name again?!"
        print "'Uhm, hello?'"
        print "'Well, hello Partyboy...'"
        print "'Ohh, hi ... you ... !'"
        print "'Oh my god, You don\'t know my name, do you?'"
        print "'Yes?! Of course I do!'"
        print "'Well, then, what is it?'"
        print "I think it was something with an 'L', something like Lisa, Lucy, Liza.."

        reply = raw_input("I think it was ... ").lower()

        if "lisa" in reply:
            print "'Educated guess, but no. My name is Lucy, Asshole!'"
            print "'Well, whatever... Let's meet anyway."
            return 'date_transition'

        elif "lucy" in reply:
            print "'Gosh, I am relieved. You\'re not like all the others..'"
            return 'date_transition'
        elif "liza" in reply:
            print "'Liza?!! That is my best friend! Are you serious? I hate you both!!'"
            return 'game_over'

class DateTransition(Level):
    def enter(self):
        print "'Do you want to go out tonight?'"
        print "'Sure, where to?'"
        print "If I only knew what type of girl she was..."
        print """We could go to a fancy bar, the pub around the corner
or for some romantic ice skating"""
        return 'date_decision'

class DateDecision(Level):
    def enter(self):
        decision = raw_input("> ").lower()

        if "bar" in decision:
            print "You\'re going to the bar with Lucy"
            return 'fancy_bar'
        elif "pub" in decision:
            print "You\'re going to the pub with Lucy"
            return 'weird_pub'
        elif "cinema" in decision:
            print "You\'re going to the cinema with Lucy"
            return 'cinema'
        elif "skating" in decision:
            print "You\'re trying some romantic ice skating with Lucy"
            return 'ice_skating'
        else:
            print "Didn\'t get that, enter again"
            return 'date_decision'

class FancyBar(Level):

    def enter(self):
        print "You arrive at a fancy bar that your boss once recommended"
        print "'Are you serious?''"
        print "'Why, is something wrong?'"
        print "'I thought you\'d know me by now.'"
        print "Damn it, what\'s wrong with this place?"
        print "'You don\n't remember, do you??'"
        print "'...Remember what exactly?'"
        print "'I told you I hate fancy places.'"
        print "'... Oh, that ... well ... '"
        print "'Both my parents died in front of a Hilton hotel, you insensitive bastard!'"

        apology = raw_input("> ").lower()

        if "sorry" in apology:
            print "'Ok, you get a second chance, where are we going?'"
            return 'date_decision'
        elif "apologize" in apology:
            print "'Ok, you get a second chance, where are we going?'"
            return 'date_decision'
        else:
            print "'You know what? This was a bad idea. Never call me again.'"
            return 'game_over'


class WeirdPub(Level):
    def enter(self):
        print "'What a nice spot!'"
        print "'I am glad you remembered how I hated fancy bars'"
        print "'Uhm.. yeah, sure.'"
        print "'You are very sweet.. I am glad I met you.'"
        print "'Me too!'"
        print "Some time later..."
        print "'Whoa, how many beers did we have?'"

        beers = int(raw_input("> "))
        print "What? %d beers already?" % beers
        #print beers

        if beers >= 6:
            print "'I am much too drunk for this, sorry!'"
            print "She goes home and you\'re alone once again. Great job."
            return 'game_over'
        elif beers <= 5:
            print "'Well, I guess that is enough, do you want to come to my place?'"
            print "'Sure thing, I\'ll get my coat'"
            return 'her_place'



class IceSkating(Level):
    def enter(self):
        print "You\'re taking the train to the ice skating rink"
        print "'Well this is nice here.'"
        print "'Oh, good, you like it.'"
        print "'Sure, you remembered that I used to be an ice skating pro, right?'"
        print "Damn, I knew there was something about that idea. Why ice skating??"
        print "You\'re going to look like a fool."
        print "'Everything ok, tiger?'"
        print "And there she goes, skating so elegantly you cannot believe."
        print "What do you do? Pretend your skates don\'t fit or follow her to the ice?"

        ice_skate = raw_input("> ")

        if "shoes" or "fit" in ice_skate:
            print "'What a shame, my shoes don\'t fit. I\'d rather watch you!'"
            print "'Don\'t be a sissy, you\'re fine!'"
            print "She pulls you onto the ice"
            print "... And, how could it be else, you stumble the second she lets go of your hand"
            print "A minute later..."
            print "You sit on a bench, your nose still bleeding."
            print "'I am so sorry. Do you want to come to my place? I\'ll make you a drink!'"

            nose_bleed = raw_input("> ")

            if "yes" or "sure" in nose_bleed:
                print "'Sure. Why not.'"
                print "You're going to Lucy\'s by train, after half an hour, the two of you arrive."
                return 'her_place'
            elif "no" or "never" in nose_bleed:
                print "'Well. Ok then. See you whenever.'"
                print "Lucy leaves."
                return 'game_over'
            else:
                print "I didn\'t get that."
                nose_bleed = raw_input("> ")


        else:
            print "You follow her carefully."
            print "Concentrate!!"
            print "You almost slip, but suddenly, Lucy is there to take your hand."
            print "'You\'re cute.'"
            print "'This was fun! Do you want to come to my place for a drink?'"

            ice_decision = raw_input("> ")


            if "yes" or "sure" in ice_decision:
                print "'Sure. Why not.'"
                print "You're going to Lucy\'s by train, after half an hour, the two of you arrive."
                return 'her_place'
            elif "no" or "never" in ice_decision:
                print "'Well. Ok then. See you whenever.'"
                print "Lucy leaves."
                return 'game_over'
            else:
                print "I didn\'t get that."
                ice_decision = raw_input("> ")



class HerPlace(Level):
    def enter(self):
        print "You enter Lucy\'s place. A weird smell is coming from her kitchen."
        print "'Well, nice place you have here...'"
        print "'Oh thank you. Sit down and get comfortable, honey..'"
        print "The bad smell is getting worse. Do you want to look for the cause?"

        smell = raw_input("> ")

        if "yes" in smell:
            print "'Excuse me, I have to go to the bathroom'"
            print "You go to the hall, but you make a right towards the kitchen."
            print """After you stood there for a couple of seconds, you realize
that the smell comes from the fridge. What do you do?"""

            decide = raw_input("> ")

            if "open" or "fridge" in decide:
                print "You open the fridge, a human head is looking at you."
                print "You are scared, you turn around and ..."
                print "Lucy is right in front of you - a knife in her left hand"
                print "'Oh, Lucy, I .. am .. sorry..'"
                print "'It is too late.'"
                print "She turns to you and stabs you in the stomach"
                print "Warm blood is dripping onto the cold kitchen floor."
                print "All memory fades, and you only see blackness..."
                return 'game_over_dead'
            else:
                print "You go back to the hall and into the bathroom."
                print "When you return, Lucy is naked and waits for you on the carpet."
                print "A smile is on her pretty face."
                return 'game_won'

        else:
            print "Suddenly you realize, that she might not be too drunk, but you are."
            print "Everything starts turning and you feel very bad."
            print "'Listen, Lucy, I really have to get up early and ...'"
            print "You stop talking, panically looking at the bathroom door across the hall."
            print "Too late, you vomit on her carpet."
            print "'Damn it, that is disgusting! Get out of here!'"
            return 'game_over'


class GameWon(Level):
    print "Great job, YOU WON!!"
    print "\nCreated by Henri Nehlsen"

class GameOver(Level):
    def enter(self):
        print "She will never speak with you again. YOU LOSE"
        print "\nCreated by Henri Nehlsen"
        exit(1)

class GameOverDead(Level):
    def enter(self):
        print "You died. GAME OVER"
        print "\nCreated by Henri Nehlsen"
        exit(1)
