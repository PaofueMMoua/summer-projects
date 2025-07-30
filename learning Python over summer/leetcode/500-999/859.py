class Solution:
    def buddyStrings(s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        different_letters = [(a, b)for a, b in zip(s, goal)if a != b]
        if len(different_letters) != 2:
            return not different_letters and len(set(s)) < len(s)
        (a1, b1), (a2, b2) = different_letters
        return a1 == b2 and b1 == a2
s = "ab"
goal = "ba"
result = Solution.buddyStrings(s, goal)

print()
print()
print()
print()
print(result)