def append_item(my_list, item):
    my_list.append(item)
    return my_list

my_numbers = [1, 2, 3]
new_item = 4
result = append_item(my_numbers, new_item)
print(result)