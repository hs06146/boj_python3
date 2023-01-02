a, b = input().split()

if int(b) > 44 :
    print(a, int(b)-45)
elif int(b) < 45 and int(a) > 0 :
    print(int(a)-1, int(b)+15)
else :
    print(23, int(b)+15)