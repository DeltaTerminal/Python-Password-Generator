import random as r

print("Do you want a fixed number of characters password or a variable ?")
type_of_generation = str(input("fixed or variable : "))
input_error = "Next time enter a usable value if you want the code to run correctly."
contains_digit = False
num_times = "5" 
testisdigit = "1234"
num_times_user = "3456"
list_of_lists = [ 'g', 'p', 'q', 'r', 's', 'I', 'J', 'K', 'L', 'T', 'U', 'V', 'W', 't', 'u', 'v', 'h', 'i', 'j', 'a', 'b', 'c', 'd', 'e', 'f', 'k', 'l', 'm', 'n', 'o', 'w', 'x', 'y', 'z', '/', ':', ';', 
'<', '=', '>', '?', '@', '[', ']', '^', '{', '|', '}', '~', '6', '7', '8', '9','0', '1', '2', '3', '4', '5', '/', ':', ';', '<', '=', '>', '?', '@', '[', ']', '^', 
 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'F', 'G', 'H', 'X', 'Y', 'Z', '{', '|', '}', '~', 'A', 'B', 'C', 'D', 'E',]

if 'fixed' in type_of_generation :
   num_times_user = str(input("Password length (05, 10, 12 or 15) : "))
if "variable" in type_of_generation :
   num_times = str(input("Password length (0 to ∞) : "))
else : 
   print("fixed or variable! ")
if num_times.isdigit() :
   contains_digit = True
if contains_digit == False :
   print(input_error)
num_timesint = int(num_times)

def printing():
   print(" ")
   print("This is a strong and randomized password that you can use :")
   print(" ")
   for i in range(num_timesint) :
        r_index = r.randint(0,len(list_of_lists)-1)
        print(list_of_lists[r_index],sep= " ",end= '')
   print("\n ")

def printing05():
   print(" ")
   print("This is a strong and random password that you can use :")
   print(" ")
   for i in range(5) :
        r_index = r.randint(0,len(list_of_lists)-1)
        print(list_of_lists[r_index],sep= " ",end= '')
   print("\n ")

def printing10():
   print(" ")
   print("This is a strong and random password that you can use :")
   print(" ")
   for i in range(10) :
        r_index = r.randint(0,len(list_of_lists)-1)
        print(list_of_lists[r_index],sep= " ",end= '')
   print("\n ")

def printing12():
   print(" ")
   print("This is a strong and random password that you can use :")
   print(" ")
   for i in range(12) :
        r_index = r.randint(0,len(list_of_lists)-1)
        print(list_of_lists[r_index],sep= " ",end= '')
   print("\n")

def printing15():
   print(" ")
   print("This is a strong and random password that you can use :")
   print(" ")
   for i in range(15) :
        r_index = r.randint(0,len(list_of_lists)-1)
        print(list_of_lists[r_index],sep= " ",end= '')
   print("\n")

def ifnot():
   if '05' not in num_times_user :
      if '10' not in num_times_user :
         if '12' not in num_times_user :
            if '15' not in num_times_user :
               print(input_error)

def final_if():
    if "3456" in num_times_user :
       if "3456" not in num_times_user : 
          ifnot()
    if '05' in num_times_user:
                printing05()
    if '10' in num_times_user:
                printing10()
    if '12' in num_times_user:
                printing12()
    if '15' in num_times_user:
                printing15()

if 'variable' in type_of_generation :
   printing()

final_if()
