#Write a program that reads the temperature in degrees Celsius from the keyboard. 
# The program then calculates and displays the temperature in Kelvin and Fahrenheit

celsius=float(input("Insert temperature in Celsius: "))
kelvin=celsius+273.15
fahrenheit=(celsius*9/5)+32

print("Temp in Kelvin: " + str(kelvin) + "\nTemp in Fahrenheit: " + str(fahrenheit) + " .")
