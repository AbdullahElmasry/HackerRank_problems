import textwrap

def printing(index):

    to_be_printed = string[last_index:index]
    print(to_be_printed)
    last_index = index



def wrap(string, max_width):
    counter = 0
    for index in range(len(string)):
        # new line \n every max_width ex:4 steps
        counter += 1
        if counter == 4:
            printing(index)
            counter = 0

    return

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)