def convert_to_C (temperature):
    C = (temperature - 32) * (5 / 9)
    print(C)
Ftemperature = int(input("Enter the temperature in Fahrenheit: "))
convert_to_C(Ftemperature)
