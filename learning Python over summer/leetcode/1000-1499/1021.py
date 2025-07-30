class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        # make a list?
        sList = []
        # temp variable?
        tempVar = ''
        # loop through each instance of the string
        for index in s:
            if index == '(':
                if sList:
                    tempVar+=index
                sList.append(index)
            else:
                sList.pop()
                if sList:
                    tempVar+=index
        return tempVar
        # check if the instance is equal to (
        # check if the list is empty
        # add to the variable the index
        # then add to the list
        # else remove from the list 
        # ifthe list is empty then add index to the variable
        # return the variable

        # st=[]
        # r=""
        # for i in s:
        #     if i=="(":
        #         if st:
        #             r+=i
        #         st.append(i)
        #     else:
        #         st.pop()
        #         if st:
        #             r+=i
        # return r
s = "(()())(())"
response = Solution.removeOuterParentheses(s)
print()
print()
print()
print(response)