class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        magazineCharCount = {}

        for character in magazine:
            magazineCharCount.setdefault(character, 0)
            magazineCharCount[character] += 1

        for randsomChar in ransomNote:
            if magazineCharCount.get(randsomChar, 0) > 0:
                magazineCharCount[randsomChar] -= 1
            else:
                return False

        return True

response = Solution.canConstruct()

print(response)