import cv2
def take_snapshot():
    vco=cv2.VideoCapture(0)
    results=True
    while(results):
        ret,frame=vco.read()
        cv2.imwrite("image1.jpg",frame)
        results=False
    vco.release()
    cv2.destroyAllWindows()
take_snapshot()        