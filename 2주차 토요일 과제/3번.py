str = input()
ps=list(str)
openP=[]
VPS=True
for i in range(len(str)):
    if str[i] == '(':
        openP.append('(')
        ps.pop()
    else:
        if not len(openP):
            VPS = False
        else:
            openP.pop()
if not VPS:
    print("NO")
else:
    if not len(openP):
        print("YES")
    else:
        print("NO")