

#Exercise 1.1: Temperature Converter

print("Temperature Converter")
print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")
print("3. Celsius to Kelvin")
print("4. Kelvin to Celsius")

choise = input("choose conversion type 1-4 : ")
tempreture = float(input("Enter the temperature to convert: "))
if choise == '1':
    result = (tempreture * 9/5) + 32
    print(f"{tempreture}°C is equal to {result}°F")
elif choise == '2':
    result = (tempreture - 32) * 5/9
    print(f"{tempreture}°F is equal to {result}°C")
elif choise == '3':
    result = tempreture + 273.15
    print(f"{tempreture}°C is equal to {result}K")
elif choise == '4':
    result = tempreture - 273.15
    print(f"{tempreture}K is equal to {result}°C")
else:
    print("Invalid choice.")

