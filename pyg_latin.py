# Create a basic Pig Latin translator
# Move first letter to the end and add 'ay'. So 'Python' becomes 'Ythonpay'

print ('Welcome to the Pig Latin Translator!')
# Ask user to input a word
original_word = input ('Enter a word: ')

# Pyg Variable
pyg = 'ay'

# Make sure user entered valid word
# Check if string is empty and characters only
# Convert word from English to Pig Latin
# Display translation
if len(original_word) > 0 and original_word.isalpha():
    first_letter = original_word[0]
    new_word = original_word + first_letter + pyg
    print("Here's your translation: " + new_word[1:].title())
else:
    print("try again!")
