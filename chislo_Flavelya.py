n, k = int(input()), int(input())

sp_num = [ i for i in range(1, n+1)]

while len(sp_num) != 1:
    for i in range(k-1):
        sp_num.append(sp_num[0])
        del sp_num [0]
    del sp_num [0]

print(*sp_num)
