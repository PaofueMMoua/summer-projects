class Solution:
    def isLongPressedName( name: str, typed: str) -> bool:
        # make a index variable
        nameindx, typeindx = 0, 0
        # make a length variable
        namelen, typedlen = len(name), len(typed)
        # prob use a while loop to cycle through each index of the length of typed
        while typeindx < typedlen:
            # check if the name index is less than the name length 
            # check if the name index is equal to the typed index
            if nameindx < namelen and name[nameindx] == typed[typeindx]:
                # add one to the name index and typed index
                nameindx += 1
                typeindx += 1
            # else check if the name index is greater than 0 to make sure it has something in it
            # check to make sure that the name index -1 isnt equal ot teh type index
            elif nameindx > 0 and name[nameindx - 1] == typed[typeindx]:
                # if they are then add one ot the type index
                typeindx += 1
            else:
                # else return false 
                return False
            # return if the name indx is equal to the name length.
        return nameindx == namelen
        

name = "alexx"
typed = "lexxa"

response = Solution.isLongPressedName( name, typed)
print()
print()
print()
print(response)