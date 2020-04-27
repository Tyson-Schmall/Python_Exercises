# Below is a list containing four number-values. The function takes in a list of numbers, and adds them all together. 
# From there, it divides the total of all numbers contained in the list, by the number OF numbers within that list. 
# In this scenairo, average_me_out will be totaled up, and divided by 4, as there are 4 numbers in the list.

"""

average_me_out = [123, 456, 854, 795]

def average_calculator(num_list):
    summed_up_list = sum(num_list)
    solution = summed_up_list/len(num_list)
    return solution

print(average_calculator(average_me_out))

"""

# Below is another way to execute the same code using reduce from functools.

from functools import reduce

# First, we pull from functools, the reduce method. Then we implement it in a way like below:

"""

def get_average(num_list):
    total = reduce((lambda total, element: total + element), num_list)
    
    return total / len(num_list)

print(get_average([25, 35, 45, 65, 95]))

"""