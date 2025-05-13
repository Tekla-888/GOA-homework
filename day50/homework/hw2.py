def add_integer_to_string():
    """Tries to add an integer to a string and handles TypeError."""
    my_string = "Hello"
    my_integer = 10

    try:
        result = my_string + my_integer
        print(result)  # This line will not be executed due to the TypeError
    except TypeError:
        print("Error: Cannot concatenate string and integer. You must convert the integer to a string first.")

add_integer_to_string() 