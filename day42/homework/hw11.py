def sum_numeric_values(my_dict):
    total_sum = 0
    for value in my_dict.values():
        if isinstance(value, (int, float)):
            total_sum += value
    return total_sum
my_dict = {
    "apple": 1,
    "banana": 2,
    "cherry": "three",
    "date": 4.5,
    "elderberry": 5
}

total = sum_numeric_values(my_dict)
print(f"Sum of numeric values: {total}")