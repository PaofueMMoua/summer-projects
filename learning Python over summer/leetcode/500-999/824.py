class Solution:
    def toGoatLatin( sentence: str) -> str:
        vowels = ['a','e','i','o','u','A','E','I','O','U']
        # split the sentence to a list of strings
        count = 1
        sentence = sentence.split()
        for index in range(len(sentence)):
            if any(element in vowels for element in sentence[index][0]):
                temp = sentence[index] + 'ma'
            else:
                temp = sentence[index] + sentence[index][0]
                temp = temp.replace(temp[0], '', 1) + 'ma'
            sentence[index] = temp + 'a'* count
            count += 1
        return ' '.join(sentence)
# if the word begind with a e i o u  then add ma to the end
# else move the first letter to the end then add ma to the end
# add a to the end

sentence = "I speak Goat Latin"
response = Solution.toGoatLatin(sentence)
print()
print()
print()
print(response)