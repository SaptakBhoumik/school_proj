'''
13. WAP to find the even numbers from a given list of integers.
'''
def get_even_num(lst):
    new_lst=[]
    for i in lst:
        if i%2==0:
            new_lst.append(i)
    return new_lst
lst=[1,2,3,4,5,6,7,8,9,10]
print("Original list:-",lst)
print("Even numbers:-",get_even_num(lst))