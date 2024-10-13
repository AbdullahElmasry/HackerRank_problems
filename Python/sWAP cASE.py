def swap_case(s):

    swaped = []

    # "helLOW woRLd"    
    for i in s:
        if i.isupper() :
            swaped.append(i.lower())
        elif i.islower():
            swaped.append(i.upper())
        else:
            swaped.append(i)
        
    final_swap = ''.join(swaped)
    
    return final_swap



if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)