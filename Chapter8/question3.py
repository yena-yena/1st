list1 = [1, 3, 5, 7, 9]
list2 = [2, 4, 6, 8, 9]
list3 = [2, 4, 6, 8, 0]


def check(checklist1, checklist2):
    for i in checklist1:
        if i in checklist2:
            result = True
        else:
            result = False

    if result == True:
        print(True)
    else:
        print(False)


check(list1, list2)
check(list1, list3)

