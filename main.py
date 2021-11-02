#Author : Nicole Giron nqg5259@psu.edu
#Collaborator : Youhyun Kim yfk5109@psu.edu
#Collaborator : Geng Niu gjn5124@psu.edu
#Collaborator : Krish Choudhary ksc5496@psu.edu


temperature = float(input("Enter temperature: "))
unit = input("Enter unit in F/f or C/c: ")
temperature = float(temperature)
if unit == "F" or unit == "f":
  print(f"{temperature}\xb0 in Fahrenheit is equivalent to {(temperature-32)*5/9}\xb0 Celsius.")
elif unit == "C" or unit == "c":
  print(f"{temperature}\xb0 in Celsius is equivalent to {temperature*1.8+32}\xb0 Fahrenheit.")
else:
  print(f"Invalid unit({unit}).")
