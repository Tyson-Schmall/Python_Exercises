# Below is a heading generator. This is simply a function, but it can be scaled and molded to fit in many different spots, if need's be.
# The first way you see we can generate a heading, is by simply using string interpolation, and returning the two parameters we specify in our function declaration.

"""

def heading_generator(title, heading_type):
    return f"<h{heading_type}>{title}</h{heading_type}>"

print(heading_generator('This is my title', '3'))

"""

