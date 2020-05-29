import re
Phone = input('Enter a phone number:')
pattern = r'\d{2,4}-\d{3,5}-\d{4}'
match = re.findall(pattern, Phone)

if len(match) == 1 and len(Phone) >= 11 and len(Phone) <=13:
    pattern_seoul = r'02-\d{3,5}-\d{4}'
    match_seoul = re.findall(pattern_seoul, Phone)
    if len(match_seoul) == 1:
        print('서울사람입니다')
    else:
        print('서울사람이 아닙니다')
else:
    print('wrong input')
    
