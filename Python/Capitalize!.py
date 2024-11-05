def solve(s):    
    result = []
    for letter in range(len(s)):
        if s[letter - 1] == " " or letter == 0:
            result.append(s[letter].upper())
        else: 
            result.append(s[letter])




    final_result = "".join(result)
        

    return final_result

#//////////// you can replace this hackerrank shit with this following code to test \\\\\\\\\\\\\\\\#
# s = "132 456 Wq  m e"
# result1 = solve(s)
# print(result1)
#/////////////////////////////////////////////////////\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\#


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
