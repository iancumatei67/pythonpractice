def remove_duplicates(x):
    return list(set(x))

def remove_duplicates_noset(x):
    new_list=[]
    for i in x:
        if i not in new_list:
            new_list.append(i)
    return new_list
    
a = [1, 1, 2, 3, 5, 8, 8, 13, 21, 21, 55, 89]
print(remove_duplicates(a))
print(remove_duplicates_noset(a))