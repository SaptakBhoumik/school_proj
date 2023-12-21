def binary_search(arr, target, low=0, high=None):
    if high == None:
        high = len(arr) - 1
    if low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            return binary_search(arr, target, mid + 1, high)
        else:
            return binary_search(arr, target, low, mid - 1)
    else:
        return -1
lst=[1,2,3,4,5,6,7,8,9,10]
print("Original list:-",lst)
target=int(input("Enter the number to be searched:-"))
s=binary_search(lst,target)
if s==-1:
    print("Number not found")
else:
    print("Number found at index",s)