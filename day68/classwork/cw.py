#Disemvowel Trolls

def disemvowel(string):
    vowels = "aeiouAEIOU"
    res = ""

    for i in string:
        if i not in vowels:
            res += i

    return res

#quare Every Digit

def square_digits(num):
    return int("".join([str(int(d)**2) for d in str(num)]))




def high_and_low(numbers):
    nums = list(map(int, numbers.split(" ")))
    return f"{max(nums)} {min(nums)}"





def high_and_low(numbers):
    nums = numbers.split()
    int_nums = []

    for i in nums: int_nums.append(int(i))

    return f"{max(int_nums)} {min(int_nums)}"






def descending_order(num):
    num_str = str(num)
    sorted_digits = sorted(num_str)[::-1]
    sorted_str = ''.join(sorted_digits)
    return int(sorted_str)



