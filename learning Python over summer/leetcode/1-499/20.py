class Solution:
    def isValid(self, s: str) -> bool:
# get s 
        problemString = s
        
# make a list to append the characters to
        stringList = []

# check how many characters are in s and return false if there arent any or is a odd amount and if it begins with an ending or is empty
        if len(problemString) % 2 != 0 or problemString[0] == ')' or problemString[0] == '}' or problemString[0] == ']' or problemString[0] == '':
            return False
        
# check to see what the string s has 
        for char in problemString:

# check for openings like ({[ then append to the list
            if char == '(' or char == '[' or char == '{':
                stringList.append(char)

# check for endings like )}] then append to the list
            if char == ')' or char == '}' or char == ']':

# check if the string list is empty and if it is then return false
                if len(stringList) == 0:
                    return False

# if the endings come out of order then return false
                if stringList[-1] == '(' and char == ')':
                    stringList.pop()
                elif stringList[-1] == '{' and char == '}':
                    stringList.pop()
                elif stringList[-1] == '[' and char == ']':
                    stringList.pop()
                else:
                    return False
        if len(stringList) != 0 and char == problemString[-1]:
            return False
        if len(stringList) == 0 and char == problemString[-1]:
            return True

# whatever goes in last has to come out first

# check if the opening has a closing part

# s = "()"
# s = "()[]{}"
# s = "(]"
# s = "([])"


response = Solution().isValid(s)

print()
print()
print(response)