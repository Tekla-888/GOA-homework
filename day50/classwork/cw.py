


def type_error_example_english():
    """Creates an integer variable, attempts to add it to a string, and handles TypeError."""

    my_integer = 10
    my_string = "Hello"

    try:
        result = my_string + my_integer
        print(result)  # This line will not execute due to the TypeError
    except TypeError:
        print("Error: Cannot concatenate string and integer. You must convert the integer to a string first.")

type_error_example_english()

