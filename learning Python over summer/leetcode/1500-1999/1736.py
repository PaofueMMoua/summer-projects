class Solution:
    def maximumTime(self, time: str) -> str:
        h1 = time[0]
        h2 = time[1]
        m1 = time[3]
        m2 = time[4]
        if h1 == '?':
            if h2 == '?' or (h2 != '?' and int(h2) <= 3):
                h1 = "2"
            else:
                h1 = "1"
        if h2 == '?':
            if h1 == '1' or h1 == '0':
                h2 = '9'
            elif h1 == '2':
                h2 = '3'
        if m1 == '?':
            m1 = '5'
        if m2 == '?':
            m2 = '9'
        return f'{h1}{h2}:{m1}{m2}'