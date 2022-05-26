import os
import scipy.io
import commands
import shutil
from PIL import Image
import numpy as np

srcDir = './rescaleBoss/'
tempDir = './singleBoss20/'

fileList = os.listdir(srcDir)
fileList.sort()
x=1

for fname in fileList:
    filePath = os.path.join(srcDir, fname)
    if os.path.isdir(filePath):
        continue

    print (fname)
    arr = fname.split('.')
    #hevcPath = os.path.join(hevcDir, arr[0])
    outPath = os.path.join(tempDir, 'single.%s.jpeg' % arr[0])
    os.system('cjpeg -quality 20 -dct float  %s>%s'%(filePath,outPath))#cjpeg -quality 90 -dct float  1.pgm>1.jpg   cjpeg -quality 60 1.pgm > foo.jpg
