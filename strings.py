caesar = "Graham"
praline = "John"
viking = "Teresa"

# Index (psoition of an item)
# Each character in an string in assigned a number.
# Index starts at 0
c = "cats"[0]
d = "dogs"[2]

# Set a variabled called fifth_letter to the 5th letter of the word MONTY

word = "MONTY"
fifth_letter = word[4]
print (fifth_letter)

# String Methods
# Methods that use dot notation only work for strings
# len() = number of characters in string
parrot = "Norwegian Blue"
print (len(parrot))
# lower() -- converts all letters to lower case
print ("AnNa".lower())
# upper()
print ("anna".upper())
# str() turns non-strings into strings

ministry = "The Ministry of Silly Walks"
print (len(ministry))
print (ministry.lower())

# String Concatenation
print ("Hi " + "number " + str(5))

# Formatting with %
# Use % to replace the %s placeholders with variables in parenthesis
name = "Mike"
print ("Hi, I'm % % (name))
