
def answer():

    answ = ""
    currBig = ""
# sets the input to being just the items and then spliting them by the comma's
    #strs = input('input \n')
    strs = '["flower","flow","flight"]'
    strs = strs.strip('",][')
    strs = strs.replace('"', '')
    inputArr = strs.split(',')
    inputArr.sort(key=len)

# checking if the length of the input is equal to 0 aka its empty then its going to return blank
    if len(strs) == 0:
        return currBig
    inputArr.sort()
                
    for i in range(len(inputArr)):
        for j in range(len(inputArr[i])):
            for z in range(len(inputArr)):
                if inputArr[0][z] in inputArr[i][j]:
                    print(inputArr[i][j], inputArr[i])
                    if inputArr[i] is  inputArr[0]:
                        answ += inputArr[i][j]
                        print(answ)
    answ = answ[:-1]
    print(f'"{answ}"')
    return(f'"{answ}"')
answer()