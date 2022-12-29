print("Welcome To The BMI Calculator")
weight=int(input("Enter your weight:"))
height=float(input("Enter your height:"))
bmi=weight/height**2
if bmi<18.5:
  print("Your underweigth")
elif bmi>=18.5 and bmi<25:
  print("Your normal weight")
elif bmi>=25 and bmi<30:
  print("Your overweigt")
else:
  print("Obesity")
