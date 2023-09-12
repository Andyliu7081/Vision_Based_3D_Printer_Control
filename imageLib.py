import numpy as np
import cv2

def capture_image(self):
        print("Capturing image")
        cap = cv2.VideoCapture(0)
        num = 1
        if not cap.isOpened():
            print("Cannot open camera")
            return
        
        # ret, frame = cap.read()
        # if not ret:
        #     print("Can't receive frame. Exiting ...")
        #     return
        
        while(cap.isOpened()):
            ret, frame = cap.read()
            cv2.imshow("Cap", frame)
            k = cv2.waitKey(1) & 0xFF
            if k == ord('s'):
                img = cv2.imwrite('saved image'+str(num)+".jpg",frame) #routeimg
                num += 1
            elif k == ord(' '):
                break

        self.image = frame
        cap.release()
        cv2.destroyAllWindows()

        # Transition to next state
        self.current_state = 'Transform'