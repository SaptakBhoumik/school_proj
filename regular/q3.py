'''
3. WAP, using function, to rotate the elements of a list in such
a way that 1st element goes to the 2nd position, 2nd to 3rd, 3rd
to 4th etc. The element in the last position will move to the 1st
position.
'''
def rotate_list(list1):
    list2=[]
    list2.append(list1[-1])
    for i in range(len(list1)-1):
        list2.append(list1[i])
    return list2
list1=[1,2,3,4,5]
print("Original list:-",list1)
print("Rotate list:-",rotate_list(list1))