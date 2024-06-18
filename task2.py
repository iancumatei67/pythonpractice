from typing import Dict

def set_to_dict(dict_to_update: Dict[str, int], **items_to_set) -> Dict:
    for key, new_value in items_to_set.items():
        if key in dict_to_update:
            if new_value > dict_to_update[key]:
                dict_to_update[key] = new_value
        else:
            dict_to_update[key] = new_value
    return dict_to_update
        
print(set_to_dict({'a': 1, 'b': 2, 'c': 3}, a=0, b=4))
print(set_to_dict({}, a=0))
print(set_to_dict({'a': 5}))