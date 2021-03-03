import cv2

class FrontOrganDetect():
    
    # Loading classifiers
    faceCascade = cv2.CascadeClassifier('xml/haarcascade_frontalface_default.xml')
    eyesCascade = cv2.CascadeClassifier('xml/haarcascade_eye.xml')
    noseCascade = cv2.CascadeClassifier('xml/haarcascade_mcs_nose.xml')
    mouthCascade = cv2.CascadeClassifier('xml/haarcascade_mcs_mouth.xml')

    def __init__(self):
        pass
    
    def draw_boundary(self, img, classifier, scaleFactor, minNeighbors, color, text,frontOrganCheck):
        # Converting image to gray-scale
        ds_factor = 0.5
        # img = cv2.resize(img, None, fx=ds_factor, fy=ds_factor, interpolation=cv2.INTER_AREA)
        gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        gray_img = cv2.bilateralFilter(gray_img,5,1,1) 
        # detecting features in gray-scale image, returns coordinates, width and height of features
        if text == 'Eyes':
            features = classifier.detectMultiScale(gray_img, scaleFactor, minNeighbors,minSize=(50,50))
        else:
            features = classifier.detectMultiScale(gray_img, scaleFactor, minNeighbors)
        # coords = []
        # drawing rectangle around the feature and labeling it
        #for (x, y, w, h) in features:
            # cv2.rectangle(img, (x,y), (x+w, y+h), color, 2)
            # cv2.putText(img, text, (x, y-4), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 1, cv2.LINE_AA)
            #coords = [x, y, w, h]
        # print(f'+++{text}==>{coords}')
        if len(features) <= 0 :
            features = None
            
        frontOrganCheck[text] = features
        return frontOrganCheck

    # Method to detect the features
    def detect(self, img, option = 'all'):
        color = {"blue":(255,0,0), "red":(0,0,255), "green":(0,255,0), "white":(255,255,255)}
        frontOrganCheck = {'Eyes': None, 'Nose': None, 'Mouth': None}
        # if option == 'eye':
        #     frontOrganCheck = self.draw_boundary(img, self.eyesCascade, 1.3, 5, color['red'], "Eyes", frontOrganCheck)
        # else:
        frontOrganCheck = self.draw_boundary(img, self.eyesCascade, 1.1, 5, color['red'], "Eyes", frontOrganCheck)
        frontOrganCheck = self.draw_boundary(img, self.noseCascade, 1.3, 5, color['green'], "Nose", frontOrganCheck)
        frontOrganCheck = self.draw_boundary(img, self.mouthCascade, 1.5, 5, color['white'], "Mouth", frontOrganCheck)
            # print(f'+++++{frontOrganCheck}')
        return frontOrganCheck
    
'''

'''