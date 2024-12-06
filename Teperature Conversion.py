unit= input ("Emter unit of input temperature (F/C):")
if unit=="F":
    temp=float(input("Input temperature:"))
    new_temp= (5 *(temp-32))/9
    print("Temperature in Celsius:", new_temp)
else:
    temp=float(input("Input temperature:"))
    new_temp= (temp * 9/5)+32
    print("Temperature in Farheneit:", new_temp)