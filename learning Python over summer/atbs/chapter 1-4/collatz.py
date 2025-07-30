X = True
number = 0
def collatz(number):
    global X
    global number
    if number == 1:
        X = False
    elif number == 0:
        X = False

    if number % 2 != 0:
        print(3*number+1)
        number = 3*number+1
    else:
        print(number//2)
        number = number//2
    
collatz(int(input('input a number. \n')))

while X == True:
    collatz(number)