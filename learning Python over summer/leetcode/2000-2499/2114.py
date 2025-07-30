class Solution:
    def mostWordsFound( sentences: [str]) -> int:
        # use a for loop to loop through each string of sentences.
        count = 0
        for i in range(len(sentences)):
            if len(sentences[i].split()) > count:
                count = len(sentences[i].split())
        return count
        # get the amount of words from each one.
        # return the one with the greatest amount of words

        alternative 

        count = 0
        for i in sentences:
                # max() gives you the largest value
                count = max(count, len(i.split(' ')))
        return count
    
        alternative 

        return max(len(i.split()) for i in sentences)


sentences = ["alice and bob love leetcode","i think so too","this is great thanks very much"]
response = Solution.mostWordsFound(sentences)
print()
print()
print()
print(response)