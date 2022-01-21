s = input()
#s = s.lower()
count = 0
max_c = 0
for i in range(len(s)):
    if s[i] == 'r':# and  s[i+1] == s[i]: 
        count += 1
        if max_c < count:
            max_c = count
    else:
        count = 0

print(max_c)
