from collections import deque
d = deque()
 
operations = {
    "append":d.append, 
    "appendleft": d.appendleft,
    "pop": d.pop,
    "popleft": d.popleft
}
for i in range(int(input())):
    op = input().split()
    if len(op)>1:
        x,y = op
        operations[x](int(y))
    else:
        operations[op[0]]()
print(*d) #To unpack function call


