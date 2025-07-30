class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        # split everything in the jewels string to a list of strings
        tempJewels = list(jewels)
        count = 0
        # find all instances of anything in jewels in stones
        for character in range(len(stones)):
            if any(element in tempJewels for element in stones[character]):
                count += 1
        return count
        # add to the count when there was a instance.

jewels = "z"
stones = "ZZzZZZZzZZZzzzzzZZ"

response = Solution().numJewelsInStones(jewels, stones)

print()
print()
print(response)