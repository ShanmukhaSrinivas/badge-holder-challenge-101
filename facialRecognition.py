import cv2
cas = cv2.CascadeClassifier("D:\\opencv\\data\\haarcascades\\haarcascade_frontalface_alt.xml")
#print(img.shape)
img = cv2.imread("D:\\New folder\\Hospital_Management\\photos\\Dr-Gowri-Dermatologist-in-hyderabad.jpg",1)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = cas.detectMultiScale(gray,scaleFactor=1.05,minNeighbors=5)
print(type(faces))
print(faces)
for x,y,w,h in faces:
    img = cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 3)
cv2.imshow("Gray", img)
cv2.waitKey(20000)
cv2.destroyAllWindows()


