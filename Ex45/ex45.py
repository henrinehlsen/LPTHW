from sys import exit
from random import randint
import MyModule



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

        elif "lucy" in reply:
            print "'Gosh, I am relieved. You\'re not like all the others..'"


class DateDecision(Level):
    def enter(self):
        print "'Do you want to go for a drink?'"
        print "'Sure, where to?'"
        print "If I only knew what type of girl she was..."
        print """We could go to a fancy bar, the pub around the corner, to the cinema
        or for some romantic ice skating"""

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
        elif ("skating" or "ice") in decision:
            print "You\'re trying some romantic ice skating with Lucy"
            return 'ice_skating'
        else:
            print "Didn\'t get that, enter again"
            return 'date_decision'

class FancyBar(Level):
    pass

class WeirdPub(Level):
    pass

class Cinema(Level):
    pass

class IceSkating(Level):
    pass



MyModule.Engine()
