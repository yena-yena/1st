#10.6
#(1)
'''
n_list = [44, 66, 34, 24, 144, 98, 38, 568, 234, 345]
new_list = []
for i in range(len(n_list)):
    if n_list[i] % 12 == 0:
        new_list.append(n_list[i])
print('n_list =', n_list)
print('new_list =',new_list)
'''
#(2)
'''
n_list = [44, 66, 34, 24, 144, 98, 38, 568, 234, 345]
new_list = list(filter(lambda a, b : b % a == 0, n_list))
a=12
b=new_list[1]

print('n_list =', n_list)
print('new_list =',new_list)
'''
#10.7
#(1)
'''
n_list = [-22.3, 29.44, 902.2, 45.7, -887.1, -56.3]
new_list = []
for i in range(len(n_list)):

    if n_list[i]>0:
        new_list.append (int(n_list[i]))
print('n_list = ',n_list)
print('new_list =',new_list)
'''
#(2)

n_list = [-22.3, 29.44, 902.2, 45.7, -887.1, -56.3]
new_list = list(map(int,filter(lambda i : i>0, n_list)))
print(new_list)


#(3)------------------------------------------------------------------
'''
n_list = [-22.3, 29.44, 902.2, 45.7, -887.1, -56.3]
new_list = [int(i) for i in n_list if i>0]
print('n_list = ',n_list)
print('new_list =',new_list)
'''

#10.9
#(1)
'''
new_list = []
for i in range(1,101):
    if i % 6 == 0:
        new_list.append(i)
print('new_list =', new_list)
'''

#(2)
'''
new_list = list(filter(lambda i : i%6==0, range(1,101)))
print('new_list =',new_list)
'''


#(3)
'''
new_list = [i*6 for i in range(1,17)]
print('new_list =', new_list)
'''