import cv2
import matplotlib.pyplot as plt

data1=cv2.imread('Phase.png',0)
blur=cv2.bilateralFilter(data1,15,15,15)
can=cv2.Canny(blur,60,255)
cv2
ret,thresh = cv2.threshold(blur,120,200,cv2.THRESH_BINARY)
contours, image = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
for i in range(len(contours)):
    cnt = contours[i]
    hull = cv2.convexHull(cnt)
    img2 = cv2.drawContours(blur, [cnt], -1, (255,255,255), 5)

import random 
centers=[]
areas=[]
for j in contours:
    x=[]
    y=[]
    if len(j)>25:
        for i in j:
            x.append(i[0][0])
            y.append(i[0][1])
        xmin=min(x)
        xli=x.index(xmin)
        yxmin=y[xli]
        xmax=max(x)
        xla=x.index(xmax)
        yxmax=y[xla]
        ymin=min(y)
        yli=y.index(ymin)
        xymin=x[yli]
        ymax=max(y)
        yla=y.index(ymax)
        xymax=x[yla]
        center=((xmin+xmax)/2,(ymin+ymax)/2)
        square=abs((ymax-ymin)*(xmax-xmin))
        tri1=(abs(xymin-ymax)*abs(xmin-xymax))/2
        tri2=(abs(xmax-xymax)*abs(xmax-xymax))/2
        tri3=(abs(xmax-xymin)*abs(yxmax-ymin))/2
        tri4=(abs(xmin-xymin)*abs(yxmin-ymin))/2
        area=square-tri1-tri2-tri3-tri4
        #display(tri1,tri2,tri3)
        areas.append(abs(area))
        centers.append(center)
random.shuffle(centers)

totald=[]
for j in range(1,13):
    random.shuffle(centers)
    distance=[]
    data1=cv2.imread('Phase.png')
    import math 
    for i in range (1,len(centers)):
        cv2.line(data1,(int(centers[i][0]),int(centers[i][1])),(int(centers[i-1][0]),int(centers[i-1][1])),(255,255,255))
        aa=centers[i][0]-centers[i-1][0]
        bb=centers[i][1]-centers[i-1][1]
        cc=math.sqrt(aa**2+bb**2)
        distance.append(cc)
        xx=(sum(distance)/len(distance))
        totald.append(xx)
    plt.subplot(3,4,j),plt.imshow(data1)
print('The average grainsize is:'+str(sum(totald)/len(totald)))
plt.savefig('graindistance.png',dpi=3000)

data1=cv2.imread('Phase.png')
color=[]
R=[]
G=[]
B=[]
r=[]
font = cv2.FONT_HERSHEY_SIMPLEX 
thickness = 1
fontScale = 0.38
g=[]
b=[]
r=0
g=0
b=0
n=1
for i in centers:
    x=int(i[0])
    y=int(i[1])
    z=data1[x-n:x+n,y-n:y+n]
    for j in z:
        for k in j:
            r+=k[0]
            r/=len(j)
            R.append(int(r))
            g+=k[1]
            g/=len(j)
            G.append(int(g))
            b+=k[2]
            b/=len(j)
            B.append(int(b))
for ii in range (len(centers)):
    color=(R[ii],G[ii],B[ii])
    org=int(centers[ii][0]),int(centers[ii][1])
    if R[ii]<100:
        img=cv2.putText(data1,'Fe3C',org,font, fontScale,color,1,cv2.LINE_AA)
    elif R[ii]>100 and R[ii]<200:
        img=cv2.putText(data1,'Alpha',org,font, fontScale,color,1,cv2.LINE_AA)
    else:
        img=cv2.putText(data1,'Beta',org,font, fontScale,color,1,cv2.LINE_AA)
plt.imshow(img)
plt.savefig('hh.png',dpi=3800)