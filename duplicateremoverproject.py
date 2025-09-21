print("Duplicate Remover")
notstripped = str(input("What is the list needed to be stripped of duplicates? (seperate with commas): "))
notstripped_list = []
for character in notstripped:
    notstripped_list.append(character)
space_stripped = []
for item in notstripped_list:
    if not item == " ":
            space_stripped.append(item)
fullstripped_list = []
for item in space_stripped:
    if not item == ",":
            fullstripped_list.append(item)
# This is the painful and beginner way to remove duplicates
noduplicates_list = []
recent_duplicates = []
for item in fullstripped_list:
    if fullstripped_list.count(item) == 1:
        noduplicates_list.append(item)
    else:
        if not item in recent_duplicates:
            noduplicates_list.append(item)
            recent_duplicates.append(item)
printing_statement = ""
for item in noduplicates_list:
    printing_statement = printing_statement + item + ","
print_list = []
for character in printing_statement:
    print_list.append(character)
del print_list[-1]
printwithout_comma = ""
for item in print_list:
    printwithout_comma += item
print(printwithout_comma)