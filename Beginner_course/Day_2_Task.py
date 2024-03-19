# day 2 task 
# day-2 project tips calculator

# primitive data types

# **********************************
# 1. string data type 
first_name ="Ashok";
last_name="Basnet";
# how should we get last alphabet 'k' from above name

print(first_name[4]) 

# string concatination using + sign 
# print(first_name+" "+last_name)

#number
# a=3
# b=4
# print(a+b)

#float

pi = 3.14
r = float(input("please input radius"));
A= pi*r*r
print("area of the circle is:",round(A,2));


#write a program to adds 2 digits of two digit number
num = 35
num = str(num);
first =int(num[0]);
second = int(num[1]);
print(first+second)


# # math operation 
# # operator precedence  () ** * / + -
# # 2+1 #add
# # 4/2 #divide
# # 4**2 # power
# # write a program that calculates the Body Mass Index(BMI) from a user's weight and height.
height = int(input("enter the height: "));
weight= int(input("enter the weight: "));
BIM = weight/ height**2
print("BIM=",BIM)

# score =0;
# score+=1;
# print(score)


# f-string 
# print(f"the score {score}");
 
current_age = int(input("enter age:"));
remaining_years =90-current_age;
total_days = remaining_years*365
total_week = remaining_years*52
total_months = remaining_years*12

print(f"you have {total_days}, {total_week} weeks and {total_months} days left")

#---------------- day-2 final task  -------------------
# tips calcualtor 

print("Welcome to the tip calcualtor.");
total_bill = float(input("What was the total bill?"));
total_person = int(input("How many people to split the bill?"));
tips_percent = float(input("What percentage tip would you like to give? 10, 12, or 15?"));
tips_percent = float(tips_percent/100);
per_person_bill = float(total_bill/total_person);
per_person_bill+=per_person_bill*tips_percent;
per_person_bill=round(per_person_bill,2);
print("each person will pay: ",per_person_bill);
