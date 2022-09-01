# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Caleb Lewis
# Section:      521
# Assignment:   Lab10a_Act2
# Date:         11 08 2021

fileName = input("Please enter the output filename: ")
P = float(input("Please enter the principal amount: "))
N = int(input("Please enter the term length (months): "))
i = float(input("Please enter the annual interest rate: "))
month = 0
total_interest = 0.00
interest = 0.00
J = i/12
M = (P*J)/(1-(1/(1+J))**N)
M = round(M,2)
print(M)
print(P)
file = open(fileName,"w")
file.write("Month,Total Accrued Interest,Loan Balance\n")
file.write("0,$0.00" + "," + str(P) + "\n")
while(P>=.01):
    interest = P*J
    interest = round(interest,2)
    total_interest += interest
    P -= M
    P += interest
    P = round(P,2)
    print(P)
    month += 1
    file.write(str(month) + ",$" + str(total_interest) + ",$" + str(P) + "\n")
