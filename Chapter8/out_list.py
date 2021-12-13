'''def out_lst(fn, lst):
    f = open(fn, 'r')
    for v in lst:
        f.write(str(v) + '\n')
    f.close()
'''

lst = []

f = open('fn.txt', 'w')
for v in lst:
    f.write(str(v) + '\n')
f.close()
