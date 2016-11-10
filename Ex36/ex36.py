import time
from sys import exit

positive=["ja", "yes", "yep", "of course", "indeed", "definitely", "absolutely"]
negative=["no", "nope", "nein", "nay", "not"]
not_understood = "I didn\'t get that, sorry"

def define_player():
    print "Welcome!"
    print "What is your name?"
    define_player.player_name = raw_input(">>> ")
    print "Ok, well then %r" % define_player.player_name
    print "Let the game begin!"
    time.sleep(2)
    office_desk()

def office_desk():
    print "You are sitting in your office chair,"
    print "waiting for the time to pass by.\n"
    time.sleep(3)
    print "\'Ring, Ring\'"
    time.sleep(1)
    print "\'Ring, Ring\'\n"
    time.sleep(1)
    print "Will you answer the phone?"

    while True:
        phone_decision = raw_input(">>> ").lower()
        if phone_decision in positive:
            print "\"Hello?\""
            phonecall()
        elif phone_decision in negative:
            print "The day is going by slower than ever"
            print "and you\'re eventually dying of boredom."
            time.sleep(2)
            exit(0)
        else:
            print not_understood

def phonecall():
    print "It is your boss."
    time.sleep(1)
    print "\"Hey %r, I need you to get a couple of" % define_player.player_name
    print "things for my wife, can you do that?\""

    while True:
        answer_to_boss = raw_input(">>> ").lower()

        if phone_decision in positive:
            print "\"Great, I\'ll send you the details via email!\""
            open_email()
        elif phone_decision in negative:
            print "\"You know what %r?" % define_player.player_name
            print "I never liked you anyway.\""
            print "\"You are fired!!!\""
            time.sleep(2)
            exit()
        else:
            print not_understood



new_purse = "New Purse"
high_heels = "High Heels"
fancy_dress = "Fancy Dress"
new_watch = "New Watch"
prices = [1600, 875, 1450, 600]

def open_email():
    print "Your boss sent you an email:\n"
    print "\tDear %r" % define_player.player_name
    open_email.email = """\tPlease get my wife some of the following items.
    She doesn\'t need all of them, so select only three out of four:\n
    \t%r - %d€
    \t%r - %d€
    \t%r - %d€
    \t%r - %d€\n
    You can take my credit card, but don't spend too much money!
    Best,
    Your Boss!\n\n""" % (new_purse, prices[0], high_heels, prices[1], fancy_dress, prices[2], new_watch, prices[3])
    print open_email.email
    print "You can buy everything online or go to the mall,"
    print "it\'s your choice, %r" % define_player.player_name
    print "what do you want to do?"

    while True:
        shopping_decision = raw_input(">>> ").lower()
        decision_online = ["online", "digital", "internet"]
        decision_mall = ["mall", "analog"]
        if shopping_decision in decision_online:
            online_shopping()
        elif shopping_decision in decision_mall:
            mall_shopping()
        else:
            print not_understood

def online_shopping():
    print "Cool, some online shopping! You\'re on Amazon now"
    time.sleep(1)
    eliminate_item()

def mall_shopping():
    print "Cool, we\'re getting out of our lazy chair."
    print "You take the train to the mall and you immediately regret it."
    time.sleep(1)
    print "You arrive at the mall and you hate it, the minute you enter it."
    print "Fortunately, you find a clerk that\'s willing to help you."
    time.sleep(1)
    eliminate_item

keyw_purse = ["purse"]
keyw_heels = ["high", "heels", "shoes"]
keyw_dress = ["fancy", "dress"]
keyw_watch = ["watch"]
option_purse = (sum(prices) - prices[0])
option_heels = (sum(prices) - prices[1])
option_dress = (sum(prices) - prices[2])
option_watch = (sum(prices) - prices[3])

def success():
    print "Well done, your boss and his wife are happy!!!\n"

def unsuccessful():
    print "You spent too much money, your boss is angry!!!"
    print "You will never get a promotion...\n"

def credits_and_ending():
    print "NOW GO BACK TO WORK!!!\n\n\n"
    print "GAME OVER, THANKS FOR PLAYING!\n"
    print "...all code written by Henri Nehlsen"

def eliminate_item():
    "First, you need to eliminate one of the items on the list."
    "You forgot everything, right? Should we look at the email once again?"

    while True:
        email_reminder = raw_input(">>> ").lower()

        if email_reminder in positive:
            print open_email.email
            break
        elif email_reminder in negative:
            print "Ok then, which item do you want to eliminate?"
            break
        else:
            print not_understood

    while True:
        dismissed_item = raw_input(">>> ").lower()

        if dismissed_item in keyw_purse:
            print "Well, then, you bought:"
            print """Beautiful %r, a pretty
            neat %r and a super cool %r""" % (high_heels, fancy_dress, new_watch)
            print "You spent %d€" % option_purse
        elif dismissed_item in keyw_heels:
            print "Well, then, you bought:"
            print """A beautiful %r, a pretty
            neat %r and a super cool %r""" % (new_purse, fancy_dress, new_watch)
            print "You spent %d€" % option_heels
        elif dismissed_item in keyw_dress:
            print "Well, then, you bought:"
            print """A beautiful %r, some pretty
            neat %r and a super cool %r""" % (new_purse, high_heels, new_watch)
            print "You spent %d€" % option_dress
        elif dismissed_item in keyw_watch:
            print "Well, then, you bought:"
            print """Beautiful %r, a pretty
            neat %r and a brand new %r""" % (new_purse, high_heels, fancy_dress)
            print "You spent %d€" % option_watch
        else:
            print not_understood

define_player()
