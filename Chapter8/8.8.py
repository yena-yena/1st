import random as r

picklist = list()
for i in range(10):
    pick = r.randint(1, 1000)
    picklist.append(pick)
print(picklist)

f = open("random_numbers.txt", "w")
f.write(str(picklist))
f.close()


#f = open("random_numbers.txt", "r")
#s = f.readline()
#f.write(str(picklist))
#f.close()
