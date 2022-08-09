from re import I
import cv2
from cv2 import bitwise_and
import numpy as np

#filer out the diffence between the two images
# img1=cv2.imread("img1.png",1)
# img2=cv2.imread("img2.png",1)
# diff=cv2.absdiff(img1,img2)
# cv2.imshow("diff",diff)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

image1=cv2.imread("test.jpg",1)
image2=cv2.imread("test1.jpg",1)
# print(image1.shape)
# print(image2.shape)

image1=cv2.resize(image1,(500,500))
image2=cv2.resize(image2,(500,500))
diff=cv2.absdiff(image1,image2)
#convert the image to gray scale
gray_img=cv2.cvtColor(diff,cv2.COLOR_BGR2GRAY)

#threshold the image
ret,thresh_img=cv2.threshold(gray_img,10,255,cv2.THRESH_BINARY)

#convert thershold image to bgr format
thresh_img=cv2.cvtColor(thresh_img,cv2.COLOR_GRAY2BGR)

#apply using bitwise and operator
bitwise_and_img=bitwise_and(image1,thresh_img)

cv2.imshow("diff",diff)
cv2.waitKey(0)
cv2.destroyAllWindows()

#Q2-----------
#To convert the bluly image to high contrast image
pic1=cv2.imread("test.jpg",1)
pic1=cv2.resize(pic1,(500,500))

#blure the image
blur_img=cv2.GaussianBlur(pic1,(7,7),0) #(image,(kernel_size),0) 
cv2.imshow("blur_img",blur_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#increse the contrast of the image
contrast_img=cv2.addWeighted(pic1,1.5,blur_img,-0.5,0) 
#add addWeighted(image,alpha,beta,gamma,delta)
#alpha is used to increase the contrast 
# beta is used to decrease the contrast 
# gamma is used to add the image  
# delta is used to subtract the image

#here the image is in BGR format
cv2.imshow("contrast_img",contrast_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#increase the contrast of the image using filter2d
pic1=cv2.imread("test.jpg",1)
pic1=cv2.resize(pic1,(500,500))
#filter2d is used to increase the contrast of the image
filter2d=cv2.filter2D(pic1,-1,np.ones((5,5),np.float32)/25) #(image,depth,kernel)
cv2.imshow("filter2d",filter2d)
cv2.waitKey(0)
cv2.destroyAllWindows()

#increase the contrast of the image using convertScaleAbs
pic1=cv2.imread("test.jpg",1)
pic1=cv2.resize(pic1,(500,500))
#convertScaleAbs is used to increase the contrast of the image
alpha = 1 # Contrast control (1.0-3.0)
beta = 0 # Brightness control (0-100)
adjusted = cv2.convertScaleAbs(pic1, alpha=alpha, beta=beta)
cv2.imshow('original', pic1)
cv2.imshow('adjusted', adjusted)
cv2.waitKey()
cv2.destroyAllWindows()

# increase the contrast of the image using histogram equalization
pic1=cv2.imread("test.jpg",0)
pic1=cv2.resize(pic1,(500,500))
#histogram equalization which is used to increase the contrast of the image
histogram=cv2.equalizeHist(pic1) 
res_hist = np.hstack((pic1,histogram)) #stack the images side by side
cv2.imshow("histogram",res_hist)
cv2.waitKey(0)
cv2.destroyAllWindows()
 

# #increase the contrast of the image using clahe
pic1=cv2.imread("test.jpg",0)
pic1=cv2.resize(pic1,(500,500))
clahe=cv2.createCLAHE(clipLimit=2.0,tileGridSize=(8,8)) 
#clipLimit is used to control the contrast of the image
#tileGridSize is used to control the size of the grid
clahe_img=clahe.apply(pic1)
cv2.imwrite("clahe_img.jpg",clahe_img)
#to show image side by side
res_clahe = np.hstack((pic1,clahe_img)) #hstack used to show the images side by side
cv2.imshow("clahe_img",res_clahe)
cv2.waitKey(0)
cv2.destroyAllWindows()