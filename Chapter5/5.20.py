src = ['aaaabbb', 'aaaabccccaaaaacccfg']


print("src =", src[0])

print("src =", src[1])


s = input('5개의 수를 입력하세요: ')

n_list = []
for n in s.split():
    n_list.append(int(n))

print('합:', sum(n_list))
print('평균:', sum(n_list) / len(n_list))
print('최댓값:', max(n_list))
print('최솟값:', min(n_list))
