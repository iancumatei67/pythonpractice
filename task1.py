#Write function which deletes defined element from list.
#Restriction: Use .pop method of list to remove item.
#Examples:
#    >>> delete_from_list([1, 2, 3, 4, 3], 3)
#    [1, 2, 4]
#    >>> delete_from_list(['a', 'b', 'c', 'b', 'd'], 'b')
#    ['a', 'c', 'd']
#    >>> delete_from_list([1, 2, 3], 'b')
#    [1, 2, 3]
#    >>> delete_from_list([], 'b')
#    []

from typing import List, Any


def delete_from_list(list_to_clean: List, item_to_delete: Any) -> List:
    while item_to_delete in list_to_clean:
        index_to_delete = list_to_clean.index(item_to_delete)
        list_to_clean.pop(index_to_delete)
    return list_to_clean

#initial_list = [1, 2, 3, 4, 5, 6]
#item_to_remove = 2
#cleaned_list= delete_from_list(initial_list, item_to_remove)
#print(cleaned_list)

print(delete_from_list([1, 2, 3, 4, 3], 3))            
print(delete_from_list(['a', 'b', 'c', 'b', 'd'], 'b')) 
print(delete_from_list([1, 2, 3], 'b'))                 
print(delete_from_list([], 'b')) 