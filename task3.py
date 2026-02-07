first, second, third = input().split()
first = int(first)
second = int(second)
third = int(third)

if first >= second + third:
    print("YES")
else:
    print("NO")