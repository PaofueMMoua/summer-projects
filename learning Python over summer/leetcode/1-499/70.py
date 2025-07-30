class Solution:
    def climbStairs(self, n: int) -> int:
        answ = 0
        if n % 2 != 0:
            n -= 1
            answ += 1
        if n % 2 == 0:
            n /= 2
            answ += n
        