b = int(input('검은 공의 개수 x를 입력하세요.(단, x>=1): '))
w = int(input('흰 공의 개수 y를 입력하세요.(단, x+y>=2): '))
p = (2*b*w)/((b+w)*(b+w-1))
print(p)
