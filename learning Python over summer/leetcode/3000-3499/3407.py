class Solution:
    def hasMatch(self, s: str, p: str) -> bool:
        # use a split
        left_part, right_part = p.split('*')
        # find the left part
        left_idx = s.find(left_part)
        # find the right part only after the left part
        right_idx = s.find(right_part, left_idx + len(left_part))
        # return the left part and the right part
        return left_idx != -1 and right_idx != -1