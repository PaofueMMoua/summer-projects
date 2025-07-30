# class Solution:
#     def romanToInt(self, s: str) -> int:

s = input('give a roman numeral \n') 
total = 0

x = 0
j=1

char = list(s)

for x in range(len(char)):
    if x == len(char) or x >= len(char) -1:
        break
    j = x+1
    if char[x] == 'C' and char[j] == 'M':
        char[x] = 1
        char[j] = 1
        x-=1
        j = x+1
        total += 900
    elif char[x] == 'C' and char[j] == 'D':
        char[x] = 1
        char[j] = 1
        x-=1
        x+1
        total += 400
    elif char[x] == 'X' and char[j] == 'C':
        char[x] = 1
        char[j] = 1
        x-=1
        j = x+1
        total += 90
    elif char[x] == 'X' and char[j] == 'L':
        char[x] = 1
        char[j] = 1
        x-=1
        j = x+1
        total += 40
    elif char[x] == 'I' and char[j] == 'X':
        char[x] = 1
        char[j] = 1
        x-=1
        j = x+1
        total +=9
    elif char[x] == 'I' and char[j] == 'V':
        char[x] = 1
        char[j] = 1
        x-=1
        j = x+1
        total += 4
    # else:
    #     break
    if len(char) == 0 or len(char) == 1:
        break

for x in range(len(char)): 
    if char[x] == 'M':
        total+=1000
        char[x] = 1
    elif char[x] == 'D':
        total+=500
        char[x] = 1
    elif char[x] == 'C':
        total+=100
        char[x] = 1
    elif char[x] == 'L':
        total+=50
        char[x] = 1
    elif char[x] == 'X':
        total+=10
        char[x] = 1
    elif char[x] == 'V':
        total+=5
        char[x] = 1
    elif char[x] == 'I':
        total+=1
        char[x] = 1
    if len(char) == 0:
        break
    
# I = 1
# V = 5
# X = 10
# L = 50
# C = 100
# D = 500
# M = 1000



print(char)

print(total)