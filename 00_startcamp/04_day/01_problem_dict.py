# #1. 평균을 구하세요

# score = {
#     '수학':80,
#     '국어':90,
#     '음악':100
# }
# total = 0
# subject = 0
# for value in score.values() :
#     total += value
#     subject += 1
# print(total/subject)

# #2. 반 평균을 구하세요. ->전체 평균
# scores = {
#     'a' : {
#         '수학':80,
#         '국어':90,
#         '음악':100
#     },
#     'b': {
#         '수학':85,
#         '국어':90,
#         '음악':100
#     }
# }

# for key in scores.keys() :
#     for value in key.values():
#         total += value
#         subject += 1
# print(total/subject)

touch 