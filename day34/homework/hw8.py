#10) Write a function 
# that iterates 
# through a range of numbers 
# (e.g., 1 to 100) and sums up
#  all the numbers divisible by 3.
#  Return the total sum.


def sum_of_numbers_divisible_by_3(start, end):
    total_sum = 0 
    for number in range(start, end + 1):
         if number % 3 == 0:  
            total_sum += number  
            return total_sum 
start_range = 1
end_range = 100
sum_of_divisible_numbers = sum_of_numbers_divisible_by_3(start_range, end_range)
print(f"The sum of numbers divisible by 3 in the range from {start_range} to {end_range}: {sum_of_divisible_numbers}")












