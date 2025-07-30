from itertools import permutations

a = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
list = []

for i in permutations(a):
    list.append(i)
    print(list)

# class Solution:
#     def permute(self, nums: List[int]) -> List[List[int]]:
        # find possible permutaitons
        # these can range from different things like 
        # abc bca acb bac cab cba 