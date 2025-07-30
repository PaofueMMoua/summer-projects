class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
 
# TODO: get s and t
# TODO: loop through s
        newSVariable = {}
        lists = []
    # TODO:replace each instance of s to what it is in t
    # make a loop that loops through each character of s
        
        # change every character in newSVariable to whatever character it is in t?
        # for character in range(len(s)):
        #     newSVariable.setdefault(s[character], ' ')
        #     newSVariable[s[character]] = t[character]
        
        # print(newSVariable)

        for i in range(len(s)):
            if s[i] not in newSVariable:
                if t[i] not in lists:
                    newSVariable[s[i]]= t[i]
                    lists.append(t[i])
                else:
                    return False
            elif newSVariable[s[i]]!=t[i]:
                return False
        return True

        
# for i in range(len(s)):
#             if s[i] not in map_dict:
#                 if t[i] in t[:i]:
#                     return False
#                 map_dict[s[i]] = t[i]
#             elif map_dict[s[i]] != t[i]:

#                 return False
        
#         return True
        # remove all the characters from t?
    # TODO: check if they are the same
    # TODO: return true
# TODO:return False

s = 'abab'
t = 'baba'
result = Solution.isIsomorphic(s, s, t)

print()
print()
print()
print()
print(result)