abc = 'abcdefghijklmnopqrstuvwxyz'
ABC = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
s = input().split()
string = ''

for e in s:
    step = len([i for i in e if i.isalpha()])
    for c in e:
        if c in abc:
            string += abc[(abc.find(c) + step) % 26]
        elif c in ABC:
            string += ABC[(ABC.find(c) + step) % 26]
        else:
            string += c
    string += ' '

print(string[:-1])
