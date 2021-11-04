s_list = ['abc', 'bcd', 'abc', 'abba', 'cddc', 'opq', 'opq']
new_s_list = []
for i in s_list:
    if i not in new_s_list:
        new_s_list.append(i)

print("s_list =", s_list)
print("new_s_list =", new_s_list)

