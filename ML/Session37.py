#reading image using opencv

import cv2
from cv2 import IMREAD_REDUCED_COLOR_4
import numpy as np

img=cv2.imread("Screenshot_3.png",cv2.IMREAD_ANYCOLOR)
print("COLOR",img) #3d array
print("ColorShape",img.shape) #(height,width,channels)

img=cv2.imread("Screenshot_3.png",cv2.IMREAD_GRAYSCALE)
print("Gray",img) #2d array
print("GrayShape",img.shape) #(height,width,channels)

image=cv2.imread("Screenshot_3.png",0) #1 is for color image it is 0 for grayscale image
#read the image as numpy array
print(image)

#imread.reduce_color() #reduce the color of the image size

#_______________________________________________________________
#show the image

img=cv2.imread("Screenshot_3.png",0)
cv2.imshow("First Image",img) #to show the image in the window
cv2.waitKey(0) #wait for 0 millisecond
cv2.destroyAllWindows() #destroy the window

#to specify key to close the window
img=cv2.imread("Screenshot_3.png",1)
cv2.imshow("First Image",img)
if cv2.waitKey(0)==ord('q'):
    cv2.destroyAllWindows()
cv2.destroyAllWindows()

#_______________________________________________________________
#to save the image
img=cv2.imread("Screenshot_3.png",IMREAD_REDUCED_COLOR_4)
cv2.imwrite("Screenshot_3_reduced.png",img)

#_______________________________________________________________
#to convert the image to gray scale
img=cv2.imread("Screenshot_3.png",1)
gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #your image must be in BGR format
hsv_img=cv2.cvtColor(img,cv2.COLOR_BGR2HSV) #convert to hsv hue saturation value
cv2.imshow("original",img)
cv2.imshow("Gray Image",gray_img)
cv2.imshow("HSV Image",hsv_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#_______________________________________________________________

img=cv2.imread("Screenshot_3.png",0)
color_img=cv2.cvtColor(img,cv2.COLOR_GRAY2BGR) 
cv2.imshow("GRAY2BGR",color_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
#here the image is on gray scale and we can't convert it to BGR because it is not in BGR format
#the source image must be in BGR format

#_______________________________________________________________
#resize the image
img=cv2.imread("Screenshot_3.png",1)
img=cv2.resize(img,(500,500))
cv2.imshow("Resize",img) 
cv2.waitKey(0)
cv2.destroyAllWindows()

#_______________________________________________________________
#create a black or white image 
white_img=np.ones((500,500,3))*255 #create a white image with all pixels as 255 (white)
black_img=np.zeros((500,500,3)) #create a black image with all pixels as 0 (black)
cv2.imshow("White",white_img)
cv2.imshow("Black",black_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#_______________________________________________________________
#add two images together
