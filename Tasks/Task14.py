import cv2
import face_recognition
from IPython.display import display, clear_output

def capture_and_display():
    # Initialize the webcam
    cap = cv2.VideoCapture(0)
    
    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()
        
        if not ret:
            break
        
        # Find faces in the frame
        face_locations = face_recognition.face_locations(frame)
        
        # Display face(s) in the top corner of the frame
        for top, right, bottom, left in face_locations:
            face = frame[top:bottom, left:right]
            # Resize face to a fixed size for display
            face = cv2.resize(face, (100, 100))
            frame[0:100, 0:100] = face
            
        # Display the frame in the notebook
        clear_output(wait=True)
        display(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
        
        # Break the loop on 'q' key press
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    # Release the webcam and close the OpenCV windows
    cap.release()
    cv2.destroyAllWindows()

# Call the function to start capturing and displaying
capture_and_display()
