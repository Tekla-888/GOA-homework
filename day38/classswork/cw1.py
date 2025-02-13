#n=[1,2,3]
#n=n.index(2)
#print(n)


def no_duplicates(user_list):
    return list(set(user_list))

   
print(no_duplicates([1,1,2,3]))
print(no_duplicates([1,2,2,3]))
print(no_duplicates([1,2,3,3,3]))
    

