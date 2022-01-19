count = 0
flag = False
for a in range(1,151):
    for b in range(1,151):
        for c in range(1,151):
            for d in range(1,151):
                for e in range(1,151):
                    count += 1
                    print(count)
                    if a**5+b**5+c**5+d**5 == e**5:
                        flag = True
if flag == True:
    print(a+b+c+d+e)

