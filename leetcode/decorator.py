def decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Before calling {func.__name__}")
        result = func(*args, **kwargs)
        print(f"After calling {func.__name__}")
        return result

    return wrapper


@decorator
def my_function():
    print("Inside the decorated function")


# Calling the decorated function
my_function()
