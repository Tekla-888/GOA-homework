def delete_elements_by_index(main_list, indexes_list):
    new_list = main_list.copy()
    for index in sorted(indexes_list, reverse=True):
     new_list.pop(index)

    return new_list
main_list = [1, 2, 3, 4, 5]
indexes_list = [2, 0]

result = delete_elements_by_index(main_list, indexes_list)
print(result) 