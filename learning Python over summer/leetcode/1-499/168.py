class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        dictCol = {}
        if not columnNumber:
            return ""
        # checking if hte column number 
        columnNumber, remainder = divmod(columnNumber - 1, 26)
        return self.convertToTitle(columnNumber) + chr(65 + remainder)

 # if 1-26 then assign accordingly. attempt enumerate?
  #
        


columnNumber = 2147483647
# columnNumber = 2147483647
# columnNumber = 3
# columnNumber = 4
# columnNumber = 5
response = Solution().convertToTitle(columnNumber)
