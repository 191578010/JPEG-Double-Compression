import os
import scipy.io
import commands
import shutil
from PIL import Image
import numpy as np

CMD_ENCODE='cjpeg -quality 90 -dct float %s>%s'
CMD_FIRST_DECODE='djpeg -pnm -dct float -outfile temp.pgm %s'
CMD_REMOVE='rm %s'

img_path="./singleBoss90"

for img_file in os.listdir(img_path):
    if os.path.isfile(os.path.join(img_path,img_file)):
       if img_file.find('.jpeg')>=0:
          os.system(CMD_FIRST_DECODE %os.path.join(img_path,img_file))
          output_file='./doubleBoss90/double.%s.jpeg'%(img_file[7:img_file.find('.jpeg')])
          os.system(CMD_ENCODE %('temp.pgm',output_file))
          os.system(CMD_REMOVE %('temp.pgm'))
    
   
