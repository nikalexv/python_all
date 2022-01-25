n = int(input())

def pascal(n):
    x = list()
    if n == 0:
        x =  [1]
        return print(x)
    else:
        for i in range(1, n+2):
            x.append([1]*i)
        
        for i in range(2, len(x)):
            for j in range(1, len(x[i])-1):
                x[i][j] = x[i-1][j-1]+ x[i-1][j]
       
        return print(x[len(x)-1])
pascal(n)
