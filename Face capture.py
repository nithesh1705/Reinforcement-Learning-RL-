import cv2

import os

def takepic(name):

    dir = 'C:/Users/nithe/Documents/UiPath/RL/Current customer'
    for f in os.listdir(dir):
        os.remove(os.path.join(dir, f))
    
    cam_port = 0
    cam = cv2.VideoCapture(cam_port)

    result, image = cam.read()

    if result:

        cv2.imshow("Photo", image)
        img_name = "C:/Users/nithe/Documents/UiPath/RL/Customer Image/"+str(name)+".png"
        cv2.imwrite(img_name, image)
        img_currentstorage = "C:/Users/nithe/Documents/UiPath/RL/Current customer/"+str(name)+".png"
        cv2.imwrite(img_currentstorage, image)
        cv2.destroyAllWindows()

    else:
    	print("No image detected. Please! try again")
