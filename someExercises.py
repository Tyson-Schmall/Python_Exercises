# When calling on a dictionary, we are able to call on it's keys, or we can even call it by the name of the key with the proper syntax, place it in square brackets like we're calling on an index.

"""

priority_index = {
    (1, "premier"): [7, 34, 12],
    (1, "mvp"): [84, 22, 21],
    (2, "standard"): [93, 81, 77],
}

print(list(priority_index.keys()))

print(priority_index[(1, "premier")])

"""

# Zip function in Python, shown very in a basic manner below. The zip function takes these two separate lists, combines their individual indexes with that of the other, and creates a list of tuple's. 

"""

positions = ['2b', '3b', 'ss', 'dh']
players = ['Altuve', 'Bregman', 'Correa', 'Gattis']

players_and_positions = zip(positions, players)

print(list(players_and_positions))

"""

# With the below codeblock, you can see that boolean is returned upon the syntax we call.
# Declaring a variable and setting it's value to see if a value is contained within an object, will return booleans.

"""

tags = {
    'python',
    'coding',
    'tutorials',
    'coding'
}

print(tags)

query_one = 'python' in tags
query_two = 'ruby' in tags

print(query_one)
print(query_two)

"""

# Below is an example of how to merge sets in Python. Note that the two sets we merge, do share some shared value attributes. 
# The merge method in Python is programmed to not display duplicate values in it's output. 

"""

# Set one
tags_one = {
    'python',
    'coding',
    'tutorials',
    'coding'
}

# Set two
tags_two = {
    'ruby',
    'coding',
    'tutorials',
    'development'
}

# Merge method
merged_tags = tags_one | tags_two

print(merged_tags)

# tags_one specific
exclusive_to_tag_one = tags_one - tags_two

# tags_two specific
exclusive_to_tag_two = tags_two - tags_one

# Below print statements will show tags that are exclusive to each tags set.
print(exclusive_to_tag_one)
print(exclusive_to_tag_two)

# tags found in both tags_one/tags_two; This shows the tags that are the same in both sets. 
universal_tags = tags_one & tags_two
print(universal_tags)

"""

