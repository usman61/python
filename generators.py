# Generators are special types of functions that allow you to generate values on the fly and
# return them one at a time, rather than generating and storing them all at once in memory.

# Simple example of a generator function that yields the square of each number from 1 to n:


def square_generator(n):
    for i in range(1,n+1):
        yield i**2



for num in square_generator(5):
    print(num)

