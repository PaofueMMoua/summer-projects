class Solution:
    def reformatNumber(self, number: str) -> str:
        res = ""
        number = re.sub('[^0-9]','',number)
        while len(number) > 4:
            res += number[:3] + '-'
            number = number[3:]
        if len(number) == 4:
            res += number[:2] + '-' + number[2:]
        else:
            res += number
        return res