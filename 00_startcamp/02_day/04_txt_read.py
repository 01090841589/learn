#1 파일 읽기(옛날방식)\
# f= open('ssafy.txt', 'r')
# all_text = f.read()
# print(all_text)
# f.close()

#2. 파일 읽기

# with open('with_ssafy_txt', 'r') as f :
#     all_text = f.read()
#     print(all_text)

#파아ㅣㄹ 읽기 옛날방식  read
# f = open('ssafy.txt', 'r')
# lines = f.readlines()

# for line in lines :
#     print(lines)
#     print(line)
# f.close

with open('with_ssafy_txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        print()
        print(line.strip())