i = 0
j = 0

for x in range(len(t)):
    if s[i] == t[j]:
        i += 1
        j += 1
    else:
        j += 1