# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Ashley McAlister
#               Sarah Smeltzer
#               Caleb Lewis
#               Botao Zeng
# Section:      521
# Assignment:   Lab8a
# Date:         10 25 2021

# Initialize lists for each property

v_list = [0.0009977, 0.0009996, 0.0010057, 0.0010149, 0.0010267, 0.0010410, 0.0010576, 0.0010769, 0.0010988, 0.0011240, 0.0011531, 0.0011868, 0.0012268, 0.0012755]
u_list = [0.04, 83.61, 166.92, 250.29, 333.82, 417.65, 501.91, 586.8, 672.55, 759.47,847.92, 938.39, 1031.6, 1128.5]
h_list = [5.03, 88.61, 171.95, 255.36, 338.96, 422.85, 507.19, 592.18, 678.04, 765.09, 853.68, 944.32, 1037.7, 1134.9] 
s_list = [0.0001, 0.2954, 0.5705, 0.8287, 1.0723, 1.3034, 1.5236, 1.7344, 1.9374, 2.1338, 2.3251, 2.5127, 2.6983, 2.8841]
temp_list = [0, 20, 40, 60, 80, 100, 120, 140, 160, 180, 200, 220, 240, 260, 261]

# Get temperature value from user
# Cast temp to float
user_temp = float(input("Enter a temperature between 0 and 260 deg C: "))
# Check value is within the acceptable range of 0-260
if (user_temp > 260 or user_temp < 0):
  print("Invalid Temperature!")
else:
  # Initialize variables for each property
  volume = 0.0
  energy = 0.0
  enthalpy = 0.0
  entropy = 0.0
  # Get the two temperature values closest to inputted temperature
  temp_min = 0 # index of minimum temp value from inputted temp value
  temp_max = 0 # index of max temp value from inputted temp value

  for i in range(len(temp_list) - 1):
      if (temp_list[i] <= user_temp and temp_list[i + 1] > user_temp):
          temp_min = i
          temp_max = i + 1
  
  # Checking if the inputted temperature is a known temperature 
  # therefore linear interpolation isn't necessary
  if (temp_list[temp_max] == user_temp):
        volume = v_list[temp_max]
        energy = u_list[temp_max]
        enthalpy = h_list[temp_max]
        entropy = s_list[temp_max]
  elif (temp_list[temp_min] == user_temp):
      volume = v_list[temp_min]
      energy = u_list[temp_min]
      enthalpy = h_list[temp_min]
      entropy = s_list[temp_min]
  else:
      # Use Linear Interpolation to get volume
      volume = ((v_list[temp_max]-v_list[temp_min])/(temp_list[temp_max]-temp_list[temp_min]))*(user_temp-temp_list[temp_min])+v_list[temp_min]
      # Use Linear Interpolation to get energy
      energy = ((u_list[temp_max]-u_list[temp_min])/(temp_list[temp_max]-temp_list[temp_min]))*(user_temp-temp_list[temp_min])+u_list[temp_min]
      # Use Linear Interpolation to get enthalpy
      enthalpy = ((h_list[temp_max]-h_list[temp_min])/(temp_list[temp_max]-temp_list[temp_min]))*(user_temp-temp_list[temp_min])+h_list[temp_min]
      # Use Linear Interpolation to get entropy
      entropy = ((s_list[temp_max]-s_list[temp_min])/(temp_list[temp_max]-temp_list[temp_min]))*(user_temp-temp_list[temp_min])+s_list[temp_min]


  # Print calculated values for each value 
  print("Properties at {} deg C are:".format(user_temp))
  print("Specific volume (m^3/kg): {:.7f}".format(volume))
  print("Specific internal energy (kJ/kg): {:.2f}".format(energy))
  print("Specific enthalpy (kJ/kg): {:.2f}".format(enthalpy))
  print("Specific entropy (kJ/kgK): {:.4f}".format(entropy))