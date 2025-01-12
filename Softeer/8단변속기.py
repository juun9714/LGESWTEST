import sys

def asc(DTC):
    ret=True
    for i in range(8):
        if i+1 != DTC[i]:
            ret=False
            break
    return ret

def desc(DTC):
    ret=True
    for i in range(8):
        if i+1 != DTC[7-i]:
            ret=False
            break
    return ret

input=sys.stdin.read
data=input().split()
DTC=[]

for i in range(8):
    DTC.append(int(data[i]))

if asc(DTC)==True:
    print("ascending")
elif desc(DTC)==True:
    print("descending")
else:
    print("mixed")
