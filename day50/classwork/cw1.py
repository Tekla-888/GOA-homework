
def get_user_data_english():
    """Gets user data (e.g., name or surname) and handles various errors."""

    try:
        user_input = input("Enter your name or surname: ")
        if not user_input:  # Check for empty input
            raise ValueError("Input is empty.")
        if not user_input.isalpha(): # check for only letters
            raise ValueError("Input must only contain letters")
        print(f"You entered: {user_input}")

    except ValueError as e:
        print(f"Error: {e}")
    except TypeError:
        print("Error: Incorrect data type.")
    except KeyboardInterrupt:
        print("\nProgram execution interrupted by user.")
    except EOFError:
        print("\nEnd of input.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

get_user_data_english()