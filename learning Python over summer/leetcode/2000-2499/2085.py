from import Counter
class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
      count=0
      a = Counter(words1)
      b = Counter(words2)
      for element in words1:
        if a[element]==b[element]==1:
          count+=1
      return count