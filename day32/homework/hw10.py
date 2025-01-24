def append_list_to_list(original_list, items_to_append):
    original_list.extend(items_to_append)
    return original_list
my_numbers = [1, 2, 3]
new_items = [4, 5, 6]
result = append_list_to_list(my_numbers, new_items)
print(result) 