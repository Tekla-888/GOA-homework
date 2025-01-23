def lengths_of_strings(strings_list):
    lengths = []
    for string in strings_list:
        length = len(string)
    lengths.append(length)
    return lengths
my_list = ["apple", "banana", "cherry"]
result = lengths_of_strings(my_list)
print(result)

   