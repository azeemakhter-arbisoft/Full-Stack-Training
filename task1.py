import re


def retain_first_occurance (input_string):
    
    temp_string = input_string.lower()
    temp = set(temp_string)
    for char in temp:
        pateren = re.compile(char, re.I)
        first_occurance = temp_string.index(char)
        input_string = input_string[: first_occurance+1] \
               + pateren.sub('', input_string[first_occurance:])
        

    return input_string

def remove_first_occurance(input_string):
    temp = set()
    for char in input_string:

        count_of_character = input_string.count(char)

        if(count_of_character > 1 and char not in temp):
            input_string = input_string.replace(char, '',1)
            temp.add(char)

    return input_string

input_string = input("please enter a string: ")
output = retain_first_occurance(input_string)
print("Output String is: " + output)
output1 = remove_first_occurance(input_string)
print("Output String is: " + output1)
