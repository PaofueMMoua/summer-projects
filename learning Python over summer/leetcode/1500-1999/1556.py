class Solution:
    def thousandSeparator( n: int) -> str:
        # possible add after each 3rd from the back?
        # make a for loop that cycles through backwards
        # add a . after every 3rd section.

        n=str(n)[::-1]
        return '.'.join(n[i:i + 3] for i in range(0, len(n), 3))[::-1]
n = 12345678999
# should result with 12.345.678.999
response = Solution.thousandSeparator(n)
print()
print()
print()
print(response)