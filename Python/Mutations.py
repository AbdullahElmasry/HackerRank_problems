def mutate_string(string, position, character):
    # abracadabra
    # 5 k
    str_ls = list(string)
    str_ls[position] = character
    string = "".join(str_ls)

    return string



if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)