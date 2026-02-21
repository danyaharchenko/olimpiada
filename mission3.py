import sys
import math

sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

while True:
    try:
        line = input()
        x1, y1, r1, x2, y2, r2 = map(int, line.split())
        
        distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
        
        if distance <= r1 + r2 and distance >= abs(r1 - r2):
            print("YES")
        else:
            print("NO")
        
    except EOFError:
        break