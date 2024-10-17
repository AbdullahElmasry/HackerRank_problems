# qA2
s = "qA2"
validation_list = []

for letter in s:
    validation_list.append(letter.isdigit())
if True in validation_list:
    print(True)
else: print(False)
validation_list.clear()