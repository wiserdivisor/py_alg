import re
##Unfinished.
for _ in range(int(input())):
    s = input()
    if all([re.search(r, s)for r in[r'^[456]',r'([0-9]{13}[-]{3})|([0-9]{16})',r'\d{4}(?![_\s])\d{4}',r'(-?\d{4}-\d{4})']]):
        print("Valid")
    else:
        print("Invalid")
