lunch = {
    '양자강' : '13ㄱ2ㄹㅈㄷ213ㄹ',
    '김밥' : '124ㄱㄹㅇ',
    '냉면집' : '13ㄹㄷㅈ'
}

#1. 방법 1

with open('lunch.csv', 'w', encoding='utf-8') as f:
    for item in lunch.items():
        f.write(f'{item[0]}, {item[1]}\n')