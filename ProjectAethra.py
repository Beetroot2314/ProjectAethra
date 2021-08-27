import cv2
import pytesseract
import pyttsx3

tts =pyttsx3.init()
tts.say("Starting code")
tts.runAndWait()
print("started")

pytesseract.pytesseract.tesseract_cmd = 'F:\\Program Files\\Tesseract-OCR\\tesseract.exe'


cap = cv2.VideoCapture(0)
while True:
    ret,frame =cap.read()
    reader = pytesseract.image_to_string(frame)

    cv2.imshow('Text',frame)
    print(reader)
    tts.setProperty('rate', 130)
    if cv2.waitKey(2) & 0xFF ==ord('q'):
        break
    tts.say(reader)
    tts.runAndWait()





cap.release()






