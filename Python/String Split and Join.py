def split_and_join(line):
    # >> This commented method would not work bc in python we can't edit the string's elements by index.
    # >> Instead we can use replace() and that would be more easier.
    #/////////////////////////
    # space = ' '
    # for i in range(len(line)):
    #     if line[i] == space:
    #         line[i] = '-'
    #/////////////////////////

    new = '-'.join(line.split())

    return new




if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)