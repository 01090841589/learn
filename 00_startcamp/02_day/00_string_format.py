# name = '홍길동'
# english_name = 'hong'

# print('안녕하세요 {}입니다. My name is {}'.format(name, english_name))

# namu = '홍길동'
# print(f'안녕하세요, {name}입니다.{english_name}')

# import random

# menu = ['1','2','3','4','5']
# lunch = random.choice(menu)
# print('오늘의 점심은 {}입니다.'.format(lunch))
# print(f'오늘의 점심은 {lunch}입니다.')

import random

numbers = list(range(1,46))
res = random.sample(numbers,6)
print(sorted(res))