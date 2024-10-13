if __name__ == '__main__':
    ls = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        ls.append([name, score])

ls.sort(key=lambda x: x[1])
lowest_score = ls[0][1]
filtered_ls = []

new_ls = []
# copy_ls = []
# copy_ls = ls[:]

# check for more lowest values and delete it
for x in ls:
    if x[1] != lowest_score:
        filtered_ls.append(x)

second_lowest = filtered_ls[0][1]         
# new_ls.append(filtered_ls[0][0])

# To check if there are value similar to the second lowest, then add it
for i in filtered_ls:
    if i[1] == second_lowest:
        new_ls.append(i[0])

new_ls.sort()

for j in range(len(new_ls)):
    print(new_ls[j])