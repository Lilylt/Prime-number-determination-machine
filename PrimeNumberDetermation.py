import sys
a = input('put a number')
b = int(a)
c = 2
while c < b:
    if b % c == 0:
       print(b,'is not a prime number')
       print ('the factor of ',b,'is',c)
       break
    else:
       c = c +1
while c == b:
    print ('it is a prime number')
    break
while c > b :
    print ('1 and 0 is not a prime number')
    break