import cv2
import numpy as np
import os

IMG_W = 224
IMG_H = 224
maskExt = '.jpg'
img_ext = '.jpg'
dim = (IMG_W, IMG_H)


images_dir = 'images'
masks_dir = 'masks'

rotation = [90, 180, 270, 30]

images = os.listdir(images_dir)
masks = os.listdir(masks_dir)

for img_path, mask_path in list(zip(images, masks)):
    print(img_path, mask_path)
    imgOrig = cv2.imread(os.path.join(images_dir, img_path))
    maskOrig =cv2.imread(os.path.join(masks_dir, mask_path))

    imgOrig = cv2.resize(imgOrig, dim)
    maskOrig = cv2.resize(maskOrig, dim)
    for i in range(1,4):
        imgRot = np.rot90(imgOrig, k=i)
        maskRot = np.rot90(maskOrig, k=i)
        cv2.imwrite(os.path.join(images_dir, img_path[:len(img_path)-4] +str(i*90)+ img_ext), imgRot)
        cv2.imwrite(os.path.join(masks_dir, img_path[:len(img_path)-4] +str(i*90)+ maskExt), maskRot)

    imgHf = cv2.flip(imgOrig, 1)
    maskHf = cv2.flip(maskOrig, 1)
    cv2.imwrite(os.path.join(images_dir, img_path[:len(img_path)-4] +'Hf'+ img_ext), imgHf)
    cv2.imwrite(os.path.join(masks_dir, img_path[:len(img_path)-4] + 'Hf'+ maskExt), maskHf)
    








