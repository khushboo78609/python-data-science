import cv2, os
import mediapipe as mp 

file = 'Computer version/sample_vid2.mp4'

if not os.path.exists(file):
    print('video file not found')
camera = cv2.VideoCapture(file)

with mp.solutions.pose.Pose(
    min_detection_confidence=.5,
    min_tracking_confidence = .5) as pd:
    while True:
        state,frame = camera.read() # frame -> image captured, state -> boolean
        if not state:
            print("Could not access camera")
            break
        frame.flags.writeable = False
        frame = cv2.cvtcolor(frame, cv2.COLOR_BGR2RGB)
        results = pd.process(frame)
        frame.flags.writeable = True
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
        if results.detections:
            cv2.putText(frame,f'{len(results.detections)}faces',
                        (10,30), cv2.FONT_HERSHEY_COMPLEX,
                        1,(0,255,0),2)
            mp.solutions.drawing_utils.draw_landmarks(
                frame, results.pose_landmarks,mp.solutions.pose.POSE_CONNECTIONS,
                
                
            )
        cv2.imshow('camera window',frame)
        if cv2.waitKey(20) == ord('q'): # if q is pressed stop the loop
            break
    camera.release()
    cv2.destroyAllWindows()
