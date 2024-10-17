if __name__ == '__main__':
    s = input()
    
# is alphanumeric
# is alphabetical
# is digit
# is lower
# is upper



def string_validation(s):
    validation_list = []
    
    for letter in s: 
        validation_list.append(letter.isalnum())
    if True in validation_list:
        print(True)
    else: print(False)
    validation_list.clear()

    for letter in s: 
        validation_list.append(letter.isalpha())
    if True in validation_list:
        print(True)
    else: print(False)
    validation_list.clear()

    for letter in s: 
        validation_list.append(letter.isdigit())
    if True in validation_list:
        print(True)
    else: print(False)
    validation_list.clear()

    for letter in s: 
        validation_list.append(letter.islower())
    if True in validation_list:
        print(True)
    else: print(False)
    validation_list.clear()

    for letter in s: 
        validation_list.append(letter.isupper())
    if True in validation_list:
        print(True)
    else: print(False)
    validation_list.clear()
    
string_validation(s)

