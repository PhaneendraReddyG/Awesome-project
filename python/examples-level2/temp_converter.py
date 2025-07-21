# temperature_celsius = 30

# F = temperature_celsius *(9/5)+32
# K = 273 + temperature_celsius

# print(f"Temperature in Fahrenheit:{F}")
# print(f"Temperature in Kelvin:{K}")



temp_input = int(input("Enter the Temperature:"))

temp_units = input("Enter the Temperture units K/C/F:").upper()

temp_faren = 0
temp_celsius = 0
temp_kelvin = 0

if temp_units == 'C':
    temp_faren = temp_input*(9/5)+32
    temp_kelvin = 273 + temp_input
    print(f"Temperature in Kelvin:{temp_kelvin}\nTemperature in Fahrenheit:{temp_faren}")
elif temp_units == 'F':
    temp_celsius = (temp_input-32)* 5/9
    temp_kelvin = temp_celsius + 273
    print(f"Temperature in Celsius :{temp_celsius}\nTemperature in Kelvin:{temp_kelvin}")

elif temp_units == 'K':
    temp_celsius = temp_input-273
    temp_faren = temp_celsius * 9/5 +32
    print(f"Temperature in Celsius :{temp_celsius}\nTemperature in Fahrenheit:{temp_faren}")
else:
    print("Invalid temp inputs")


