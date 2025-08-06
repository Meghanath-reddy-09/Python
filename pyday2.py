#starting letters will be captail:

str=input().title()
print(str)

#vowels:

n= input().lower()
c=0
for i in n:
   if i in"aeiou":
       c+=1
print(c)

#LOWER AND UPPER CASE:

n= input()
new_str = ""
for i in n:
    if i.isupper():
        new_str+=i.lower()
    else:
        new_str+=i.upper()
print(new_str)


#LIST SORTING:

li=[1,2,3,4,5,6,7]
a=sorted (li)
print(a[-1])

#largest no:

n= [1,2,5,15,30]
m=n[0]
for i in n:
    if i>m:
        m=i
print(m)


