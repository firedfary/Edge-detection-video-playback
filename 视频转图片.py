# 使用这篇代码将视频逐帧分割
import cv2
import os
def save_img():
    video_path = './1' # 保存视频的路径
    video_name = '1.mp4' # 视频的名字
    file_name = video_name.split('.')[0]
    folder_name = video_path + file_name
    os.makedirs(folder_name, exist_ok=True)
    vc = cv2.VideoCapture(video_path+'/'+video_name) # 视频加载
    c=0
    rval=vc.isOpened() #判断是否加载成功，成功则rval为True
    while rval: #当rval为True时
        c = c + 1 #当前在处理第c帧
        rval, frame = vc.read() 
        # 进行单帧读取，rval依然表示加载成功，frame是图片内容
        pic_path = video_path +'/' # 在路径./1的后面加上一个/
        if rval: #如果单帧加载成功
            cv2.imwrite(pic_path + str(c) + '.jpg', frame) #写入图片
            # pic_path就是'./1/'后面再加上当前帧数和'.jpg'构成图片路径
            cv2.waitKey(1)
        else: # 如果单帧加载失败
            break #结束循环
    vc.release()
    print('save_success')
    print(folder_name)

    
save_img()