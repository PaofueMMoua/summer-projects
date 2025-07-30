class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        	dictm = {'a': '0', 'b': '1', 'c': '2', 'd': '3', 'e': '4', 'f': '5', 'g': '6', 'h': '7', 'i': '8', 'j': '9'}

    s1 = ''.join([dictm[i] for i in firstWord])
    s2 = ''.join([dictm[i] for i in secondWord])
    s3 = ''.join([dictm[i] for i in targetWord])

    return (int(s1) + int(s2)) == int(s3)