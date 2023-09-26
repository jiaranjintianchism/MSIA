# -*-coding:utf-8-*-
# -*-coding:utf-8-*-
import os

from mmdet.apis import init_detector, inference_detector

import matplotlib.image as re
import cv2
import pandas as pd
def np_list_int(tb):
	tb_2 = tb.tolist()  # 将np转换为列表
	return tb_2


def shot(img, dt_boxes, name):  # 应用于predict_det.py中,通过dt_boxes中获得的四个坐标点,裁剪出图像
	os.makedirs('/home/chenlei/video/frozen-in-time-main/frozen-in-time-main/data/msvd_object/' + name)
	dt_boxes = np_list_int(dt_boxes)
	boxes_len = len(dt_boxes)
	num = 0
	path = '/home/chenlei/video/frozen-in-time-main/frozen-in-time-main/data/msvd_object/' + name
	while 1:
		if (num < boxes_len):
			box = dt_boxes[num]
			tl = box[0]
			tr = box[1]
			br = box[2]
			bl = box[3]
			print("打印转换成功数据num =" + str(num))
			print("tl:" + str(tl), "tr:" + str(tr), "br:" + str(br), "bl:" + str(bl))
			print(tr, bl, tl, br)

			crop = img[int(tr):int(bl), int(tl):int(br)]

			# crop = img[27:45, 67:119] #测试
			# crop = img[380:395, 368:119]
			file = path + name + '_' + str(num) + '.jpg'
			cv2.imwrite(file, crop)

			num = num + 1
		else:
			break

config_file = '/frozen-in-time-main/mmdetection-master/configs/yolox/yolox_x_8x8_300e_coco.py'
# 从 model zoo 下载 checkpoint 并放在 `checkpoints/` 文件下
# 网址为: http://download.openmmlab.com/mmdetection/v2.0/faster_rcnn/faster_rcnn_r50_fpn_1x_coco/faster_rcnn_r50_fpn_1x_coco_20200130-047c8118.pth
checkpoint_file = '/frozen-in-time-main/mmdetection-master/checkpoints/yolox_x_8x8_300e_coco_20211126_140254-1ef88d67.pth'
# device = 'cuda:0'
# 初始化检测器
model = init_detector(config_file, checkpoint_file)
images = pd.read_csv('/data/msvd_/all.txt', sep='\t')
images = images.values
for i in range(len(images)):
	img = images[i].__array__()[0]
	name = img[:-4]
	img = '/home/chenlei/video/frozen-in-time-main/frozen-in-time-main/data/msvd_images/' + img
	img = cv2.imread(img)
	result = inference_detector(model, img)
	img1, bbox = model.show_result(img, result)
	shot(img, bbox[:, 0:4], name)
	model.show_result('/home/chenlei/video/frozen-in-time-main/frozen-in-time-main/data/image', result, out_file= name + 'result.jpg')

