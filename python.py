#String formatters

#{} is the placeholders


print("Tom has {} balloons".format(3))
#-----------------------
#output: Tom has 3 balloons
#-----------------------

print("Tom has {} {}".format(5, "balloons"))
#-----------------------
#output: Tom has 5 balloons
#-----------------------

print("Tom, {0}, has {1} balloons".format("my friend", 3))
#-----------------------
#output: Tom, my friend, has 3 balloons
#-----------------------

print("Tom the {0} has {number} balloons".format("boss", number=5))
#-----------------------
#output: Tom the boss has 5 balloons
#-----------------------


#Spifying Type
#{field_name:conversion}, where field_name specifies the index number of the argument
#s for string, d for decimal, f for floats

print("Tom ate {0:.3f} percent of a {1}".format(2.123456, "pizza"))
#-----------------------
#output: Tom ate 2.123 percent of a pizza
#-----------------------
