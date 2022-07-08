''' Convert the temperature from celcius to farenheit'''


def convert(temp):  # define the function
    return temp*1.8+32  # formulae to convert degree celcius to farenheit


t = int(input("Enter the temperature in celcius: "))
final = convert(t)
print("Temperature in farenheit is ", final)
