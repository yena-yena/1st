score=[11,22,33,44,55,66,77,88]
sum=0
for i in range(1,8):
    sum=sum+score[i]
    print("sum",'=',sum)
    print('average','=',sum/len(score))
#score의 인덱스 번호는 0,1,...7로 7까지 뿐이다. 그런데 3번째 문장에서 처음엔 for i in range(1,9)라고 했고 결국 index error 가 났다 list index out of range.