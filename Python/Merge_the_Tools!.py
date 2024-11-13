'''
s = "AABCAAADA"
k = 3

AB
CA
AD
'''

# >>> this is first approach which will work for few test cases <<<

# def merge_the_tools(string, k):
#     separated = []
#     temp = []
#     result = []
#     for i in range(len(string)):
#         temp.append(string[i])
#         if (i+1) % k == 0:
#             separated.append(temp[:]) # we save copy of tmep bc of dear python is not saving a copy of the values, it instead save them by refrence, that's mean that if we edit the source the others will be affected
#             temp = []

#     # now we will make this separated list unique first
#     for part in separated:
#         unique_list = []
#         for unique_letter in part:
#             if unique_letter not in unique_list:
#                 unique_list.append(unique_letter)
#         temp.append(unique_list)
#     # temp = [['A', 'B'], ['C', 'A'], ['A', 'D']]


#     # converting the 2D list into a 1D array 
#     for sub_list in temp:
#         for letter in sub_list:
#             result.append(letter)

#     # print(list(result))

#     semi_final = ""
#     final_string = ""
#     step = int(len(result)/k) # EX: k = 3 >> step = 6/3 = 2

#     for i in range(0, len(result), step):
#             semi_final += ''.join(result[i:i + step]) + "\n"

#     final_string = semi_final.rstrip("\n")
#     print(f"{final_string}")


# Second approach, better one (i hope so).
def merge_the_tools(string, k):
    for i in range(0, len(string), k):
        part = string[i:i+k]

        unique_part = []
        for letter in part:
            if letter not in unique_part:
                unique_part.append(letter)
        
        print("".join(unique_part))


s = "AABCAAADA"
k = 3
merge_the_tools(s, k)