# map function in pyton
# its a built-in function that allows you to apply a given function to each item of one or more
# iterable objects (e.g., lists, tuples) and returns an iterator that yields the results

# A function that squares a number
def square(x):
    return x ** 2

numbers = [1, 2, 3, 4, 5]


# Using map() to square each element of the 'numbers' list
squared_numbers = map(square, numbers)

# The result of 'map' is an iterator, so we convert it to a list to see the values
squared_numbers_list = list(squared_numbers)

print(squared_numbers_list)