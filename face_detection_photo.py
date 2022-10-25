import cv2 

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt2.xml')
image = cv2.imread('face.png')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
face = face_cascade.detectMultiScale(gray, 1.5, 5)

for (x,y,w,h) in face:
    cv2.rectangle(image, (x,y), (x+w,y+h), (255,255,255), 3)
cv2.imshow("image", image)
cv2.waitKey(0)  
cv2.destroyAllWindows()
