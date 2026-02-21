import sys

sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

while True:
    try:
        line = input()
        a, b, c = line.split()

        b = int(b)//6
        a = int(a)//2
        c = int(c)
        
        if a < b and a < c:
            print(a)
        elif c < b and c < a:
            print(c)
        elif b < a and b < c:
            print(b)

    except EOFError:
        break