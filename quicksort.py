def pa(ar, lo, hi):
    piv = ar[hi]
    i = lo - 1
    for j in range(lo, hi):
        if(piv>=ar[j]):
            i= i+1
            ar[j],ar[i] = ar[i],ar[j]
    ar[hi],ar[i+1] = ar[i+1],ar[hi]
    return i+1

def qs(ar, lo, hi):
    if(lo<hi):
        pi = pa(ar, lo, hi)
        qs(ar, lo, pi-1)
        qs(ar, pi+1, hi)

ar = [int(input("enter :"))for _ in range(int(input("Enter size :")))]
qs(ar, 0, len(ar)-1)
print(ar)
