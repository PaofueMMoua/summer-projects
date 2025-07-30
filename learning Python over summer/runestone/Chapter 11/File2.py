infile = open("ccdata.txt", "r")
aline = infile.readline()
print("Year\tEmmision\n")
while aline:
    items = aline.split()
    dataline = items[0] + '\t' + items[2]
    print(dataline)
    aline = infile.readline()

infile.close()