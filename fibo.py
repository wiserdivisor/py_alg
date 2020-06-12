l = [0,1]
for _ in range(int(input())-2):
    l.append(l[-1]+l[-2])
print(l)
