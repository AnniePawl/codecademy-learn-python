# CONTROL FLOW gives us the ability to choose among outcomes based on what else is happening in the program
# There are 6 comparators

3 == 3
5 > 2
4 < 7
7 >= 7
5 <= 9
4 != 8

# BOOLEAN Operators
# Compare statements and result in True or Flase
# 'and' checks if both statements are True
# 'or' checks if either statement is true
# 'not' gives opposite of statement
(3 < 4) and (5 == 5)
# Order of Operations
# Parenthesis () used to ensure expressions are evaluated in the right order
# 'not' evaluated first
# 'and' next
# 'or'nis last

# Conditional Statement SYNTAX
# 'if' is a conditional statement that executes some specified code after checking if its expression is True
# 'else' complements 'if'. The pair says, if this is true, run this indented block. If
# 'elif' is short for else is. This statement is only checked if original if statement is false
if this_might_be_true():
  print "This really is true."
elif that_might_be_true():
  print "That is true."
else:
  print "None of the above."
