class Solution:
    def modifyString(self, s: str) -> str:
        # loop through the string to find all ?
        # replace the ? with anything other than the after or before 
        # if s if equal to ?
            # return anything
        # setting sets equal to set(s)
        # setting the avaliable characters equal to set()
        # loop through each character in s 
            # if the character is equal to ?
                # if not avaliable characters
                    # avaluable characters are equal to the set of all letters without sets
                # replace the character within s
        if s == '?':
            return 'p'
        sets = set(s)
        avaliable_characters = set()
        for index in s:
            if index == '?':
                if not avaliable_characters:
                    avaliable_characters = set('abcdefghijklmnopqrstuvwxyz').difference(sets)
                s = s.replace(index, avaliable_characters.pop(), 1)
        return s


        # if s == '?':
        #     return 'a'
        # s_set = set(s)
        # available_chars = set()
        # for char in s:
        #     if char == '?':
        #         if not available_chars:
        #             available_chars = set('abcdefghijklmnopqrstuvwxyz').difference(s_set)
        #         s = s.replace(char, available_chars.pop(), 1)
        # return s