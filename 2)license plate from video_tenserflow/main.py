import cv2
import pytesseract

# Configure the path to tesseract executable
# For Windows, it might be something like 'C:/Program Files/Tesseract-OCR/tesseract.exe'
pytesseract.pytesseract.tesseract_cmd = "C:/Program Files/Tesseract-OCR/tesseract.exe"

def recognize_license_plate(img):
    # Use Tesseract to do OCR on the captured image
    text = pytesseract.image_to_string(img)
    return text

def main():
    cap = cv2.VideoCapture(0)

    while True:
        # Capture frame-by-frame from webcam
        ret, frame = cap.read()
        if ret:
            # Our operations on the frame come here
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # Display the resulting frame
            cv2.imshow('frame', gray)

            # Call the license plate recognition function
            plate_text = recognize_license_plate(gray)
            if plate_text:
                print("Recognized License Plate:", plate_text)

            # Break the loop
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break

    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
