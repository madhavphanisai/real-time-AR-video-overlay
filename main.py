import cv2
import numpy as np

cap = cv2.VideoCapture(0)
imgTarget = cv2.imread('targetIMG.jpg')
myVid = cv2.VideoCapture('targetVid.mp4')

detected = False

success , imgVid = myVid.read()
hT, wT, cT = imgTarget.shape
imgVid = cv2.resize(imgVid, (wT, hT))

# to detect key points in the target image
orb = cv2.ORB_create(nfeatures=1000)
kp1,des1 = orb.detectAndCompute(imgTarget,None)
imgTarget = cv2.drawKeypoints(imgTarget,kp1,None)
while True:
    success, imgWebCam = cap.read()
    imgAug = imgWebCam.copy()
    kp2,des2 = orb.detectAndCompute(imgWebCam,None)
    # imgWebCam = cv2.drawKeypoints(imgWebCam,kp2,None)

    if detected:
        success, imgVid = myVid.read()

        if not success:  # End of video
            myVid.set(cv2.CAP_PROP_POS_FRAMES, 0)  
            success, imgVid = myVid.read()

        imgVid = cv2.resize(imgVid, (wT, hT))

    bf = cv2.BFMatcher()
    matches = bf.knnMatch(des1,des2,k=2)
    good = []
    for m,n in matches:
        if m.distance < 0.75*n.distance:
            good.append(m)
    # print(len(good))
    imgFeatues = cv2.drawMatches(imgTarget,kp1,imgWebCam,kp2,good,None,flags=2)
    if len(good)>25:
        detected = True 
        srcPts = np.float32([kp1[m.queryIdx].pt for m in good]).reshape(-1,1,2)
        dstPts = np.float32([kp2[m.trainIdx].pt for m in good]).reshape(-1,1,2)
        matrix , mask = cv2.findHomography(srcPts,dstPts,cv2.RANSAC,5)

        pts = np.float32([[0,0],[0,hT],[wT,hT],[wT,0]]).reshape(-1,1,2)
        dst = cv2.perspectiveTransform(pts,matrix)
        img2 = cv2.polylines(imgWebCam,[np.int32(dst)],True,(255,0,255),5)
        
        imgWarp = cv2.warpPerspective(imgVid,matrix,(imgWebCam.shape[1],imgWebCam.shape[0]))
        maskNew = np.zeros((imgWebCam.shape[0],imgWebCam.shape[1],3),np.uint8)
        cv2.fillPoly(maskNew,[np.int32(dst)],(255,255,255))
        maskInv = cv2.bitwise_not(maskNew)
        imgAug = cv2.bitwise_and(imgAug,maskInv)
        imgAug = cv2.bitwise_or(imgWarp,imgAug)

    cv2.imshow("OUTPUT",imgAug)
    # cv2.imshow(" IMG Capture", imgWebCam) 
    # img1_resized = cv2.resize(imgWebCam, (640, 480))
    # img2_resized = cv2.resize(imgAug, (640, 480))

    # side_by_side = np.hstack((img1_resized, img2_resized))

    # Show in one window
    # cv2.imshow("OUTPUT", side_by_side)
    # cv2.waitKey(1)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break 