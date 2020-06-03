import re

data = '''apple-사과,banana-바나나,lemon-레몬,eraser-지우개,pencile-연필,python-파이
썬,fire-불,integer-정수,yonsei-연세,function-함수,clock-시계,potato-감자'''

w = input('Enter a word : ')

while w not in data:
     print("Sorry there's no such word")
     w = input('Enter a word : ')

pattern = r'[\w]+-[\w]+'
match = re.findall(pattern, data)

for i in range(len(match)-1):
    if w in match[i]:
        m = match[i]

print('The word means',m)
