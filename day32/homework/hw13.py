def insert_item(my_list, index, item):
     my_list.insert(index, item)
     return my_list
my_numbers = [1, 3, 5]
index = 1
new_item = 2
result = insert_item(my_numbers, index, new_item)
print(result) 