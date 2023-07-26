import cv2
import numpy as np

class StateMachine:
    def __init__(self):
        self.states = {
            'Capture': self.capture_image,
            'Transform': self.transform_image,
            'DetermineExposure': self.determine_exposure,
        }
        self.current_state = 'Capture'
        self.image = None

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

    def transform_image(self):
        print("Transforming image")
        if self.image is not None:
            self.image = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
            self.image = cv2.calcHist([self.image], [0], None, [256], [0, 256])

            cv2.imshow("show transform", self.image)
            # Transition to next state
            self.current_state = 'DetermineExposure'
        else:
            print("No image to transform")

    def determine_exposure(self):
        print("Determining exposure")
        if self.image is not None:
            mean_value = np.mean(self.image)
            if mean_value > 200: # arbitrary threshold
                print("Image is overexposed")
            elif mean_value < 50: # arbitrary threshold
                print("Image is underexposed")
            else:
                print("Image exposure is fine")

            # Transition back to Capture state for next cycle
            self.current_state = 'Capture'
        else:
            print("No image to determine exposure")

    def execute(self):
        self.states[self.current_state]()

# Test the state machine
sm = StateMachine()
sm.execute()  # Capture
sm.execute()
sm.execute()

