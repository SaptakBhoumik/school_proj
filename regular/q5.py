'''
5. WAP, using function, to create a dictionary D1={'1':'one',
'2':'two', '3':'three', '4':'four'} and also a second dictionary from D1
with opposite mapping, dictionary D2={'4':'four', '3':'three',
'2':'two', '1':'one}
'''
def reverse_dict():
    dict1={'1':'one','2':'two','3':'three','4':'four'}
    dict2={}
    keys=list(dict1.keys())
    size=len(keys)
    for i in range(size):
        key=keys[size-i-1]
        dict2[key]=dict1[key]
    return dict1,dict2

dict1,dict2=reverse_dict()
print("Dictionary:-",dict1)
print("Reverse dictionary:-",dict2)