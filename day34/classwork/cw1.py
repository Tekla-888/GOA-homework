def remove_one_element(my_list, index):
    my_list = [1, 2, 3, 4, 5]
    new_list = my_list
    new_list.pop(index)
    return new_list

index_to_remove = 2

result = remove_one_element(my_list, index_to_remove)
print(result)