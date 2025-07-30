# with <create some object that understands context> as <some name>:
#     do some stuff with the object

with open('mydata.txt') as md:
    print(md)
    for line in md:
        print(line)
print(md)