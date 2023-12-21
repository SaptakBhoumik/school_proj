'''
2. WAP, using function, to generate a new list from two
existing lists of same lengths. The new list must contain the
sum value of elements of those two lists of the corresponding
positions.
'''
def sum_of_list(list1,list2):
    list3=[]
    for i in range(len(list1)):
        list3.append(list1[i]+list2[i]) 
    return list3

list1=[1,2,3,4,5]
list2=[6,7,8,9,10]
print("List1:-",list1)
print("List2:-",list2)
print("Sum of list:-",sum_of_list(list1,list2))