import re
[print(x,end='\n')for _ in range(int(input()))for x in re.findall(r':?.(#[0-9A-Fa-f]{3,6})',input())]
