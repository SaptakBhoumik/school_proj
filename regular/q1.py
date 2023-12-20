'''
1. WAP for given a list
pairs=[[2,5],[4,2],[9,8],[12,10]], count the number of pairs [a,b]
such that both a,b are even
'''
def count_even_pairs(pairs):
    count=0
    for pair in pairs:
        if pair[0]%2==0 and pair[1]%2==0:
            count+=1
    return count
pairs=[[2,5],[4,2],[9,8],[12,10]]
print("Pairs:-",pairs)
print("No of pair in which both the number are even:-",count_even_pairs(pairs))