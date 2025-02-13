#9) Define a function that takes 
# a list of i
# ntegers and returns
# a new list containing
#  only the positive numbers.
#  Use a loop and a conditional
#  statement.


def check_positive(numbers_list):
    for number in numbers_list:
        if number>0:
            print(f"{number} is positive")
        else:
            print(f"{number} is not positive")
numbers=[1,-2,3,4,-5,6,7,8,9,10]
check_positive(numbers)











