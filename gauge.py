import cv2
from cv2 import waitKey
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

class tester():
    def __init__(self):
        pass
    def pixel_count(self,Video_name, cropX1, cropY1, cropX2, cropY2, blurred=False):
        # Establish capture
        cap = cv2.VideoCapture(Video_name)
        # Loop through each frame
        white_pixel_count=[]
        for frame_idx in range(int(cap.get(cv2.CAP_PROP_FRAME_COUNT))):
            try:
                ret, frame = cap.read()
                frame = frame[cropX1:cropY1, cropX2:cropY2]
                
                # Gray transform
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                if blurred:
                    gray = cv2.GaussianBlur(frame, (3,3),3,0)
                canny = cv2.Canny(gray, threshold1=60, threshold2=90)
                white_pixel_count.append(np.sum(canny == 255))
            except:
                break
        return  white_pixel_count
