up = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
lo = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
b=''
a=input()
for i in range(len(a)):
    if a[i].isalpha():    
        if a[i].isupper():
            c=up.find(a[i])
            b+=up[(c+10)%32]
        else:
            c=lo.find(a[i])
            b+=lo[(c+10)%32]        
    else:
        b+=a[i]
print(b)
