#unique
list_1=[3,6,4,7,6,7,3]
first_sum=sum(list_1)
second_sum=sum(set(list_1))*2
res = second_sum-first_sum
print(res)

#factorial
n = int(input("enter a value:"))
fact=1
for i in range (n,1,-1):
    fact=fact*i
print(fact)

#print sum of first 10 multiples of given no.
n=int(input("enter the value:"))
fact = 0
for i in range (1,11):
    fact +=n*i
print(fact)

#right angle triangle star
n = int(input())
for i in range (1,n+1):
    print("* "*i) 
 
# #for reverse star
n = int(input())
for i in range (n,0,-1):
    print("* "*i)  
    
#for no.s
n = int(input())
for i in range (1,n+1):
    str1=""
    for j in range(1,i+1):
        str1=str1+str(j)+" "
    print(str1)
    
#reverse
n = int(input())
for i in range (n,0,-1):
    str1=""
    for j in range(1,i+1):
        str1=str1+str(j)+" "
    print(str1)

#star pyramid
n=int(input())
for i in range(1,n+1):
    print(" "*(n-i)+"* "*i)