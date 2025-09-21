import random
import time
import sys
print("Password Generator")
lowercase_abcs = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
uppercase_abcs = []
for letter in lowercase_abcs:
    uppercase_abcs.append(letter.upper())
_symbols = ["!","@","#","$","%","&","*","<",">","?"]
numbs = ["1","2","3","4","5","6","7","8","9","0"]
while True:
    length_needed = input("How long should the password be (min 8)?: ")
    if length_needed.isdigit() and int(length_needed) >= 8:
        length_needed = int(length_needed)
        break
    print("Please enter a number greater than or equal to 8.")
lowercase = str(input("Should there be lowercase letters in the password? Y/N: "))
if lowercase == "Y":
    lowercase = True
elif lowercase == "N":
    lowercase = False
else:
    print("Please rerun the program to fix your mistake.")
    sys.exit()
uppercase = str(input("Should there be uppercase letters in the password? Y/N: "))
if uppercase == "Y":
    uppercase = True
elif uppercase == "N":
    uppercase = False
else:
    print("Please rerun the program to fix your mistake.")
    sys.exit()
symbols = str(input("Should there be symbols in the password? Y/N: "))
if symbols == "Y":
    symbols = True
elif symbols == "N":
    symbols = False
else:
    print("Please rerun the program to fix your mistake.")
    sys.exit()
numbers = str(input("Should there be numbers in the password? Y/N: "))
if numbers == "Y":
    numbers = True
elif numbers == "N":
    numbers = False
else:
   print("Please rerun the program to fix your mistake.")
   sys.exit()
yes_no = [lowercase, uppercase, symbols, numbers]
requested_lists = yes_no.count(True)
print("Creating your password...")
fake_nums = []
ind = 1
while ind < int(length_needed) - 2:
    fake_nums.append(ind)
    ind = ind + 1
per_list = []
ind = 0
requested_num = 0
while True:
    per_list.append(random.choice(fake_nums))
    ind_inside = 0
    requested_num = 0
    while ind_inside < requested_lists:
        requested_num += (per_list[ind_inside])
        ind_inside += 1
        if ind_inside == len(per_list):
            break
    # :(
    if len(per_list) >= requested_lists and requested_num != int(length_needed) or per_list.count(1) > 0 and int(length_needed) >=8:
        per_list.clear()
        requested_num = 0
    elif len(per_list) == requested_lists and requested_num == int(length_needed):
        break
character_pass = []
perlist_number = 0
if lowercase == True:
    while ind < per_list[0]:
        character_pass.append(random.choice(lowercase_abcs))
        ind = ind + 1
    perlist_number += 1
else:
    perlist_number = 0
ind = 0
if uppercase == True:
    while ind < per_list[perlist_number]:
        character_pass.append(random.choice(uppercase_abcs))
        ind = ind + 1
    perlist_number += 1
else:
    perlist_number = 0
ind = 0
if symbols == True:
    while ind < per_list[perlist_number]:
        character_pass.append(random.choice(_symbols))
        ind = ind + 1
    perlist_number += 1
else:
    perlist_number = 0
ind = 0
if numbers == True:
    while ind < per_list[perlist_number]:
        character_pass.append(random.choice(numbs))
        ind = ind + 1
else:
    perlist_number = 0
#fake_nums.clear()
#for number in range(1,int(length_needed) + 1):
#    fake_nums.append(number)
#random_order = []
#ind = 0
#while ind < len(fake_nums):
#    random_order.append(random.choice(fake_nums))
#    if len(random_order) != len(set(random_order)):
#        random_order.clear()
#        ind = 0
#        continue
#    ind = ind + 1
#final_pass = []
#ind = 0
#while ind < len(random_order):
#    if ind > len(random_order):
#        break
#    final_pass.append(character_pass[random_order[ind] - 1])
#    ind = ind + 1
time.sleep(3)
print("Your new password is:")
time.sleep(1)
#idk = ""
#ind = 0
#for character in final_pass:
#    idk = idk + final_pass[ind]
#    ind += 1
random.shuffle(character_pass)
final_pass2 = character_pass
ind = 0
for char in final_pass2:
    idk2 = idk2 + final_pass2[ind]
    ind += 1
print(idk2)