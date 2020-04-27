# Below is a function that takes in an object. It iterates through that object, and says for each key(name) and each value(weight)
# inside of the collection, we want to append each key to the container_list list, however many times it's relative
# value shows. So for Win, it will append once. For break_even, it will append twice, etc. 
# from there, we say that we want the function to iterate through the dynamic array, and randomly print out a single
# value from that list.

import numpy as np

def weighted_lottery(weights):
    container_list = []

    for (name, weight) in weights.items():
        for _ in range(weight):
            container_list.append(name)

    return np.random.choice(container_list)

weights = {
    "win" : 1,
    "break_even" : 2,
    "lose" : 3
}

print(weighted_lottery(weights))