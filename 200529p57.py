import re

String = input('Enter a string: ')

pattern = r' '
match = re.findall(pattern,String)

for i in match:
    String = String.replace(i,'_')

print(String)
                            
