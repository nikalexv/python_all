#Methods:
##########################################################################################
#capitalize()                               #isalnum() isalpha() isdigit() True/False    #
#swapcase()                                 #islower()  isupper() isspace()  True/False  #
#title()                                    #txt = 'I am {}, {} years'.format(name, age) #
#lower()                                    #txt = f'I am {name}, {amount} years'        #
#upper()                                    #                                            #
##########################################################################################
#count()                                    #
#startswith() endswith() True/False         #
# find(), rfind()                           #
# index(), rindex()                         #
#replace()                                  #
#strip() lstrip() rstrip()                  #
#############################################
n = int(input())
summ = list()
summ1 = list()

for i in range(0, n):
    summ.append(int(input()))
i = 0
while len(summ) > 1:
    summ1.append(summ[0] + summ[1])
    i += 1
    del summ[0]

print(summ)
print(summ1)
