# day -3 python 
# conditonal statement 
num = int(input("please enter the number: "));
if(num%2==0):
    print(f"{num} is even number!")
else:
    print(f"{num} is odd number!")

#check rider with age
# nested conditional statement 
height = int(input("enter your height(in cm):"));
if(height>=120):
 print("Congrats! you are eligible for ride vehicle.")
 age = int(input("enter your age(years)"));
 if(age>=18):
  print("please pay for $18");
 else:
  print("please pay for $7");
else:
 print("Sorry, you have to grow taller before you can ride.")
    
#bmi 2.0
h = float(input("please enter your height: "));
w= float(input("please enter your weight: "));
bmi = w/h**2
if(bmi<18.5):
    print(f"your bmi is {bmi}, you are underweight.");
elif bmi>=18.5 and bmi<25:
    print(f"your bmi is {bmi}, you are normal weight.");
elif bmi>=25 and bmi<30:
    print(f"your bmi is {bmi}, you are overweight.");
elif bmi>=30 and bmi<35:
    print(f"your bmi is {bmi}, you are obese.");
elif bmi>=35:
    print(f"your bmi is {bmi}, you are clincially obese.");
else:
    print("invalid input")

# ***********************************************************
# leap year
# ***********************************************************

year = int(input("Please enter the year (e.g., 2020): "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")

# ***********************************************************
# leap year
# ***********************************************************
