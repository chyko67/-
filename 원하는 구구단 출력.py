def Input():
    flag = True
    while flag:
        n = input('구구단 중 원하는 단의 숫자를 입력해주세요(1부터 9까지의 정수 중). : ')
        x = ['1','2','3','4','5','6','7','8','9']
        print('\n')
        if n in x:
            flag = False
            return n
        else:
            print('1부터 9까지의 정수 중 하나를 다시 입력해주세요.\n')

n = Input()

N = int(n)
print('-------[%d단]-------'%N)
for i in range(1,10):
    print('%d X'%N,i,'= %d'%(N*i))
