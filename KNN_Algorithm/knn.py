from cmath import sqrt
from tkinter import Image
import numpy as NP
from PIL import Image
from pathlib import Path
from time import time
import math

def calcDistance(pixel1, pixel2):
    return math.sqrt((pixel1[0]-pixel2[0])**2 + (pixel1[1]-pixel2[1])**2 + (pixel1[2]-pixel2[2])**2)

def countImgDistance(files, type):
    for file in files:
        img = Image.open(file)
        img.resize((500, 300))
        dis = 0
        for (pixel1, pixel2) in zip(testImg.getdata(), img.getdata()):
            dis += calcDistance(pixel1, pixel2)
        distance.append([dis, type])

K = 3


files1, files2 = Path('summer').glob('*'), Path('winter').glob('*')

testImg = Image.open('day-2.jpg')
testImg.resize((500, 300))

distance = list()

countImgDistance(files1, 'summer')
countImgDistance(files2, 'winter')

distance.sort(key = lambda x: x[0])

summerCount, winterCount = 0, 0

for i in range(K):
    if distance[i][1]=='summer': summerCount+=1
    else: winterCount+=1

if summerCount>winterCount: print('summer')
else: print('winter')
