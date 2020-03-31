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
