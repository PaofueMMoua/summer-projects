class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:

        sSegment = []
        s = s.replace('-', '').upper()
        # Determine the size of the first group
        mod = len(s) % k
        # Use a list for efficient string building
        # Add the first group if it is not empty
        if mod > 0:
            sSegment.append(s[:mod])
        # Add the remaining groups
        for i in range(mod, len(s), k):
            sSegment.append(s[i:i+k])
        # Join segments with a dash
        return '-'.join(sSegment)

response = Solution.thousandSeparator(n)
print()
print()
print()
print(response)