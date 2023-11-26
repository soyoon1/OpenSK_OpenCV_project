import os
import cv2 as cv

from flask import Flask, render_template, request, send_from_directory
from werkzeug.utils import secure_filename
from flask import send_file

import os
from flask import Flask,request, send_from_directory
from . import Resemble_prj
from flask.templating import render_template
from werkzeug.utils import secure_filename
import cv2 as cv
from pybo.img_processing import embossing, cartoon, pencilGray, pencilColor, oilPainting, detailEnhance


# 공통적으로 사용할 수 있는 폴더를 반드시 하나 만들어줘야 함.

def create_app():
    app = Flask(__name__, static_url_path='')  # 앱을 만들어 줌. 플라스크가 구동되어져 있는 서버의 역할을 하는 파일로 쓰겠다라는 것을 의미

    app.secret_key = os.urandom(24) # 랜덤 값
    app.config['RESULT_FOLDER'] = 'dataset'  # 반드시 폴더 미리 생성
    app.config['UPLOAD_FOLDER'] = 'uploads'  # 반드시 폴더 미리 생성

    @app.route('/img_processing/', methods=['GET'])
    def img_processing():
        return render_template('img_processing.html')

    @app.route('/upload_img/<filename>') # 서버에 저장되어 있는 이미지 클라이언트로 전달.
    def upload_img(filename):
        return send_from_directory(app.config['UPLOAD_FOLDER'], filename) # 폴더에 대한 정보가 첫 번째 파라미터에 들어감. 그리고 찾고자 하는 파일 이름

    @app.route('/result_img/<filename>')
    def result_img(filename):
        # 파일name에 찾고자 하는 연예인 이름+1.jpg
        # split을 해서 연예인이름   1.jpg
        # 1.jpg는 filename으로, 연예인이름은 app.config['UPLOAD_FOLDER']+"/"+연예인이름해서 밑에 있는 함수의 첫번째 매개변수로 집어넣음.
        # 띄어쓰기를 기준으로 문자열 분리
        name_parts = filename.split('_')
        print(name_parts)
        print(name_parts[0])
        print(name_parts[1])
        # 분리된 부분 확인
        name_part = name_parts[0]  # 여기서는 'Minji'를 가져옴
        number_part = name_parts[1]  # 여기서는 '1.jpg'를 가져옴

        print(name_part)
        print(number_part)
        directory_path = app.config['RESULT_FOLDER']+"/"+name_part
        return send_from_directory(directory_path, number_part) # 폴더에 대한 정보가 첫 번째 파라미터에 들어감. 그리고 찾고자 하는 파일 이름




    @app.route('/img_result', methods=['GET', 'POST'])
    def img_result():
        if request.method == 'POST':
            f = request.files['file']  # form에서 사용자가 선택한 모든 값들이 전달됨. 사용자가 전달해준 것 중 id가 file인 것을 사용하겠다. /img_processing이 사용자

            # Save the file to ./uploads
            basepath = os.path.dirname(__file__)
            file_path = os.path.join(basepath, 'uploads', secure_filename(f.filename)) # basepath 프로젝트 파일, 그리고 upload 파일 및에 있는 것들, 그리고 파일 이름
            print(file_path)
            f.save(file_path) # 가져온 것 저장
            file_name = os.path.basename(file_path)
            print(file_name)

            # reading the uploaded image
            img = cv.imread(file_path)

            # processing 지금은 따로 안 하고 동일한 이미지를 저장하겠다.
            # style = request.form.get('style')
            # if style == 'Embossing' :
                # Embossing
# processing
            output_name = Resemble_prj.detectAndDisplay(img)  # Get the name returned by the function
            
            # Write the result to ./pybo/dataset/{name}/1.jpg
            result_folder_name = output_name
            print(output_name)
            result_fname = output_name+"/1.jpg"
            result_path = os.path.join(secure_filename(result_fname))
            fname = os.path.basename(result_path)
            
            # Save the result image
            # cv.imwrite(result_path, output)

            return render_template('img_result.html', file_name=file_name, result_file=fname, output_name=output_name)


        return ""

    @app.route('/')
    def index():
        # return "hello~~~pybo 패키지~~~"
        return render_template('index.html')  # 이 html을 클라이언트에 전달하겠다.

    return app

