numbers = [x for x in range(1, 101) if (x % 3 == 0 or x % 5 == 0) and not (x % 3 == 0 and x % 5 == 0)]

print(numbers)