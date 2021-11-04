a, b, c, d, e = input("5개의 수를 입력하세요 : ").split()
a, b, c, d, e = int(a), int(b), int(c), int(d), int(e)
n_list = [a, b, c, d, e]
print("합 :", sum(n_list))
print("평균 :", sum(n_list)/len(n_list))
print("최댓값 :", max(n_list))
print("최솟값 :", min(n_list))
