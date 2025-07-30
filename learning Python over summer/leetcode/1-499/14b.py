from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        word = strs[0]
        prefix = ""

        for index in range(len(word)):
            char = word[index]

            for owi in range(1, len(strs)):
                ow = strs[owi]

                if index >= len(ow):
                    return prefix


                owChar = ow[index]

                if char != owChar:
                    return prefix

            prefix += char

        return prefix

    #     answ = ''
    #     if len(strs) == 1:
    #         return strs

    # # checking if the length of the input is equal to 0 aka its empty then its going to return blank
    #     if len(strs) == 0:
    #         return(f'"{answ}"')
    #     for i in range(len(strs)):
    #         for j in range(len(strs[i])):
    #             for z in range(len(strs)):
    #                 if strs[0][z] in strs[i][j]:
    #                     print(strs[i][j], strs[i])
    #                     if strs[i] is  strs[0]:
    #                         answ += strs[i][j]
    #                         print(answ)

    #         if answ[0] != strs[i][0]:
    #             return('')
    #     answ = answ[:-1]

        # return(answ)
    

#strs = ["dog", "god", "daff"]
# strs = ["flower","flow","flight"]
# strs = ["dog","racecar","car"]
strs = ["a"]


response = Solution().longestCommonPrefix(strs)

print()
print()
print(response)