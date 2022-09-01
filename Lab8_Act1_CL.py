# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Ashley McAlister
#               Sarah Smeltzer
#               Caleb Lewis
#               Botao Zeng
# Section:      521
# Assignment:   Lab8
# Date:         10 25 2021

# Variables
v_list = [] # (list of specific volumes)
u_list = [] # (list of specific internal energies)
h_list = [] # (list of specific enthalpy values)
s_list = [] #(list of specific entropy values)
temp_list = [] # (list of temperatures ranging from 0 to 260 K)
user_temp = [] # (value that the user inputs)

temp_min = 0 # (index of minimum temperature from inputted temperature)
temp_max = 0 #(index of maximum temperature from inputted temperature)

# Calculate the values for each property using the linear interpolation formula
volume = ((v_list[temp_max]-v_list[temp_min])/(temp_list[temp_max]-temp_list[temp_min]))*(user_temp-temp_list[temp_min])+v_list[temp_min]
energy = ((u_list[temp_max]-u_list[temp_min])/(temp_list[temp_max]-temp_list[temp_min]))*(user_temp-temp_list[temp_min])+u_list[temp_min]
enthalpy = ((h_list[temp_max]-h_list[temp_min])/(temp_list[temp_max]-temp_list[temp_min]))*(user_temp-temp_list[temp_min])+h_list[temp_min]
entropy = ((s_list[temp_max]-s_list[temp_min])/(temp_list[temp_max]-temp_list[temp_min]))*(user_temp-temp_list[temp_min])+s_list[temp_min]