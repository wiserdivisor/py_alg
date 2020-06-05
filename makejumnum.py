def jmpnum(x, n):
    global s

    if(x>n):return

    s.add(x)
    mod = x%10

    if(mod == 0):
        temp = x*10+(mod+1)
        jmpnum(temp, n)

    elif(mod == 9):
        temp = x*10+(mod-1)
        jmpnum(temp, n)

    else:
        temp = x*10+(mod+1)
        jmpnum(temp, n)

        temp = x*10+(mod-1)
        jmpnum(temp, n)

s  = set()
for _ in range(int(input("No. of testcases :"))):
    n = int(input("Enter limit :"))
    for i in range(0, 10):jmpnum(i, n)
    s=sorted(s)
    for i in s:print(i)
    s = set()
