class Solution:
    def repeatedCharacter(s: str) -> str:
        # change s to a dictionary and when one of the letters lands again then itll change to return that letter.
        sCharCount = {}
        for character in s:
            sCharCount.setdefault(character, 0)
            sCharCount[character] += 1
            if sCharCount[character] == 2:
                return character
s = "abccbaacz"
response = Solution.repeatedCharacter(s)
print()
print()
print()
print(response)