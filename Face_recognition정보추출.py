#recognition 정보가 있어야 하니 10장-25장 준비해서 특성 추출하기
#이미지 선처리가 중요하나 그것은 안함 (face Landmark / face Alignment)
# 128d 128vector 이미지를 encoding

import cv2
import face_recognition
import pickle #정보를 serialize(일렬로 세우기)한 후 다른 형태로 deserealize해줌


dataset_paths=['./project/dataset/minsi/','./project/dataset/ara/' ,'./project/dataset/yoonjeong/', './project/dataset/goeun/', './project/dataset/dami/', './project/dataset/chaewon/', './project/dataset/taeri/', './project/dataset/yunseo/', './project/dataset/ningning/', './project/dataset/narae/', 
                './project/dataset/boyoung/', './project/dataset/sodam/', './project/dataset/suji/', './project/dataset/sacura/', './project/dataset/eunbin/', './project/dataset/hyunjin/', './project/dataset/yejin/', './project/dataset/hyekyo/', './project/dataset/mina/', './project/dataset/sekyung/',
                './project/dataset/hyeseon/', './project/dataset/iu/', './project/dataset/ujin/', './project/dataset/nara/', './project/dataset/winter/', './project/dataset/yuna/', './project/dataset/doyeon/', './project/dataset/yeonglan/', './project/dataset/wonyoung/', './project/dataset/jeondoyeon/', 
                './project/dataset/somin/', './project/dataset/jongseo/', './project/dataset/jihuyn/', './project/dataset/jeongsomin/', './projectaet/dataset/yumi/', './project/dataset/hoyeon/', './project/dataset/jenny/', './project/dataset/ihyeon/', './project/dataset/jijel/', './project/dataset/woohee/', 
                './project/dataset/karina/', './project/dataset/kazha/', './project/dataset/hani/', './project/dataset/sohee/', './project/dataset/jimin/', './project/dataset/hyoju/', './project/dataset/yunjin/', './project/dataset/hyeri/', './project/dataset/eunchae/','./project/dataset/daniel/',

                './project/dataset/gangdaniel/','./project/dataset/dongwon/','./project/dataset/gray/','./project/dataset/jongguk/','./project/dataset/junho/','./project/dataset/woobin/','./project/dataset/youngchul/','./project/dataset/dex/','./project/dataset/dogyeom/','./project/dataset/do/',
                './project/dataset/rocco/','./project/dataset/bogeom/','./project/dataset/seojun/','./project/dataset/jaebeom/','./project/dataset/baekhyeon/','./project/dataset/v/','./project/dataset/sam/','./project/dataset/gangjun/','./project/dataset/syeonu/','./project/dataset/songgangho/',
                './project/dataset/seunggwan/','./project/dataset/ssamdi/','./project/dataset/sechan/','./project/dataset/sehyeong/','./project/dataset/yoseop/','./project/dataset/yeongjun/','./project/dataset/jaeseok/','./project/dataset/youhiyeol/','./project/dataset/gwangsu/','./project/dataset/sugeon/',
                './project/dataset/eetk/','./project/dataset/hero/','./project/dataset/junggook/','./project/dataset/woosung/','./project/dataset/jujihun/','./project/dataset/juhaknyeon/','./project/dataset/jiseokjin/','./project/dataset/changuk/','./project/dataset/chaeunwoo/','./project/dataset/woosik/',
                './project/dataset/taemin/','./project/dataset/tail/','./project/dataset/philiks/','./project/dataset/hajungwoo/','./project/dataset/hyeonbin/','./project/dataset/hyeonjin/','./project/dataset/gongyou/','./project/dataset/najaemin/','./project/dataset/gangsky/','./project/dataset/leejunho/']

# 코랩 상의 파일 경로
dataset_paths=['/content/drive/MyDrive/openSK/dataset/minsi/','/content/drive/MyDrive/openSK/dataset/ara/' ,'/content/drive/MyDrive/openSK/dataset/yoonjeong/', '/content/drive/MyDrive/openSK/dataset/goeun/', '/content/drive/MyDrive/openSK/dataset/dami/', '/content/drive/MyDrive/openSK/dataset/chaewon/', '/content/drive/MyDrive/openSK/dataset/taeri/', '/content/drive/MyDrive/openSK/dataset/yunseo/', '/content/drive/MyDrive/openSK/dataset/ningning/', '/content/drive/MyDrive/openSK/dataset/narae/', '/content/drive/MyDrive/openSK/dataset/boyoung/'
                , '/content/drive/MyDrive/openSK/dataset/sodam/', '/content/drive/MyDrive/openSK/dataset/suji/', '/content/drive/MyDrive/openSK/dataset/sacura/', '/content/drive/MyDrive/openSK/dataset/eunbin/', '/content/drive/MyDrive/openSK/dataset/hyunjin/', '/content/drive/MyDrive/openSK/dataset/yejin/', '/content/drive/MyDrive/openSK/dataset/hyekyo/', '/content/drive/MyDrive/openSK/dataset/mina/', '/content/drive/MyDrive/openSK/dataset/sekyung/', '/content/drive/MyDrive/openSK/dataset/hyeseon/', '/content/drive/MyDrive/openSK/dataset/iu/'
                , '/content/drive/MyDrive/openSK/dataset/ujin/', '/content/drive/MyDrive/openSK/dataset/nara/', '/content/drive/MyDrive/openSK/dataset/winter/', '/content/drive/MyDrive/openSK/dataset/yuna/', '/content/drive/MyDrive/openSK/dataset/doyeon/', '/content/drive/MyDrive/openSK/dataset/yeonglan/', '/content/drive/MyDrive/openSK/dataset/wonyoung/', '/content/drive/MyDrive/openSK/dataset/jeondoyeon/', '/content/drive/MyDrive/openSK/dataset/somin/', '/content/drive/MyDrive/openSK/dataset/jongseo/', '/content/drive/MyDrive/openSK/dataset/jihuyn/'
                , '/content/drive/MyDrive/openSK/dataset/jeongsomin/', '/content/drive/MyDrive/openSK/dataset/yumi/', '/content/drive/MyDrive/openSK/dataset/hoyeon/', '/content/drive/MyDrive/openSK/dataset/jenny/', '/content/drive/MyDrive/openSK/dataset/ihyeon/', '/content/drive/MyDrive/openSK/dataset/jijel/', '/content/drive/MyDrive/openSK/dataset/woohee/', '/content/drive/MyDrive/openSK/dataset/karina/', '/content/drive/MyDrive/openSK/dataset/kazha/', '/content/drive/MyDrive/openSK/dataset/hani/', '/content/drive/MyDrive/openSK/dataset/sohee/'
                , '/content/drive/MyDrive/openSK/dataset/jimin/', '/content/drive/MyDrive/openSK/dataset/hyoju/', '/content/drive/MyDrive/openSK/dataset/yunjin/', '/content/drive/MyDrive/openSK/dataset/hyeri/', '/content/drive/MyDrive/openSK/dataset/eunchae/','/content/drive/MyDrive/openSK/dataset/daniel/',

                '/content/drive/MyDrive/openSK/dataset/gangdaniel/','/content/drive/MyDrive/openSK/dataset/dongwon/' ,'/content/drive/MyDrive/openSK/dataset/gray/', '/content/drive/MyDrive/openSK/dataset/jongguk/', '/content/drive/MyDrive/openSK/dataset/junho/', '/content/drive/MyDrive/openSK/dataset/woobin/', '/content/drive/MyDrive/openSK/dataset/youngchul/', '/content/drive/MyDrive/openSK/dataset/dex/', '/content/drive/MyDrive/openSK/dataset/dogyeom/', '/content/drive/MyDrive/openSK/dataset/do/', 
                '/content/drive/MyDrive/openSK/dataset/rocco/', '/content/drive/MyDrive/openSK/dataset/bogeom/', '/content/drive/MyDrive/openSK/dataset/seojun/', '/content/drive/MyDrive/openSK/dataset/jaebeom/', '/content/drive/MyDrive/openSK/dataset/baekhyeon/', '/content/drive/MyDrive/openSK/dataset/v/', '/content/drive/MyDrive/openSK/dataset/sam/', '/content/drive/MyDrive/openSK/dataset/gangjun/', '/content/drive/MyDrive/openSK/dataset/syeonu/', '/content/drive/MyDrive/openSK/dataset/songgangho/', 
                '/content/drive/MyDrive/openSK/dataset/seunggwan/', '/content/drive/MyDrive/openSK/dataset/ssamdi/', '/content/drive/MyDrive/openSK/dataset/sechan/', '/content/drive/MyDrive/openSK/dataset/sehyeong/', '/content/drive/MyDrive/openSK/dataset/yoseop/', '/content/drive/MyDrive/openSK/dataset/yeongjun/', '/content/drive/MyDrive/openSK/dataset/jaeseok/', '/content/drive/MyDrive/openSK/dataset/youhiyeol/', '/content/drive/MyDrive/openSK/dataset/gwangsu/', '/content/drive/MyDrive/openSK/dataset/sugeon/',
                '/content/drive/MyDrive/openSK/dataset/eetk/', '/content/drive/MyDrive/openSK/dataset/hero/', '/content/drive/MyDrive/openSK/dataset/junggook/', '/content/drive/MyDrive/openSK/dataset/woosung/', '/content/drive/MyDrive/openSK/dataset/jujihun/', '/content/drive/MyDrive/openSK/dataset/juhaknyeon/', '/content/drive/MyDrive/openSK/dataset/jiseokjin/', '/content/drive/MyDrive/openSK/dataset/changuk/', '/content/drive/MyDrive/openSK/dataset/chaeunwoo/', '/content/drive/MyDrive/openSK/dataset/woosik/', 
                '/content/drive/MyDrive/openSK/dataset/taemin/', '/content/drive/MyDrive/openSK/dataset/tail/', '/content/drive/MyDrive/openSK/dataset/philiks/', '/content/drive/MyDrive/openSK/dataset/hajungwoo/', '/content/drive/MyDrive/openSK/dataset/hyeonbin/', '/content/drive/MyDrive/openSK/dataset/hyeonjin/', '/content/drive/MyDrive/openSK/dataset/gongyou/', '/content/drive/MyDrive/openSK/dataset/najaemin/', '/content/drive/MyDrive/openSK/dataset/gangsky/', '/content/drive/MyDrive/openSK/dataset/leejunho/' ]

names=['minsi','ara', 'yoonjeong', 'goeun', 'dami', 'chaewon', 'taeri', 'yunseo', 'ningning', 'narae', 
        'boyoung', 'sodam', 'suji', 'sacura', 'eunbin', 'hyunjin', 'yejin', 'hyekyo', 'mina', 'sekyung', 
        'hyeseon', 'iu', 'ujin', 'nara', 'winter', 'yuna', 'doyeon', 'yeonglan', 'wonyoung', 'jeondoyeon', 
        'somin', 'jongseo', 'jihuyn', 'jeongsomin', 'yumi', 'hoyeon', 'jenny', 'ihyeon', 'jijel', 'woohee',
        'karina', 'kazha', 'hani', 'sohee', 'jimin', 'hyoju', 'yunjin', 'hyeri', 'eunchae', 'daniel',

        'gangdaniel','dongwon','gray','jongguk','junho','woobin','youngchul','dex','dogyeom','do',
        'rocco','bogeom','seojun','jaebeom','baekhyeon','v','sam','gangjun','syeonu','songgangho',
        'seunggwan','ssamdi','sechan','sehyeong','yoseop','yeongjun','jaeseok','youhiyeol','gwangsu','sugeon',
        'eetk','hero','junggook','woosung','jujihun','juhaknyeon','jiseokjin','changuk','chaeunwoo','woosik',
        'taemin','tail','philiks','hajungwoo','hyeonbin','hyeonjin','gongyou','najaemin','gangsky','leejunho']

number_images=20
image_type='.jpg'
encoding_file='encodingsTest.pickle'
model_method='cnn' #?네? 대표적인 시각화 방법으로 정확하지만 느림/ hog는 빠르지만 정확도 낮음

knownEncodings=[]
knownNames=[]

for (i, dataset_path) in enumerate(dataset_paths): #enumerate : 인덱스와 원소를 이루어진 튜플로 만들어줌
    #이름 추출
    name=names[i]

    for idx in range(number_images): 
        file_name=dataset_path+str(idx+1)+image_type #이미지 읽어오기
        image=cv2.imread(file_name)
        rgb=cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        #boundary box
        #얼굴을 인식해서 위치를 찾음 cnn방식으로
        boxes=face_recognition.face_locations(rgb, model=model_method)

        #encoding
        encodings=face_recognition.face_encodings(rgb, boxes) #얼굴만 갖고옴
        # 128개의 real number로 되어있으니 loop를 돌리기
        for encoding in encodings:
            print(file_name, name, encoding)
            knownEncodings.append(encoding) 
            knownNames.append(name)

#save the facial encoding + 파일로 저장하기
data = {"encodings": knownEncodings, "names": knownNames}
f = open(encoding_file, "wb") #파일 열기
f.write(pickle.dumps(data)) #데이터 넣어주기
f.close()

