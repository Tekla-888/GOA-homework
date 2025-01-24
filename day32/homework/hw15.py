def insert_item_at_end_with_insert(my_list, item):
    my_list.insert(len(my_list), item)
    return my_list
my_numbers = [1, 2, 3]
new_item = 4
result = insert_item_at_end_with_insert(my_numbers, new_item)
print(result)