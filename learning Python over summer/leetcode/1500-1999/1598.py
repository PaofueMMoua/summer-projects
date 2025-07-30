class Solution:
    def minOperations( logs: [str]) -> int:
        # set a variable for answers
        ans = 0
        # loop through each instance of logs
        for log in logs: 
        # if the log is equal to ./ then continue
        # if the log is ../ then the answer should equal the maximum number from 0 to answer -1
        # else the answer should add one as it moves into a folder.
            if log == "./": continue
            elif log == "../": ans = max(0, ans-1) # parent directory
            else: ans += 1 # child directory 
        return ans 

logs = ["d1/","d2/","../","d21/","./"]
result = Solution.minOperations(logs)

print()
print()
print()
print()
print(result)