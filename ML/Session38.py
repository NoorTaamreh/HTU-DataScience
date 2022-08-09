# import cv2 as cv
# import numpy as np
# img=cv.imread('morph.png',0)
# kernel=np.ones((5,5),np.uint8)
# erosion=cv.erode(img,kernel,iterations=1)
# dilation = cv.dilate(img,kernel,iterations=2)

# cv.imshow('og',img)
# cv.imshow('new',erosion)
# cv.imshow('new2',dilation)
# cv.waitKey()
# cv.destroyAllWindows()



# import cv2 as cv
# import numpy as np
# img=cv.imread('C:\\Users\\USER\\Pictures\\265.png',0)
# kernel=np.ones((5,5),np.uint8)
# erosion=cv.erode(img,kernel,iterations=1)
# dilation = cv.dilate(img,kernel,iterations=2)

# cv.imshow('og',img)
# cv.imshow('new',erosion)
# cv.imshow('new2',dilation)
# cv.waitKey()
# cv.destroyAllWindows()


# import cv2 as cv
# import numpy as np
# img=cv.imread('C:\\Users\\USER\\Pictures\\Screenshot_2.png',0)
# kernel=np.ones((5,5),np.uint8)
# erosion=cv.erode(img,kernel,iterations=1)
# dilation = cv.dilate(img,kernel,iterations=2)

# cv.imshow('og',img)
# cv.imshow('new',erosion)
# cv.imshow('new2',dilation)
# cv.waitKey()
# cv.destroyAllWindows()

#edge detection
# import cv2
# import numpy as np

# img=cv2.imread('C:\\Users\\USER\\Pictures\\Screenshot_2.png',0)
# #we need to convert the image to grayscale
# gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# laplace=cv2.Laplacian(gray_image,cv2.CV_64F)
# laplace=np.uint8(np.absolute(laplace))
# cv2.imshow('laplace',laplace)
# cv2.waitKey()

#sobel operator
# import cv2
# image=cv2.imread('C:\\Users\\USER\\Pictures\\265.png')

# gray_image=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
#Sobel_x=cv2.Sobel(gray_image,cv2.CV_64F,1,0) #cv2.CV_64F is the type of the output image
# Sobel_y=cv2.Sobel(gray_image,cv2.CV_64F,0,1) #cv2.cv_64F converts the output image to float64
# cv2.imshow('Gradient_x',Sobel_x) #x is horizontal
# cv2.imshow('Gradient_y',Sobel_y)  #we can see that the gradient is not uniform
# Sobel=cv2.bitwise_or(Sobel_x,Sobel_y)
# cv2.imshow('Actual image',image)
# cv2.imshow("gradient",Sobel)
# cv2.waitKey()
# cv2.destroyAllWindows()

#canny edge detection
import cv2
img=cv2.imread('C:\\Users\\USER\\Pictures\\265.png',0)
final=cv2.Canny(img,100,300)
cv2.imshow('og',img)
cv2.imshow("result",final)
cv2.waitKey()
cv2.destroyAllWindows()
