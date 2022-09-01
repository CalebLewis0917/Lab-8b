# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Caleb Lewis
# Section:      521
# Assignment:   Lab10a_Act2
# Date:         11 08 2021

file1 = open("game.txt","r")
file2 = open("coins.txt","w")
coins = 0
# Converts game.txt to a list of strings
commands = list(file1)
# Splits each line into two elements, a string and an int
for i in range(len(commands)):
    line = commands[i].split(" ")
    line[1] = line[1].strip("\n")
    if(line[1][0]=='+'):
        line[1] = line[1][1:]
# Check the command and either adds coins, jumps to a different line, or does nothing
    if(line[0]=='coin'):
        coins += int(line[1])
        file2.write(str(line[1]) + "\n")
    elif(line[0]=='jump'):
        i += int(line[1])
    else:
        file2.write('0\n')
print("Total coins: " + str(coins))