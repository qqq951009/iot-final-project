import cv2

class VideoCamera(object):
    def __init__(self):
        self.faceCascade = cv2.CascadeClassifier('/home/pi/webstream/haarcascade_frontalface_default.xml')
        self.cap = cv2.VideoCapture(0)

    def __del__(self):
        self.cap.release()

    def get_frame(self):
        ret, img = self.cap.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = self.faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.2,
            minNeighbors=5,
            minSize=(20, 20)
        )
        for (x,y,w,h) in faces:
            cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = img[y:y+h, x:x+w]
            cv2.imwrite('/home/pi/webstream/1.jpg',img)
        ret, jpeg = cv2.imencode('.jpg',img)

        return jpeg.tostring()
