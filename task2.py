first, second, third = input().split()
first = int(first)
second = int(second)
third = int(third)

if (first >= 94 and first < 727) and (second >= 94 and second < 727) and (third >= 94 and third < 727):
    if first > second and first > third:
        print(first)
    elif second > first and second > third:
        print(second)
    else:
        print(third)
else:
    print("Error")