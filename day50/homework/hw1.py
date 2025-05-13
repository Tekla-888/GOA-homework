def access_list_element():
    """Creates a list and handles IndexError."""
    my_list = [10, 20, 30]

    try:
        index = int(input("Enter an index to access: "))
        element = my_list[index]
        print(f"Element at index {index}: {element}")
    except IndexError:
        print("Error: Index is out of range. Please enter an index between 0 and", len(my_list) - 1)
    except ValueError:
        print("Error: Invalid input. Please enter an integer index.")

access_list_element()