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


post = ('Python Basics', 'Intro guide to python', 'Some cool python content', 'published')

tags = ['Hello', 'Again', 'And Again']

print(tags[:2]) # This is calling for the tags list, and it is saying to start at the 0'th index, and to end the slice at the beginning of the 2nd index.
print(post[:2]) # Same as above, calling to begin on the 0'th index, slice ends at the start of the 2nd index.

print (post[1::2]) 
# The above syntax is another way to be specific, it takes three possible parameters.
# The first parameter, says start at the beginning of the 1st index.
# The second parameter, can be used to indicate the end of the slice.
# The third parameter says how to 'step'. So if we start at 1, and we 'step' 2, then this slice will SPECIFICALLY grab
# every other index after the 1st index.

post = ('Python Basics', 'Intro guide to python', 'Some cool python content', 'published')

# To remove something from the end of a tuple, see below.
post = post[:-1]

print(post)

# To remove from the start of the Tuple, see below,.
post = post[1:]

print(post)

# It is possible to completely remove an element by using the .remove() syntax, however this is a HORRIBLE practice,
# it is heavily discouraged amongts the programming community.


