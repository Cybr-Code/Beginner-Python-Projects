# This is a project I am attempting to make without python modules
# Need to actually use the bottom list now!
print("Number to Text Form Conversion!")
unfiltered_comment = input("What would you like to convert?: ")

one2twenty_num2string = {
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "six",
    "7": "seven",
    "8": "eight",
    "9": "nine",
    "10": "ten",
    "11": "eleven",
    "12": "twelve",
    "13": "thirteen",
    "14": "fourteen",
    "15": "fifteen",
    "16": "sixteen",
    "17": "seventeen",
    "18": "eighteen",
    "19": "nineteen",
    "20": "twenty",
}
print("Hi")

def number_to_word(number):
    print("number_to_word")
while True:
    if unfiltered_comment.strip().isdigit():  
        # It's a number
        filtered_comment = unfiltered_comment.strip()
        result = number_to_word("filtered_comment")
        break
    else:  
        # They are words/symbols
        print("Please put a number to convert!")

print(filtered_comment)