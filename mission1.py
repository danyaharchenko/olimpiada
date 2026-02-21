import sys

sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

while True:
    try:
        line = input()
        line = int(line)
        
        if line == 12 or line == 1 or line == 2:
            print("Winter")
        elif line == 3 or line == 4 or line == 5:
            print("Spring")
        elif line == 6 or line == 7 or line == 8:
            print("Summer")
        elif line == 9 or line == 10 or line == 11:
            print("Autumn")
        else:
            print("Error")
    except EOFError:
        break
