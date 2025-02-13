#7) Write a function
# that takes a list
# of numbers and checks
# whether each number
# is even or odd using 
# a loop and conditional
#statements. Print 
# "Even" for even
# numbers
#and "Odd" for odd 
# numbers.

def check_even_odd(numbers_list):
    for number in numbers_list:
        if number % 2==0:
            print(f"{number}-even")
        else:
            print(f"{number}-odd")
numbers=[1,2,3,4,5,6,7,8,9,10]
check_even_odd(numbers)




