'''
4. WAP, using function, to create a third dictionary from two
dictionaries having some common keys, in a way so that the
values of common keys must added in the third dictionary.
'''
def merge_dictionaries(dict1, dict2):
    merged_dict = {}
    for key in dict1:
        if key in dict2:
            merged_dict[key] = dict1[key] + dict2[key]
    return merged_dict
dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 10, 'c': 20, 'd': 30}
merged = merge_dictionaries(dict1, dict2)
print("Dictionary 1:-",dict1)
print("Dictionary 2:-",dict2)
print("Merged dictionary:-",merged)

