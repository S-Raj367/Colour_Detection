import cv2   #FOR VIDEO/IMG PROCESSING
from PIL import Image #FOR MASKING(isolating ceratin part of img based on some condn)
from utils import get_limits #fn from another file

red=[0,0,255] #IN BGR FORMAT

webcam=cv2.VideoCapture(0);#starting webcam

while True:
    ret, frame=webcam.read() #read webcam frame to frame
   
    #convertBGR toHSV(makes easier to detect colour)
    hsvImg=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    lowerlimit ,upperlimit=get_limits(color=red)#get range for detecting the clour
    
    #lets mask(isolate) the req region
    mask=cv2.inRange(hsvImg,lowerlimit,upperlimit)
 
    #Convert OpenCV mask to a Pillow image-->it gives a easy way to make boundarys box:getbbox() → (x1, y1, x2, y2)
    mask_ = Image.fromarray(mask)

    bbox = mask_.getbbox()

    if bbox is not None:   #if mask detected then make box
        x1, y1, x2, y2 = bbox
        #make box
        frame = cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 5) #coor,colur of line,width

    #everything is done so show modified frame
    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
     break

#release used memory
cap.release()

cv2.destroyAllWindows()

