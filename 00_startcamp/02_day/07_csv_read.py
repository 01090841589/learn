# with open("lunch.csv", 'r', encoding='utf-8') as f :
#     lines = f.readlines()
#     for line in lines:
#         # print(line.strip())
#         print(line.strip().split(','))

with open("lunch.csv", 'r', encoding='utf-8') as f :
    lines = csv.reader(f)
    print(lines)

    for line in lines:
        print(line)