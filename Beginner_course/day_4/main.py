# day-4
# integer random number 
import random
# random_number = random.randint(1,10);
# print(random_number);

# float random number 
# random_float = random.randint(0,1);
# if(random_float ==1):
#     print("heads");
# else:
#     print("tails");


# list data types with data method 

# states_nepal = ["koshi","madhesh","bagmati","gandaki","lumbini","kadali","sudurpachim"];

# each element in list is access by using index number from 0-(n-1) 
# print(f"state 1 {states_nepal[0]}");
#list method
#append
# states_nepal.append("new_pradesh");
# print(states_nepal);
# states_nepal.extend(["new_pradesh_1","new_pradesh_2"]);
# print(states_nepal);
# states_nepal.pop();
# print(states_nepal);
# states_nepal.remove("koshi")
# print(states_nepal);

# random pay bill generator

# names_string = input("Give me everybody names, separated by comma(,)");
# name_list =names_string.split(", ");
# print(name_list);
# list_lenght = len(name_list);
# index= random.randint(0,list_lenght-1);
# print(f"bill will paid by {name_list[index]}")

#teasure map game
# row1=["😃","😃","😃"];
# row2=["😃","😃","😃"];
# row3=["😃","😃","😃"];
# map =[row1,row2,row3];
# print (f"{row1}\n{row2}\n{row3}")
# position = str(input("where do you want to put the teasure?"));
# index1= int(position[0]);
# index2 =int(position[1]);
# map[index1][index2]="😘"
# print (f"{row1}\n{row2}\n{row3}")


#rock paper scissors game

