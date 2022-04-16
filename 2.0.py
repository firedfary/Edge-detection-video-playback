import time
from winsound import PlaySound
import winsound
import cv2
import os
# fn="1/1.wav"
# oau=AudioFileClip(fn)
# nau=oau.fl_time(lambda t:0.58*t,apply_to=["mask","audio"])
# nau=nau.set_duration(oau.duration/0.58)
cap=cv2.VideoCapture("1/1.mp4")
print(cap.get(cv2.CAP_PROP_FPS))

cv2.namedWindow('image',0)
cv2.resizeWindow('image',1280,720)   #这两行用来创建大小可调的窗口，1280和720就是大小
au = r"./1/1.wav"
i = 0
PlaySound(au,winsound.SND_ASYNC)  # 这3行用来播放声音。
a=time.time()
while True:
    try:
        flag,img=cap.read()
        blur = cv2.GaussianBlur(img, (3, 3), 0)
        canny = cv2.Canny(blur, 50, 150)
        cv2.imshow('image',canny)
        cv2.waitKey(14)  
        i += 1
        print(i) # 显示当前播放到第几帧
    except Exception:
        break
cv2.destroyAllWindows()
b=time.time()
print((b-a)*1000,"ms")