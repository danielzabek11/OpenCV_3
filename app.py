import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while True:
    #Capture video frame by frame
    ret, frame = cap.read()
    width = int(cap.get(3)) #width needs to be int instead of float for slice later
    height = int(cap.get(4)) #height

    image = np.zeros(frame.shape, np.uint8)
    smaller_frame = cv2.resize(frame, (0,0), fx=0.5, fy=0.5)

    image[:height//2, :width//2] = cv2.rotate(smaller_frame, cv2.ROTATE_180) #top left
    image[height//2:, :width//2] = smaller_frame #bottom left
    image[:height//2, width//2:] = smaller_frame #top right
    image[height//2:, width//2:] = cv2.rotate(smaller_frame, cv2.ROTATE_180) #bottom right

    #Display each frame
    cv2.imshow('frame', image)

    
    if cv2.waitKey(1) == ord('q'):
        break

# After the loop release the cap object (relase our webcam so it can be used by other programs)
cap.release()
# Destroy all the windows
cv2.destroyAllWindows()