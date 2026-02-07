a = int(input())
if a > 10000:
    print("NO")
else:
    for i in range (1, 50):
        if a % 2 != 0:
            print("NO")
            break
        else:
            a = a / 2
            if a == 1:
                print("YES")
                break