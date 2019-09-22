import cv2
import numpy as np

src = cv2.imread('object2.jpg')
src= cv2.resize(src,None,fx = 0.8,fy = 0.8,interpolation = cv2.INTER_CUBIC)
gray = cv2.cvtColor(src,cv2.COLOR_RGB2GRAY)
gray=cv2.medianBlur(gray,5)
edges = cv2.Canny(gray,10,160)
cv2.imwrite("detect3.jpg",edges)


lines = cv2.HoughLinesP(edges,1,np.pi/180,80,minLineLength =200,maxLineGap =8)



N = lines.shape[0]
for n in range(N):
    x1 = lines[n,:,0]
    y1 = lines[n,:,1]
    x2 = lines[n,:,2]
    y2 = lines[n,:,3]
    cv2.line(src,(x1,y1),(x2,y2),(0,0,255),5)



circles = cv2.HoughCircles(edges,cv2.HOUGH_GRADIENT,1,200,param1 = 250,param2 =60,minRadius =100,maxRadius =200)


circles = np.int16(np.around(circles))
for i in circles[0,:]:
    cv2.circle(src,(i[0],i[1]),i[2],(0,0,255),8)#draw a circle
    cv2.circle(src,(i[0],i[1]),1,(0,255,0),6)
    cv2.imshow('d',src)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
cv2.imwrite("detect2.jpg",src)