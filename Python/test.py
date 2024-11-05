def solve(s):    
    result = []
    for letter in range(len(s)):
        if s[letter - 1] == " " or letter == 0:
            result.append(s[letter].upper())
        else: 
            result.append(s[letter])




    final_result = "".join(result)
        

    return final_result


s = "132 456 Wq  m e"
result1 = solve(s)
print(result1)