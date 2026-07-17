from typing import Callable


def log_function(func: Callable):
    
    
    #this will be printing the function name before running it

    def wrapper(*args, **kwargs):
        print(f"\nRunning: {func.__name__}")
        return func(*args, **kwargs)

    return wrapper