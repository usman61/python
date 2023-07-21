# Decorators:
# The main use case of the symbol @ in Python are decorators. 
# In Python, a decorator extends the functionality of an existing function or class.
# Let understand decorators with help of a example given below.


def my_decorator(func):    # argument func here means say_hello
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")


say_hello()