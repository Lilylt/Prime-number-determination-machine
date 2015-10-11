import sys
print ('spam',2 ** 16)
a = input('put a number')
b = int(a)
c = 2
while c < b:
    if b % c == 0:
        print(b,c)
        break
    if c == b:
        print ("it is a prime unmber")
        break
    else:
        c = c +1
        print('try')
