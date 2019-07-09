import os

os.chdir(r'C:\Users\student\TIL\00_startcamp\02_day\dummy')
#                          ^ ^
for filename in os.listdir('.') :
    # os.rename(filename, f'SAMSUNG_{filename}')
    os.rename(filename, filename.replace('SAMSUNG_','SSAFY_'))