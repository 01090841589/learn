with open('writelines_ssafy.txt', 'r') as f:
    lines = f.readlines()

lines.reverse()

with open('reverse_ssafy.txt', 'w') as f:
    for line in lines:
        f.write