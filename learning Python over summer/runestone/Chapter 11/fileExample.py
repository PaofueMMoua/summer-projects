f = open("studentdata.txt", "r")

for aline in f:
# get each line in the file
# check if the scores are greater than 6 
# begin at index [1:] because the namem is always the first thing in the file.
    items = aline.split()
    if len(items[1:]) > 6:
        print(items[0])

f.close()