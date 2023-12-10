# this code is just modified from the original setup.py so i dont ruin the original
import os

num = 10

os.makedirs('data', exist_ok=True)
os.makedirs('data/HuPR', exist_ok=True)
os.makedirs('visualization', exist_ok=True)
os.makedirs('logs', exist_ok=True)
os.makedirs('preprocessing/raw_data', exist_ok=True)
os.makedirs('preprocessing/raw_data/iwr1843', exist_ok=True)

for i in range(1, num+1):
    root = 'data/HuPR/'
    dirName = root + 'single_' + str(i)
    dirVertName = dirName + '/vert'
    dirHoriName = dirName + '/hori'
    dirAnnotName = dirName + '/annot'
    dirVisName = dirName + '/visualization'
    os.makedirs(dirName, exist_ok=True)
    os.makedirs(dirVertName, exist_ok=True)
    os.makedirs(dirHoriName, exist_ok=True)
    os.makedirs(dirAnnotName, exist_ok=True)
    os.makedirs(dirVisName, exist_ok=True)