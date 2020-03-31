# The below code is just how to declare variables. The two variables below contain different data types. The first, is a string. The second, is a number.
# The following two lines, we are simply calling the two variables and printing their value into the console.

name = 'Tyson'
post_count = 42

print(name)
print(post_count)

x = 23
y = 123
# Single letter variable names are heavily discouraged. Best practice is to limit my comments in Python coding, and ensure that my variable names are well-thought-out.

# Booleans - True or false value. * The way you designate if something is true, you use Capital T and spell out True. Same with False. Capital F and follow with the remaining letters to complete the word. 
# Numbers - Very complex data type in Python, can connected to other number databases in Python.
# Strings - Can be any type of byte sequence. Ex: A name, an entire HTML document, integrate strings in different ways. Usually are wrapped by single or double quotation marks.
# Bytes and byte arrays - Very advanced, will MAYBE learn later on.
# None - Want to define a variable? Dont want to set a value? Set it equal to None, basically a placeholder. 

# DATA CATEGORIES - USED TO MANAGE COLLECTIONS OF DATA.
# Lists - Similar to an array, gives you a list of items.
# Tuples - Similar to sets, has own definitions though.
# Sets - Similar to Tuples.
# Dictionaries - Abilities to have key value pairs.

# Below is an example of some basic math syntax in python. You can also see that you are able to reassign the value of a variable to the value of another variable, if you choose to do so.

meal_completed = True
total = 100
tip = total * 1/5
total = total + tip
receipt = "Your total is " + str(total)
print(receipt)

first = 'Springer'
second = 'Bregman'
third = 'Altuve'

print(first)

first = third

print(first)

# Targeting different characters for capitalization. Using these 'functions' to modify the value contained within our targeted variable.

sentence = 'the quick brown fox jumps over the lazy dog.'.capitalize()
print(sentence)

sentence = 'the quick brown fox jumps over the lazy dog'.title()
print(sentence)

sentence = 'THE QUICK BROWN FOX JUMPED OVER THE LAZY DOG'.lower()
print(sentence)


# The quick brown fox jumps over the lazy dog
# T => 0
# h => 1
# e => 2
# space-after-letter-e => 3
# Strings are immutable, meaning we cannot alter the charactes in the string once it has been created. We are able to create a new variable that would be a modified version of our primary variable, but we are not able to modify the primary variable because strings are immutable.

starter_sentence = 'The quick brown fox jumps over the lazy dog'
print(starter_sentence[12])= 'Z'
print(starter_sentence) 

# The above will not change the 12th index of the starter_sentence variable, because the starter_sentence variable is a string, strings are immutable.

# below is a demonstration of ranges.
""" 
starter_sentence_two = 'The quick brown fox jumps over the lazy dog'
first_word = starter_sentence_two[0:3]
new_sentence= first_word
print(new_sentence)
"""

# Below is a demonstration of a string, and while being immutable, we find a way to spit out a new variable that is a modified version of the initial variable we used.
"""
starter_sentence = 'The quick brown fox jumps over the lazy dog.'
new_sentence = 'Thy' + starter_sentence[3:]
print(new_sentence)
"""

# Heredoc is a multi line string, that counts all of the newline characters.
# .strip() is a string method in python, that removes whatever characters you pass into it. So if I 
# wanted spaces at the start and end to be removed, I can just leave the paran's in .strip() blank.

content = """
Nullam id dolor id nibh ultricies vehicula ut id elit.   Nullam quis risus eget urna mollis ornare vel eu leo.

Vestibulum id ligula porta felis euismod semper. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Cras justo odio, dapibus ac facilisis in.

Integer posuere erat a ante venenatis dapibus posuere velit aliquet.
""".strip()
print(content)

# Below is just a little bit of math play. Declared variables possess numeric datatype values, we were shown
# the basics of using if/else conditionals inside of the Python language.

positive_number = 234
negative_number = positive_number * -1

print(negative_number)

pos_num = 25
if pos_num > 0:
  num = num*-1
  print(num)
else:
  print(num)


print(email_content)

# ######################################################################################################################################
# Below is an example of string interpolation in Python. And there are two different ways displayed for how you can have these displayed.

name_one = 'Skyllas'
age_one = 5
product_one = 'Python eLearning course'

# greeting_one = "Hi {0}, you are listed as {1} years old and you have purchased: {2}...".format(name_one, age_one, product_one)

# print(greeting_one)

greeting_one = f"Hi {name_one}, you are listed as {age_one} years old and you have purchased: {product_one}..."

print(greeting_one)

# Partition typically breaks a string into a 3-value tuple. If you assign each piece of the string to a variable, however, as is done in line 135 below, then each value is stored within the declared variable names.

heading = "Python: An Introduction"

# '_' is used as a placeholder, essentially. Something we don't necessarily care for, that is why the colon is assigned to it. 

header, _, subheader = heading.partition(': ')

print(header)
print(_)
print(subheader)

# ######################################################################################################################################

tags = 'python,coding,programming,development'

# Split. Quick overview. Split shown below, with the ',', means that python will go in and find each occurance of the comma, and make the values before and after the comma, their own values within a list.

list_of_tags = tags.split(',')

print(list_of_tags)

# Below is split being used without targeting any piece of the string in particular. This would result in a list with a single item/value. This singular value would be the entire string.

list_of_tags = tags.split()

print(list_of_tags)

