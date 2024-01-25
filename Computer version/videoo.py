import cv2, os
file = 'Computer version\sample_vid2.mp4'
if not os.path.exists(file):
    print('video file not found')
camera = cv2.VideoCapture(file)
while True:
    state,frame = camera.read() # frame -> image captured, state -> boolean
    if not state:
        print("Could not access camera")
        break
    cv2.imshow('camera window',frame)
    if cv2.waitKey(20) == ord('q'): # if q is pressed stop the loop
        break
camera.release()
cv2.destroyAllWindows()
