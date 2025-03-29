def get_number_input():
  """Prompts the user for a number and handles invalid input."""
  while True:  # Loop until valid input is received
    try:
      user_input = input("Enter a number: ")
      number = float(user_input)  # Attempt to convert to float
      return number  # Return the number if conversion is successful
    except ValueError:
      print("Error: Invalid input. Please enter a valid number.")

# Example usage:
user_number = get_number_input()
print(f"You entered: {user_number}")