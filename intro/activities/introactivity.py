# Python Advanced Features Homework
# ---------------------------------
# This homework will give you practice with:
# - List comprehensions
# - Generators
# - Decorators
# - Lambda functions

# Part 1: List Comprehensions
# --------------------------

def exercise_1():
    """
    1. Create a list of squares of even numbers from 1 to 20
    """
    # TODO: Replace with your solution
    pass

def exercise_2():
    """
    2. Create a list of tuples (number, square, cube) for numbers from 1 to 10
    """
    # TODO: Replace with your solution
    pass

def exercise_3(words):
    """
    3. Filter a list of words to only include those with more than 5 characters
       and convert them to uppercase
       
    Args:
        words: List of strings
    """
    # TODO: Replace with your solution
    pass

def exercise_4(matrix):
    """
    4. Flatten a matrix (list of lists) into a single list
    
    Args:
        matrix: A list of lists of integers
    """
    # TODO: Replace with your solution
    pass

def exercise_5(dictionary):
    """
    5. Create a list of formatted strings from a dictionary
    
    Args:
        dictionary: A dictionary with string keys and integer values
    """
    # TODO: Replace with your solution
    pass

# Part 2: Generators
# -----------------

def fibonacci_generator(n):
    """
    1. Create a generator that yields the first n Fibonacci numbers
    
    Args:
        n: Number of Fibonacci numbers to generate
    """
    a, b = 0, 1
    count = 0
    while count < n:
        yield a
        a, b = b, a + b
        count += 1

def filtered_reading_generator(filename, filter_func):
    """
    2. Create a generator that reads a file line by line and yields only lines
       that satisfy a filter_func
       
    Args:
        filename: Name of file to read
        filter_func: Function that takes a string and returns a boolean
    """
    with open(filename, 'r') as file:
        for line in file:
            if filter_func(line):
                yield line.strip()

def countdown_generator(start, step=1):
    """
    3. Create a generator that counts down from start to 0 by step
    
    Args:
        start: Starting number
        step: Step size for countdown (default 1)
    """
    current = start
    while current >= 0:
        yield current
        current -= step

def exercise_6():
    """
    4. Use a generator expression to calculate the sum of squares of odd numbers from 1 to 50
    """
    # TODO: Replace with your solution
    pass

# Part 3: Decorators
# -----------------

def timer_decorator(func):
    """
    1. Create a decorator that measures and prints the execution time of a function
    """
    import time
    
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Function {func.__name__} took {end_time - start_time:.6f} seconds to run")
        return result
    
    return wrapper

def retry_decorator(max_attempts):
    """
    2. Create a decorator that retries a function up to max_attempts times if it raises an exception
    
    Args:
        max_attempts: Maximum number of retry attempts
    """
    def decorator(func):
        def wrapper(*args, **kwargs):
            attempts = 0
            while attempts < max_attempts:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    attempts += 1
                    if attempts == max_attempts:
                        raise e
                    print(f"Attempt {attempts} failed. Retrying...")
            
        return wrapper
    return decorator

def cache_decorator(func):
    """
    3. Create a decorator that caches the results of a function call
    """
    cache = {}
    
    def wrapper(*args):
        if args in cache:
            return cache[args]
        result = func(*args)
        cache[args] = result
        return result
    
    return wrapper

def validate_args_decorator(validator_func):
    """
    4. Create a decorator that validates arguments using a validator function
    
    Args:
        validator_func: Function that takes the same arguments as the decorated function
                       and returns True if they are valid, False otherwise
    """
    def decorator(func):
        def wrapper(*args, **kwargs):
            if not validator_func(*args, **kwargs):
                raise ValueError("Invalid arguments provided")
            return func(*args, **kwargs)
        return wrapper
    return decorator

# Part 4: Lambda Functions
# -----------------------

def exercise_7():
    """
    1. Sort a list of tuples by the second element using a lambda function
    """
    data = [(1, 5), (3, 2), (7, 8), (2, 1)]
    # TODO: Replace with your solution
    pass

def exercise_8():
    """
    2. Use map with a lambda function to convert a list of temperatures from Celsius to Fahrenheit
    """
    celsius_temps = [0, 10, 20, 30, 40]
    # TODO: Replace with your solution
    pass

def exercise_9():
    """
    3. Use filter with a lambda function to get all prime numbers from 1 to 50
    """
    # This is a more complex example using a lambda with a helper function
    def is_prime(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True
    
    # TODO: Replace with your solution
    pass

def exercise_10():
    """
    4. Create a dictionary mapping each number from 1 to 10 to its factorial using a dictionary comprehension
       and a lambda function
    """
    import functools
    # TODO: Replace with your solution
    pass

# Part 5: Integration
# ------------------

@timer_decorator
def compute_prime_squares(n):
    """
    Use a list comprehension to get squares of prime numbers up to n.
    This function is decorated with the timer_decorator.
    
    Args:
        n: Upper limit for considering prime numbers
    """
    is_prime = lambda x: x > 1 and all(x % i != 0 for i in range(2, int(x**0.5) + 1))
    return [x**2 for x in range(2, n+1) if is_prime(x)]

def number_generator_pipeline(n):
    """
    Create a generator pipeline that:
    1. Generates numbers from 1 to n
    2. Filters out non-prime numbers
    3. Maps each prime to (prime, prime^2)
    
    Use generator expressions and lambda functions.
    
    Args:
        n: Upper limit of the range
    """
    # Generate numbers from 1 to n
    numbers = (i for i in range(1, n+1))
    
    # Filter for primes (reusing the lambda from compute_prime_squares)
    is_prime = lambda x: x > 1 and all(x % i != 0 for i in range(2, int(x**0.5) + 1))
    primes = (x for x in numbers if is_prime(x))
    
    # Map to tuples of (prime, prime^2)
    result = ((p, p**2) for p in primes)
    
    return result

# --------------------------------
# Bonus Challenge: Advanced Usage
# --------------------------------

def compose(*functions):
    """
    Create a function that composes multiple functions together.
    For example: compose(f, g, h)(x) = f(g(h(x)))
    
    Args:
        *functions: Variable number of functions to compose
    """
    def composed_function(x):
        result = x
        for f in reversed(functions):
            result = f(result)
        return result
    return composed_function

@validate_args_decorator(lambda x: isinstance(x, list) and all(isinstance(i, int) for i in x))
@cache_decorator
def product_of_primes(numbers):
    """
    Compute the product of all prime numbers in a list.
    This function is decorated with both validate_args_decorator and cache_decorator.
    
    Args:
        numbers: List of integers
    """
    is_prime = lambda x: x > 1 and all(x % i != 0 for i in range(2, int(x**0.5) + 1))
    prime_numbers = [n for n in numbers if is_prime(n)]
    
    if not prime_numbers:
        return 1
        
    import functools
    return functools.reduce(lambda x, y: x * y, prime_numbers)