class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        
        increase = 0
        decrease = len(s)
        my_list = []

        for i in str(s):
            if i == "I":
                my_list.append(increase)
                increase += 1

            elif i == "D":
                my_list.append(decrease)
                decrease -= 1

        my_list.append(increase)

        return my_list