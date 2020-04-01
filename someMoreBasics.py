# Find the longest word in a list and return it, function below:

"""

def find_longest_word(words_list):
    word_len = []
    for n in words_list:
        word_len.append((len(n), n))
    word_len.sort()
    return word_len[-1][1]

print(find_longest_word(["Inconsequential", "Barbaric", "Indivisibility"]))

"""

# Below is a way to return/replace the first letter of a string with some specific value/character.

"""

my_string = "racecar driver"
replace_value = my_string[0]
modified_string= my_string.replace(replace_value, "$")

print(replace_value + modified_string[1:])

"""

# Below is a funciton, which cam take in two numbers and treats them as an exponential equation.
# 'Number' multiplies itself however many times 'power_of' says to. 

"""

def manual_calculation(number, power_of):
    num_list = [number] * power_of
    calc_result = 1
    
    for i in num_list:
        calc_result = i * calc_result
    return calc_result

print(manual_calculation(23, 17))

"""

# Below is a function which can reverse a string entirely. 

"""

def reversible_word(example):
    return example[::-1]

print(reversible_word("Indivisibility"))

"""

# Another method for reversing a word. This one behaves a little differently, however.
# This function iterates over each letter of the string, splits them, appends them to the list called
# 'word_container', and then maps them into the word_container list, as their own values.
# Finally, it uses the 'join' method/function, and joins each element together in the form of the string data type.
# Specifically, it is in the form of one string. 

"""

def word_reverser(word):
    word_container = []

    for i in word: word_container = i.split() + word_container

    word_container = map(str, word_container)
    reverse_word = "".join(word_container)

    return reverse_word

print(word_reverser)

"""

# One last way to reverse a word in Python. See the function below:

"""

def reversible_word(word):
    result = ""
    word_list = list(word)

    for letter in range(len(word_list)):
        result += word_list.pop()

    return result

print(reversible_word("Tyson"))

"""
# Below is an example of a dictionary object that has an interesting set of key-value pairs. The value is an array of channels.
# The print statements are simply to demonstrate how to traverse and isolate different keys/values/items in this dictionary.

"""

filter_genre = {
    "Action" : {
        "HBO" : ["The Pacific", "Watchmen"],
        "TNT" : ["Top Gun", "Terminator"]
    },
    "Romance" : {
        "ABC" : ["The Bachelorette", "Once Upon A Time"],
        "CBS" : ["Mom", "I Love Lucy"]
    },
    "Comedy" : {
        "Fox" : ["How I Met Your Mother", "New Girl"],
        "Disney Channel" : ["That's So Raven", "Mickey's Playhouse"]
    }
}

print(filter_genre.keys()) # All genres.
print(filter_genre["Comedy"].keys()) # Keys within Comedy Genre
print(filter_genre.pop("Romance", "Genre does not exist")) # Channels and lists of Romance genre.
print(filter_genre["Action"]["HBO"][1:2]) # Second TV show listed in HBO key/channel.

"""

# Below is a demonstration on how to utilize slice in a few different ways. Brief overview.
# To slice up lists, tuples, arrays, or strings, you use the below syntax in the print statements.

"""

post = ('Python Basics', 'Intro guide to python', 'Some cool python content', 'published')

tags = ['Hello', 'Again', 'And Again']

print(tags[:2]) # This is calling for the tags list, and it is saying to start at the 0'th index, and to end the slice at the beginning of the 2nd index.
print(post[:2]) # Same as above, calling to begin on the 0'th index, slice ends at the start of the 2nd index.

print (post[1::2]) 

"""

# The above syntax is another way to be specific, it takes three possible parameters.
# The first parameter, says start at the beginning of the 1st index.
# The second parameter, can be used to indicate the end of the slice.
# The third parameter says how to 'step'. So if we start at 1, and we 'step' 2, then this slice will SPECIFICALLY grab
# every other index after the 1st index.

"""

post = ('Python Basics', 'Intro guide to python', 'Some cool python content', 'published')

# To remove something from the end of a tuple, see below.
post = post[:-1]

print(post)

# To remove from the start of the Tuple, see below,.
post = post[1:]

print(post)

"""
# It is possible to completely remove an element by using the .remove() syntax, however this is a HORRIBLE practice,
# it is heavily discouraged amongts the programming community.


# Basic for loop example. Looping over a tuple and printing out each individual element of that tuple.

"""

players = ('Altuve', 'Bregman', 'Correa', 'Gattis')

for player in players:
    print(player)


# Below, the for loop does a little more than the one above. The loop below, loops through the dictionary object, and we are labeling the key as position, and the value as player. 
# When I say print, it prints out a string to give a nice appearance to the output, indicating what IS being printed.
# From there, we are saying to the key (position) and value (player). 

players = {
    '2b' : 'Altuve',
    '3b' : 'Bregman',
    'ss' : 'Correa',
    'dh' : 'Gattis',
}

for position, player in players.items():
    print('Position/Playerssssss : ', position, player)

"""

# Below we have a list labeled 'users'. 

"""

users = [
    'Altuve',
    'Bregman',
    'Correa',
    'Gattis',
    'Tyson'
]

# Continue / Break. 'Continue' continues the looping process even if what we are searching for is found or specified. 'Break' stops the loop once the goal has been accomplished, or what we have been searching for has been found. 
# The for loop below will iterate over the users list created above, and will stop looping once it finds the user 'Gattis'. It will then print out an interpolated string, that specifies which index the user 'Gattis' was found at.

for user in users:
    if user == "Gattis":
        print(f'{user} was found at index {users.index(user)}')
        break
    print(user)

"""


# The below code block is a quick showing of a while loop. The nums variable we declared, is a list that ranges from 1 all the way to 99. The range ends at the final number's index.
# This will return each number from 1 all the way through 99.

"""

nums = list(range(1, 100))

while len(nums) > 0:
    print(nums.pop())

"""

# Below is an example with two solutions listed. The first one is not necessarily a solution, but a method that is close to achieving the goal.
# The goal is to get these two lists to display in the form of a single list.

"""

legacy_customers = ['Alice', 'Bob']
new_customers = ['Tiffany', 'Kristine']

raw_db = [legacy_customers, new_customers]

# Again, doing it this way will have raw_db return us a list that contains two lists. The goal should be to get these elements all combined into a singular list.

print(raw_db)

# Below is how we would accomplish this. We simply use a for-loop to loop over one of the two lists, and append each of the looped-values from the looped-list, to the other list.

for legacy_customer in legacy_customers:
    new_customers.append(legacy_customer)

print(new_customers)

"""

# For the below code, a range is created. From there, a for loop is running through the created-range.
# The for loop's condition is saying for each number in the created range, if you divide that number by 2, and your result is an even number, then append the number you divided by 2, to the even_nums list.

"""

num_list = range(1, 11)
even = []

for num in num_list:
    if num % 2 == 0:
        even.append(num)

print(even)

# Below we have assigned two variables using a single-line for loop. The syntax is a little different.
# The first 'num' you see in this assignment, is what will be returned when the variable is called. This is the first thing a single-line for loop must state.
# From there, we say for each individual value in the num_list, if that value divided-by-two is equal to an even number, then populate this list with that number.
# Same for the odd_numbers list. Instead of saying if the value divided-by-two is equal to an even number, we are saying if the number divided-by-two is equal to an odd number.

even_numbers = [num for num in num_list if num % 2 == 0]

odd_numbers = [num for num in num_list if num % 2 == 1]

print(even_numbers)
print(odd_numbers)

"""

# Below is a demonstration of the ** operator, which in Python, is a way of saying to exponentially multiply the value before the **, as many times as the value after the ** is equal to.

"""

num_list = range(1, 11)

cubed_nums = []

for num in num_list:
    cubed_nums.append(num ** 3)

# The for loop above, causes the print statement below to show each number between 1 and ten, cubed. so 1*1*1, 2*2*2, so-on and so-forth.

print(cubed_nums)

cubed_nums = [num ** 3 for num in num_list]

print(cubed_nums)

"""

