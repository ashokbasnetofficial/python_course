# for loop in py
fruits = ["apple","banana","grapes"];
for fruit in fruits:
    print(fruit);
height = [134,154,167,172,176,165];
sum =0
for h in height:
    sum +=h;
average_height = sum/len(height);
average_height=round(average_height,2)
print(average_height);


# heightest score finding challenge 
student_score = [90,56,76,65,87,41,96,89,67];
for score in student_score:
 list =[];
no_students = int((input("Please enter the number of students")));
for student in range(0,no_students):
    ele=int(input());
    list.append(ele)
print(list)
max=0;
for i in range(0,no_students):
    if(list[i]>=max):
        max=list[i];
print(f"maximum score:{max}");

# for loop
for i in range(1,10,2):
    print(i)
# add even number from 2 to 100
index = int(input("please enter the range of number"))
sum =0;
for i in range(2,index+1,2):
    sum+=i;
print(f"even number sum of 2 to {index}={sum}")
# for score in student_score:
list =[];
no_students = int((input("Please enter the number of students")));
for student in range(0,no_students):
    ele=int(input());
    list.append(ele)
print(list)
min=list[0];
for i in range(0,no_students):
    if(list[i]<=min):
        min=list[i];
print(f"minimum score:{min}");

# *************************fizz buzz game *****************************************

for i in range(1,100+1):
    if(i%3==0 and i%5==0):
        print("fizzbuzz\n");
    elif(i%3==0):
        print("fizz\n");
    elif(i%5==0):
        print("buzz\n");
    else:
        print(i,"\n");
       

# password generator program 
import string;
import random;
letters = list(string.ascii_uppercase+string.ascii_lowercase);
digits = list(string.digits);
symbols = ['@','#','!','%','(',')','*','&','$']
print("Welcome to password generator!");
total_password_char = int(input("How many character should be in your password?:\n"));
total_symbol =int(input("How many symbol should included?\n"));
total_number=int(input("How many digits should be included?:\n"));
generatedPassword=[];
# random character *****************
for i in range(0,total_password_char):
 rand_char_index = random.randint(0,len(letters)-1);
 generatedPassword.append(letters[rand_char_index])
# random symbol ****************************
for i in range(0,total_symbol):
 rand_symbol_index =random.randint(0,len(symbols)-1);
 generatedPassword.append(symbols[rand_symbol_index])
 # total number************************
for i in range(0,total_number):
 rand_digit_index=random.randint(0,len(digits)-1);
 generatedPassword.append(digits[rand_symbol_index]);
randomPassword =''
for char in generatedPassword:
 random_index = random.randint(0,len(generatedPassword)-1);
 randomPassword+=generatedPassword[random_index];
print("Your newly generated password:",randomPassword);