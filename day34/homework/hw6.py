#8) Find the Maximum
#Create a function
#  that takes a list
#  of numbers and uses 
# a loop to find and
#  return the maximum
#  number.


def find_maximum_with_max(numbers_list):
    if not numbers_list:
     return None

    return max(numbers_list)
numbers = [5, 2, 9, 1, 5, 6]
maximum_number = find_maximum_with_max(numbers)
print(f"The maximum number in the list is: {maximum_number}")


