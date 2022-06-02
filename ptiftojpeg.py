import cv2
import os


path = os.getcwd()  # 获取代码所在目录
tif_list = [x for x in os.listdir(path) if x.endswith(".TIF")]   # 获取目录中所有png格式图像列表
for num,i in enumerate(tif_list):      # 遍历列表
    img = cv2.imread(i,-1)       #  读取列表中的tif图像
    cv2.imwrite(i.split('.')[0]+".jpg",img,[int(cv2.IMWRITE_JPEG_QUALITY),100])    # tif 格式转 jpg 并按原名称命名
    print(tif_list[num])
