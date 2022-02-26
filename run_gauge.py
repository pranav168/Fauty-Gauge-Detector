import cv2
from cv2 import waitKey
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def pixel_count(Video_name, cropX1, cropY1, cropX2, cropY2):
    # Establish capture
    cap = cv2.VideoCapture(Video_name)
    # Loop through each frame
    white_pixel_count=[]
    for frame_idx in range(int(cap.get(cv2.CAP_PROP_FRAME_COUNT))):
        # Read frame 
        try:
            ret, frame = cap.read()
            frame = frame[cropX1:cropY1, cropX2:cropY2]
            
            # Gray transform
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            # blurred = cv2.GaussianBlur(frame, (3,3),3,0)
            canny = cv2.Canny(gray, threshold1=100, threshold2=40)
            white_pixel_count.append(np.sum(canny == 255))
            cv2.imshow('Video Player', canny)
            
            # Breaking out of the loop
            if cv2.waitKey(20) & 0xFF == ord('q'):
                break
        except:
            break
        # Close down everything
    cap.release()
    cv2.destroyAllWindows()
    return  white_pixel_count


# white_pixel_count_needle_1 = pixel_count('needle2.mp4', cropX1=1, cropY1=100, cropX2=900, cropY2=1000)
# white_pixel_count_needle_2 = pixel_count('needle2.mp4', cropX1=1, cropY1=42, cropX2=1180, cropY2=1290)
white_pixel_count_stable_needle = pixel_count('stable-needle2.mp4', cropX1=340, cropY1=380, cropX2=530, cropY2=560)

# plt.plot(white_pixel_count_needle_1)
# plt.show()
# white_pixel_count_needle_2=[1/i for i in white_pixel_count_needle_2  ]

# plt.plot(white_pixel_count_needle_2)
# plt.show()


# plt.plot(white_pixel_count_stable_needle)
# plt.show()



# # Establish capture
# cap = cv2.VideoCapture('needle2.mp4')
# # Loop through each frame
# white_pixel_count=[]
# for frame_idx in range(int(cap.get(cv2.CAP_PROP_FRAME_COUNT))):
    
#     # Read frame 
#     try:
#         ret, frame = cap.read()

#         frame = frame[1:42, 1180:1290]
        
#         # Gray transform
#         gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#         # blurred = cv2.GaussianBlur(frame, (3,3),3,0)
#         canny = cv2.Canny(gray, threshold1=60, threshold2=200)
#         white_pixel_count.append(np.sum(canny == 255))
#         cv2.imshow('Video Player', canny)
        
#         # Breaking out of the loop
#         if cv2.waitKey(20) & 0xFF == ord('q'):
#             break
#     except:
#         white_pixel_count
#         break
#     # Close down everything
# cap.release()
# cv2.destroyAllWindows()

# # Establish capture
# cap = cv2.VideoCapture('needle.mp4')
# # Loop through each frame
# for frame_idx in range(int(cap.get(cv2.CAP_PROP_FRAME_COUNT))):
    
#     # Read frame 
#     ret, frame = cap.read()

#     frame = frame[1:100, 900:1000]

    
#     # Gray transform
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#     # blurred = cv2.GaussianBlur(frame, (3,3),0)
#     canny = cv2.Canny(gray, threshold1=50, threshold2=200)
#     # Show image
#     cv2.imshow('Video Player', canny)
    
#     # Breaking out of the loop
#     if cv2.waitKey(100) & 0xFF == ord('q'):
#         break

# # Close down everything
# cap.release()
# cv2.destroyAllWindows()

# cap = cv2.VideoCapture('stable-needle.mp4')
# # Loop through each frame
# for frame_idx in range(int(cap.get(cv2.CAP_PROP_FRAME_COUNT))):
    
#     # Read frame 
#     ret, frame = cap.read()

#     frame = frame[100:500, 300:1000]

    
#     # Gray transform
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#     # blurred = cv2.GaussianBlur(frame, (3,3),0)
#     canny = cv2.Canny(gray, threshold1=50, threshold2=200)
#     # Show image
#     cv2.imshow('Video Player', canny)
    
#     # Breaking out of the loop
#     if cv2.waitKey(100) & 0xFF == ord('q'):
#         break

# # Close down everything
# cap.release()
# cv2.destroyAllWindows()

# cap = cv2.VideoCapture('needle.mp4')
# # Loop through each frame
# for frame_idx in range(int(cap.get(cv2.CAP_PROP_FRAME_COUNT))):
    
#     # Read frame 
#     ret, frame = cap.read()

#     frame = frame[1:100, 900:1000]

    
#     # Gray transform
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#     # blurred = cv2.GaussianBlur(frame, (3,3),0)
#     canny = cv2.Canny(gray, threshold1=50, threshold2=200)
#     # Show image
#     cv2.imshow('Video Player', canny)
    
#     # Breaking out of the loop
#     if cv2.waitKey(100) & 0xFF == ord('q'):
#         break

# # Close down everything
# cap.release()
# cv2.destroyAllWindows()