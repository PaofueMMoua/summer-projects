class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        # get the length strs
        # a for loop that is in the range of the len of strs index 0
        m = len(strs)
        n = len(strs[0])
        count = 0

        for i in range(n):
            for j in range(1,m):
                if strs[j][i] < strs[j-1][i]:
                    count += 1
                    break
        return count



        # m, n = len(strs), len(strs[0])
        # count = 0
        
        # for i in range(n):
        #     for j in range(1,m):
        #         if strs[j][i] < strs[j-1][i]:
        #             count += 1
        #             break
        
        # return count