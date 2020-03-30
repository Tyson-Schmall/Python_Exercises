import operator
from functools import reduce

# Function that will do the dynamic reducing, is declared below; It takes in two arguments.
# Arguments: collection, and the operators[op]. 
# The imported library 'operator' is what is providng the functions we assigned in the
# below 'operators' dictionary object(.add, .sub. .mul, .truediv).
# From functools import reduce, provides us access to the reduce function that is used further down.
def dynamic_reducer(collection, op):
    operators = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv
    }
    
    # reduce takes in two arguments/parameters. The first is a lambda. the second, is whatever collection we pass in.
    # a lambda is an anonymous function. In this scenario, it takes in a total and an element as it's two param's.
    # We have defined the 'element' parameter as taking in the value of whatever key we pass in from our dictionary object.
    # Each Key in the dictionary, being tied to a function from the operator library, will expect two arguments.
    # So this lambda, is saying basically, to take the operator from our dictionary, and in the collection that is passed in
    # to this function, place the operator between each element of that collection, and compute.
    # Examples of the function running are down at the bottom of this document.
    return reduce((lambda total, element: operators[op](total, element)), collection)

print(dynamic_reducer([1, 3, 5], '+')) # 1 + 3 + 5
print(dynamic_reducer([1, 3, 5], '-')) # 1 - 3 - 5
print(dynamic_reducer([1, 3, 5], '*')) # 1 * 3 * 5
print(dynamic_reducer([1, 3, 5], '/')) # 1 / 3 / 5