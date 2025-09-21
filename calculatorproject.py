print("Calculator")
initial_equation = input("Please enter your equation: ")
stripped_equation = ""
for character in initial_equation:
    if character != " ":
        stripped_equation = stripped_equation + character
print(stripped_equation)
stripped_equation_list = []
for character in stripped_equation:
    stripped_equation_list.append(character)
operators = ['+','-']
operatorindex_in_equation = []
operator_in_equation = []
for item in stripped_equation_list:
    if item in operators:
        operatorindex_in_equation.append(stripped_equation_list.index(item))
        operator_in_equation.append(item)
PEMDAS = ['+','-']
if "+" in operator_in_equation:
    before = operatorindex_in_equation[operator_in_equation.index(+)] - 1
    after = operatorindex_in_equation[operator_in_equation.index(+)] + 1
