class Solution:
    def removeDuplicates( s: str) -> str:
        #  make s a list
        stack=[s[0]]
        #  iterate through that list to find if something is equal to the one after it. 
        for i in range(1,len(s)):
            if(stack and stack[-1]==s[i]):
                stack.pop()
            else:
                stack.append(s[i])
        return "".join(stack)
        # remove the one after it 
        # 
s = "abbaca"
response = Solution.removeDuplicates(s)
print()
print()
print()
print(response)