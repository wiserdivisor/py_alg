n = 11
for _ in range(9):
    print(n)
    s = str(n)
    m = int(s[::-1])
    while(n!=m):
        n+=9
        print(n, end="")
    n+=1
