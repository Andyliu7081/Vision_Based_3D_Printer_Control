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
        cap = cv2.VideoCapture(0)
        num = 1
        while(cap.isOpened()): # check camera status
            ret_flag,Vshow = cap.read() # get img
            cv2.imshow("Capture_Test",Vshow) # display img
            k = cv2.waitKey(1) & 0xFF
            if k == ord('s'): # press S to save
                cv2.imwrite('saved image'+str(num)+".jpg",Vshow) #route
                print("success to save "+str(num)+".jpg")
                print("-------------------------")
                num += 1
            elif k == ord(' '): #press ' ' to exit
                break

        cap.release() # release storage
        cv2.destroyAllWindows() # exit and close all window

        # Transition to next state
        self.current_state = 'Transform'

    def transform_image(self):
        print("Transforming image")
        if self.image is not None:
            self.image = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
            self.image = cv2.calcHist([self.image], [0], None, [256], [0, 256])

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
sm.execute()  # Transform
sm.execute()  # Determine Exposure
