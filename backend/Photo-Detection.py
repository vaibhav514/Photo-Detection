import cv2
import os
cascPath = "face.xml"
imagePath = "3.JPG"
size = os.path.getsize(imagePath)
size /= 1024
roundsize = round(size,3)
faceCascade = cv2.CascadeClassifier(cascPath)

image = cv2.imread(imagePath)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

faces = faceCascade.detectMultiScale(
    gray,
    scaleFactor=1.5,
    minNeighbors=4,
    minSize=(4, 4),
)
s = int (format(len(faces)));
if (s > 0 ):
    print("Select Exam type :")
    print("1)ABC")
    print("2)SAF")
    print("3)GATE")
    Exam_type=input()
    if Exam_type=="ABC":
        if 10 < roundsize < 40:
            print("The submitted file is a photograph and valid for ABC exam ")
        else:
            print("File size is to small or to large mantain the size under 40Kb and over 10Kb ")
        print("Uploaded File Size: ", roundsize)
    elif Exam_type=="SAF":
        if 50 < roundsize < 70:
            print("The submitted file is a photograph and valid for SAF exam")
        else:
            print("File size is to small or to large mantain the size under 70Kb and over 50Kb " )
            print("Uploaded File Size: ", roundsize)
    elif Exam_type=="GATE":
         if 45 < roundsize < 65:
            print("The submitted file is a photograph and valid for GATE exam")
         else:
            print("File size is to small or to large mantain the size under 65Kb and over 45Kb ")
            print("Uploaded File Size: ", roundsize)
    else:
        print("Enter Valid Exam name")
else:
    print("No it is not a photograph. Please choose right image.")
