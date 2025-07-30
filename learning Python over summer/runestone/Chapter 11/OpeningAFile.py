infile = open("ccdata.txt", "r")
line = infile.readline()
while line:
    values = line.split()
    print('In', values[0], 'the average temp. was', values[1], '°C and CO2 emmisions were', values[2], 'gigatons.')
    line = infile.readline()

infile.close()