#Write a program that calculates the Body Mass Index (BMI) 
#based on your height in cm and weight in kg. 
##The user enters the data from the keyboard. 
#Find the formula on the Internet for calculating BMI. 
##Then, using your program, check that you have the correct weight. Sample result:
height=int(input("Enter your height in cm:"))
weight=int(input("Enter your weight in kg:"))

he=height/100
he=he**2
BMI=weight/he
print(BMI)