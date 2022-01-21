n = int(input())

sp1 = [ (input()) for i in range(n) ]
for i in range(n):
    for c in 'anton':
        if c in sp1[i]:
            sp1[i] = sp1[i][sp1[i].find(c):]
           # print(sp1[i])
            flag = True
        else:
            flag = False
            break
        #print(flag)    
    if flag == True:
        print(i+1, end=' ')

