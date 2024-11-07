'''
s = "AABCAAADA"
k = 3

AB
CA
AD
'''

separated = []
temp = []
result = []

def merge_the_tools(string, k):
    for i in range(len(string)):
        temp.append(string[i])
        if (i+1) % k == 0:
            separated.append(temp[:]) # we save copy of tmep bc of dear python is not saving a copy of the values, it instead save them by refrence, that's mean that if we edit the source the others will be affected
            temp.clear()
    print(separated)
# separated = [['A', 'A', 'B'], ['C', 'A', 'A'], ['A', 'D', 'A']]
    for part in separated:
        for i in range(len(part)):
            if part[i] != part[i-1]: 
                result.append(part[i])
    
    
    print(result)
            

    # print(f"this is the result: {result}")

        

s = "AABCAAADA"
k = 3
merge_the_tools(s, k)