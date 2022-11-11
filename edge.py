import cv2
import matplotlib.pyplot as plt
img=cv2.imread("lion.jpg")
img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#Canny
plt.figure(figsize=(20,20))
c=cv2.Canny(gray_img,threshold1=30,threshold2=100)
plt.subplot(3,3,1)
plt.title("Original image")
plt.imshow(img)
plt.axis("off")
plt.subplot(3,3,2)
plt.title("Gray image")
plt.imshow(gray_img,cmap='gray')
plt.axis("off")
plt.subplot(3,3,3)
plt.title("Canny edge image")
plt.imshow(c,cmap='gray')
plt.axis("off")
#Sobel
img_gaussian=cv2.GaussianBlur(gray_img,(3,3),0)
img_sobelx=cv2.Sobel(img_gaussian,cv2.CV_8U,1,0,ksize=5)
img_sobely=cv2.Sobel(img_gaussian,cv2.CV_8U,0,1,ksize=5)
img_sobel=img_sobelx+img_sobely
plt.subplot(3,3,4)
plt.title("Sobel x image")
plt.imshow(img_sobelx)
plt.axis("off")
plt.subplot(3,3,5)
plt.title("Sobel y image")
plt.imshow(img_sobely,cmap='gray')
plt.axis("off")
plt.subplot(3,3,6)
plt.title("Sobel image")
plt.imshow(img_sobel,cmap='gray')
plt.axis("off")
import numpy as np
kernelx=np.array([[1,1,1],[0,0,0],[-1,-1,-1]])
kernely=np.array([[-1,0,1],[-1,0,1],[-1,0,1]])
prewittx=cv2.filter2D(img_gaussian,-1,kernelx)
prewitty=cv2.filter2D(img_gaussian,-1,kernely)
prewitt=prewittx+prewitty
plt.subplot(3,3,7)
plt.title("Prewitt x image")
plt.imshow(prewittx,cmap='gray')
plt.axis("off")
plt.subplot(3,3,8)
plt.title("Prewitt y image")
plt.imshow(prewitty,cmap='gray')
plt.axis("off")
plt.subplot(3,3,9)
plt.title("Prewitt image")
plt.imshow(prewitt,cmap='gray')
plt.axis("off")
plt.show()
