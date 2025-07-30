# open reading file aka file 1
infile = open("ccdata.txt", "r")
# opening writing file aka file 2
outfile = open("emissiondata.txt", "w")
# getting lines from file 1
aline = infile.readline()
# writing to file 2
outfile.write("Year \tEmmision\n")
# while loop for file 1 to get each item from file 1 and pasting it inside of file 2.
while aline:
    items = aline.split()
    dataline = items[0] + '\t' + items[2]
    outfile.write(dataline + '\n')
    aline = infile.readline()
# closing both files.
infile.close()
outfile.close()