def insert_item(my_list,index, item):
    my_list.insert(index,item)
    return my_list

my_list=[1,2,3]
new_list=insert_item(my_list,1,10)
print(new_list)
