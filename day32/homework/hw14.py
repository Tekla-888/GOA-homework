def insert_item_at_beginning(my_list, item):
     my_list.insert(0, item)
     return my_list
my_numbers = [1, 2, 3]
new_item = 0
result = insert_item_at_beginning(my_numbers, new_item)
print(result)