
"""fact=1
for i in range(1,n+1):
    fact*=i
    print("factorial=",fact)
n = int(input("Enter a number: "))

digit = len(str(n))
sum = 0

for i in str(n):
    sum += int(i) ** digit

if sum == n:
    print("Armstrong number",sum)
else:
    print("Not Armstrong")
n=int(input("enter a number:"))
a=0
b=1
print("fibnnnaci series:")
for i in range(n):
    print(a,end=" ")
    c=a+b
    a=b
    b=c
n=int(input("enter number:"))
if n<=1:
    print("not prime no.")
else:
    for i in range(2,n):
        if n%i==0:
            print("not prime number")
            break
        else:
            print("prime")
n=int(input("enter a number:"))
temp=n
rev=0
while temp>0:
    d=temp%10
    rev=rev*10+d
    temp//=10
    if rev==n:
        print("its palindrome")
        else:
            print("not")
n=int(input("enter a number:"))
sum=0
for i in range(1,n+1):
    sum=+i
    print("sum is ",sum)
for i in range(1, 5):
    for j in range(i):
        print("*", end=" ")
    print()
list=[1,'n',3,4]
list.append(7)
print(list)
list2=[8,3,4]
list.extend(list2)
print(list)
list.insert(3,4)
print(list)
list.remove(4)
print(list)
b=list.reverse()
print(b)
p=(2,4,4,5,'n')
print(p)
m=p.reverse()
print(m)
a={2,6,3}
b=a
print(b)
set={'1','3'}
print(set)
set.add(9)
print(set)
c={'2':{'0','3'}}
print(c)
def f(n,m):
    return n+m
add= lambda n,m: n+m
print(add(7,9))
def p(n):
    if n<=1:
        return "not prime"
    for i in range(2,int(n**0.5)+ 1):
        if n%i==0:
            return "not prime"
        return "prime"
    c=int(input("number"))
    print(p(c))"""
