# Complete the solve function below.
def solve(s):
    words = s.split()
    for word in words:
        word.capitalize()
        result = ' '.join(word)
        

    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
