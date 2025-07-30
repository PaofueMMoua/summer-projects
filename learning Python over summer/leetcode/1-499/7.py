x = -123

x = str(x)
if '-' in x:
    x = x.replace('-', '')
    print(x)
    x = x[::-1]
    x = '-' + x
else:
    x = x[::-1]
x = int(x)
print(x)