a = input()

if int(a) % 4 == 0 and int(a) % 100 != 0 or int(a) % 400 == 0 :
    print(1)
else :
    print(0)