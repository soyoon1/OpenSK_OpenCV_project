import cv2
import face_recognition
import pickle
import dlib
import numpy as np
# from PIL import Image

image_file="project/dataset/hani/1.jpg"
encoding_file="project/encodings4.pickle"
unknown_name="Unknown"
model_method="cnn"

def detectAndDisplay(image):
    images = np.array(image)
    rgb=cv2.cvtColor(images, cv2.COLOR_BGR2RGB)

    #얼굴 인식 부분 박스 그리기
    boxes = face_recognition.face_locations(rgb,model=model_method)
    #박스 인식 부분을 encoding 해주기
    encodings = face_recognition.face_encodings(rgb, boxes)

    names=[]

    for encoding in encodings:
        matches = face_recognition.compare_faces(data["encodings"],encoding)
        name = unknown_name

        #매치 여부 확인
        if True in matches:
            #매치 index 값 주기
            matchedIdxs = [i for (i, b) in enumerate(matches) if b]
            counts = {}

            #어떤 내용으로 매치 되었는지 for문 돌리기
            for i in matchedIdxs:
                name = data["names"][i]
                counts[name] = counts.get(name, 0) + 1
                print(name,counts[name])

            #가장 많이 이름이 나온 것으로 결정
            name = max(counts, key=counts.get)
        
        
        #이름 넣어주기/없으면 unknown
        names.append(name)
        #print(name)

    #name이 image dataset에 있으면 해당 이미지의 첫번째 사진을 출력
    if name in data["names"]:
        path="project/dataset/"+name+"/1.jpg"
        img = cv2.imread(path)
        cv2.imshow("talent image", img)
        cv2.imshow("original image", image)
   


data=pickle.loads(open(encoding_file,"rb").read())

#align 보정작업
RIGHT_EYE = list(range(36, 42))
LEFT_EYE = list(range(42, 48))
EYES = list(range(36, 48))

predictor_file = 'shape_predictor_68_face_landmarks.dat'
MARGIN_RATIO = 1.5 #얼굴이 조금더 크게 나오게 함
OUTPUT_SIZE = (300, 300)

detector = dlib.get_frontal_face_detector() #얼굴 찾기
predictor = dlib.shape_predictor(predictor_file) #점 찍기

image=cv2.imread(image_file)
image_origin = image.copy()

(image_height, image_width) = image.shape[:2]
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

rects = detector(gray, 1)

def getFaceDimension(rect):
    return (rect.left(), rect.top(), rect.right() - rect.left(), rect.bottom() - rect.top())

def getCropDimension(rect, center):
    width = (rect.right() - rect.left())
    half_width = width // 2
    (centerX, centerY) = center
    startX = centerX - half_width
    endX = centerX + half_width
    startY = rect.top()
    endY = rect.bottom() 
    return (startX, endX, startY, endY)    

for (i, rect) in enumerate(rects): #얼굴 인식한 것들을 for문 돌려주기
    (x, y, w, h) = getFaceDimension(rect)
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

    points = np.matrix([[p.x, p.y] for p in predictor(gray, rect).parts()])
    show_parts = points[EYES]

    right_eye_center = np.mean(points[RIGHT_EYE], axis = 0).astype("int")
    left_eye_center = np.mean(points[LEFT_EYE], axis = 0).astype("int")
    print(right_eye_center, left_eye_center)

    cv2.circle(image, (right_eye_center[0,0], right_eye_center[0,1]), 5, (0, 0, 255), -1)
    cv2.circle(image, (left_eye_center[0,0], left_eye_center[0,1]), 5, (0, 0, 255), -1)
    
    cv2.circle(image, (left_eye_center[0,0], right_eye_center[0,1]), 5, (0, 255, 0), -1)
    
    cv2.line(image, (right_eye_center[0,0], right_eye_center[0,1]),
            (left_eye_center[0,0], left_eye_center[0,1]), (0, 255, 0), 2)
    cv2.line(image, (right_eye_center[0,0], right_eye_center[0,1]),
        (left_eye_center[0,0], right_eye_center[0,1]), (0, 255, 0), 1)
    cv2.line(image, (left_eye_center[0,0], right_eye_center[0,1]),
        (left_eye_center[0,0], left_eye_center[0,1]), (0, 255, 0), 1)

    eye_delta_x = right_eye_center[0,0] - left_eye_center[0,0]
    eye_delta_y = right_eye_center[0,1] - left_eye_center[0,1]
    degree = np.degrees(np.arctan2(eye_delta_y,eye_delta_x)) - 180

    eye_distance = np.sqrt((eye_delta_x ** 2) + (eye_delta_y ** 2))
    aligned_eye_distance = left_eye_center[0,0] - right_eye_center[0,0]
    scale = aligned_eye_distance / eye_distance

    eyes_center = (int((left_eye_center[0,0] + right_eye_center[0,0]) // 2), int((left_eye_center[0,1] + right_eye_center[0,1]) // 2))
    cv2.circle(image, eyes_center, 5, (255, 0, 0), -1)
            
    metrix = cv2.getRotationMatrix2D(eyes_center, degree, scale)
    cv2.putText(image, "{:.5f}".format(degree), (right_eye_center[0,0], right_eye_center[0,1] + 20),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)

    warped = cv2.warpAffine(image_origin, metrix, (image_width, image_height),
        flags=cv2.INTER_CUBIC)
    
    cv2.imshow("warpAffine", warped)
    (startX, endX, startY, endY) = getCropDimension(rect, eyes_center)
    croped = warped[startY:endY, startX:endX]
    output = cv2.resize(croped, OUTPUT_SIZE)
    cv2.imshow("output", output)

    for (i, point) in enumerate(show_parts):
        x = point[0,0]
        y = point[0,1]
        cv2.circle(image, (x, y), 1, (0, 255, 255), -1)


detectAndDisplay(image)
cv2.waitKey(0)
cv2.destroyAllWindows()