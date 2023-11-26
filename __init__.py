import os
from flask import Flask,request, send_from_directory
from . import Resemble_prj
from flask.templating import render_template
from werkzeug.utils import secure_filename
import cv2 as cv

def create_app():
    app = Flask(__name__, static_url_path='')

    app.config['UPLOAD_FOLDER'] = 'project/static/images'
    app.config['RESULT_FOLDER'] = 'project/static/result_images/'

    @app.route('/upload_img/<filename>') # 서버에 저장되어 있는 이미지 클라이언트로 전달.
    def upload_img(filename):
        return send_from_directory(app.config['UPLOAD_FOLDER'], filename) # 폴더에 대한 정보가 첫 번째 파라미터에 들어감. 그리고 찾고자 하는 파일 이름

    @app.route('/result_img/<filename>')
    def result_img(filename):
        return send_from_directory(app.config['RESULT_FOLDER'], filename)
    
    @app.route('/', methods=['GET'])
    def img_processing():
        return render_template('mainpage.html')

    @app.route('/img_result', methods=['GET', 'POST'])
    def img_result():
        if request.method == 'POST':
            f = request.files['file']  # form에서 사용자가 선택한 모든 값들이 전달됨. 사용자가 전달해준 것 중 id가 file인 것을 사용하겠다. /img_processing이 사용자

            # Save the file to ./uploads
            basepath = os.path.dirname(__file__)
            file_path = os.path.join(basepath, 'project/static/images', secure_filename(f.filename)) # basepath 프로젝트 파일, 그리고 upload 파일 및에 있는 것들, 그리고 파일 이름
            print(file_path)
            f.save(file_path) # 가져온 것 저장
            file_name = os.path.basename(file_path)
            print(file_name)

            # reading the uploaded image
            img = cv.imread(file_path)

            resemble_path=Resemble_prj.detectAndDisplay(file_path)
        
            return render_template('resultpage.html', file_name=file_name, result_file=resemble_path) # 거기에 들어갈 이미지의 이름을 전달해줌. 클라이언트에서 그 해당하는 이미지를 찾아서 보여줘라는 것.
        return ""
    return app

    #         # processing 지금은 따로 안 하고 동일한 이미지를 저장하겠다.
    #         style = request.form.get('style')
    #         if style == 'Embossing' :
    #             # Embossing
    #             output = embossing(img)

    #             # Write the result to ./result_images
    #             result_fname = os.path.splitext(file_name)[0] + "_emboss.jpg" # splitext: 확장자를 기준으로 나눠줌.
    #             result_path = os.path.join(basepath, 'result_images', secure_filename(result_fname)) # result_images라는 폴더에  저장하겠다.
    #             fname = os.path.basename(result_path)
    #             cv.imwrite(result_path, output)

    #             return render_template('img_result.html', file_name=file_name, result_file=fname) # 거기에 들어갈 이미지의 이름을 전달해줌. 클라이언트에서 그 해당하는 이미지를 찾아서 보여줘라는 것.

    #         elif style == 'Cartoon' :

    #             output = cartoon(img)

    #             # Write the result to ./result_images
    #             result_fname = os.path.splitext(file_name)[0] + "_cartoon.jpg" # splitext: 확장자를 기준으로 나눠줌.
    #             result_path = os.path.join(basepath, 'result_images', secure_filename(result_fname)) # result_images라는 폴더에  저장하겠다.
    #             fname = os.path.basename(result_path)
    #             cv.imwrite(result_path, output)

    #             return render_template('img_result.html', file_name=file_name, result_file=fname) # 거기에 들어갈 이미지의 이름을 전달해줌. 클라이언트에서 그 해당하는 이미지를 찾아서 보여줘라는 것.

    #         elif style == 'PencilGray' :
    #             output = pencilGray(img)

    #             # Write the result to ./result_images
    #             result_fname = os.path.splitext(file_name)[0] + "_pencilgray.jpg" # splitext: 확장자를 기준으로 나눠줌.
    #             result_path = os.path.join(basepath, 'result_images', secure_filename(result_fname)) # result_images라는 폴더에  저장하겠다.
    #             fname = os.path.basename(result_path)
    #             cv.imwrite(result_path, output)

    #             return render_template('img_result.html', file_name=file_name, result_file=fname) # 거기에 들어갈 이미지의 이름을 전달해줌. 클라이언트에서 그 해당하는 이미지를 찾아서 보여줘라는 것.

    #         elif style == 'PencilColor' :

    #             output = pencilColor(img)

    #             # Write the result to ./result_images
    #             result_fname = os.path.splitext(file_name)[0] + "_pencilcolor.jpg" # splitext: 확장자를 기준으로 나눠줌.
    #             result_path = os.path.join(basepath, 'result_images', secure_filename(result_fname)) # result_images라는 폴더에  저장하겠다.
    #             fname = os.path.basename(result_path)
    #             cv.imwrite(result_path, output)

    #             return render_template('img_result.html', file_name=file_name, result_file=fname) # 거기에 들어갈 이미지의 이름을 전달해줌. 클라이언트에서 그 해당하는 이미지를 찾아서 보여줘라는 것.

    #         elif style == 'OilPainting' :

    #             output = oilPainting(img)

    #             # Write the result to ./result_images
    #             result_fname = os.path.splitext(file_name)[0] + "_oil.jpg" # splitext: 확장자를 기준으로 나눠줌.
    #             result_path = os.path.join(basepath, 'result_images', secure_filename(result_fname)) # result_images라는 폴더에  저장하겠다.
    #             fname = os.path.basename(result_path)
    #             cv.imwrite(result_path, output)

    #             return render_template('img_result.html', file_name=file_name, result_file=fname) # 거기에 들어갈 이미지의 이름을 전달해줌. 클라이언트에서 그 해당하는 이미지를 찾아서 보여줘라는 것.

    #         elif style == 'DetailEnhance' :

    #             output = detailEnhance(img)

    #             # Write the result to ./result_images
    #             result_fname = os.path.splitext(file_name)[0] + "_detail.jpg" # splitext: 확장자를 기준으로 나눠줌.
    #             result_path = os.path.join(basepath, 'result_images', secure_filename(result_fname)) # result_images라는 폴더에  저장하겠다.
    #             fname = os.path.basename(result_path)
    #             cv.imwrite(result_path, output)

    #             return render_template('img_result.html', file_name=file_name, result_file=fname) # 거기에 들어갈 이미지의 이름을 전달해줌. 클라이언트에서 그 해당하는 이미지를 찾아서 보여줘라는 것.


    #     return ""

    # return app

    # # @app.route('/', methods=['GET','POST'])
    # # def hello():
    # #     if request.method=='GET':
    # #         return render_template('mainpage.html')
        
    # #     elif request.method=='POST':
    # #         chooseFile=request.files["chooseFile"]
    # #         chooseFile.save('project/static/images/'+str(chooseFile.filename))
    # #         chooseFile_path='project/static/images/'+str(chooseFile.filename)

    # #         resembleFile=Resemble_prj.detectAndDisplay(chooseFile_path)
    # #         resembleFile_path='./static/images/'+str(resembleFile.split('/')[-1])

    # #     return render_template('mainpage.html',chooseFile= chooseFile_path, resembleFile=resembleFile_path)

    # @app.route('/result', methods=['GET','POST'])


    # # if __name__ == "__main__":
    # #     app.run(host="127.0.0.1", port=5000)            