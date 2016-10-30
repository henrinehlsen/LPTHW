def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "You have %d cheeses!" % cheese_count
    print "You have %d boxes of crackers" % boxes_of_crackers
    print "Man that's enough for a party!"
    print "Get a blanket. \n"



print "We can just give the function numbers directly:"
# gives exact numbers as arguments to the function
cheese_and_crackers(20, 30)

print "OR, we can use variables from our script:"
# defines two variables with exact values
amount_of_cheese = 10
amount_of_crackers = 50

# gives the two variables created earlier to the function,
# which is then assigned to the function
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print "We can even do math inside, too:"
# adds 10 to 20, and 5 to 6, and gives the results
# of those calculations to the function
cheese_and_crackers(10 + 20, 5 + 6)

print "And we can combine the twi, variables and math:"
# takes our predefined variables and adds 100 / 1000 to it.
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
