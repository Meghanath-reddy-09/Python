#amstrong
n=str(input())
s = 0
power = len(n)
for i in n:
    s+=int(i)**power
if s==int(n):
    print("is amstrong")
else:
    print("not amstrong")

#prime
def is_prime(m):
     is_prime = True
     if m<=1:
         is_prime=False
     else:
        for i in range(2,int(m**0.5)+1):
            if m%i==0:
                is_prime = False
                break
     if is_prime:
        print(m,"is a prime")
m= int(input())
for i in range(1,m+1):
    is_prime(i)