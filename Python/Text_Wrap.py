import textwrap
    
def wrap(string, max_width):
    result = ""

    for index in range(0, len(string),max_width): # Iterate over every $max_width elements
        step_elements = [] # reseting every step

        for elem in string[index:index+max_width]:
            step_elements.append(str(elem))
        
        result += "".join(step_elements) + "\n"

    return result

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)