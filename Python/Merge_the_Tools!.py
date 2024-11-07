'''
s = "AABCAAADA"
k = 3

AB
CA
AD
'''

separated = []
temp = []

def merge_the_tools(string, k):
    for i in range(len(string)):
        temp.append(string[i])
        if (i+1) % k == 0:
            separated.append(temp)
            temp.clear()
    print(separated)
    

s = "AABCAAADA"
k = 3
merge_the_tools(s, k)