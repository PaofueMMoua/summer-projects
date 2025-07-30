class Solution:
    def freqAlphabets(self, s: str) -> str:
        # get the string
        # begin from the back of hte string and check if the last index is a #
            # extract the numbers before the #
            # map the number with a num + 96
            # add to the list
        # if it isnt a # then its a single digit number then convert to a int using int()
            # extract the single digit number then map it using the same num + 96 method
            # add to the list
        # reverse the list and add it together

        i=len(s)-1
        str1=""
        while(i>=0):
            if (s[i]=="#"):
                num=int(s[i-2:i])
                i=i-3
            else:
                num=int(s[i])
                i-=1
            str1=chr(num+96)+str1
        return str1