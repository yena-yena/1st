#3.
list=[]
for num in range(1,101):
    if num%2==0:
        list.append(num)
print(list)
#num=n

li=[n for n in range(1,101) if n%2==0]
print(li)

#4.
four=[n*n for n in range(1,10) if n%3==0]
print(four)

nums=[]
for n in range(1,10):
    if n%3==0:
        nums.append(n*n)
    for i in nums:
        print(i, end=',')