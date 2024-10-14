def count_substring(string, sub_string):
    # Input:
    # DCDC
    # CDC
    
    counter = 0
    copy_string = string
    ls_copy_string = list(copy_string) # turning to list because string is immutable from assigning


    for _ in range(len(string)):
        index = copy_string.find(sub_string) # if not found returns -1
        if index != -1:
            counter += 1
            del ls_copy_string[0:index+1] # delete the elements before the first occurance including the first letter of the subString
    
    
    return counter






if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)