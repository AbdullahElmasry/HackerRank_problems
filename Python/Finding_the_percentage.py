if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

# 3
# Krishna 67 68 69
# Arjun 70 98 63
# Malika 52 56 60
# Malika >> querey_name
summ = 0
lenth = len(student_marks[query_name])
val_list = student_marks[query_name]

for i in range(lenth):
    summ =  summ + val_list[i]

percentage = summ/lenth
print(f"{percentage:.2f}") # Suiiiiiiiiii