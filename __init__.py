# from flask import Flask,request
# from . import Resemble_prj
# from flask.templating import render_template

# app = Flask(__name__)
# @app.route('/', methods=['GET','POST'])
# def hello():
#     if request.method=='GET':
#         return render_template('./templates/mainpage.html')
    
#     elif request.method=='POST':
#         chooseFile=request.files["chooseFile"]
#         chooseFile.save('./static/images/'+str(chooseFile.filename))
#         chooseFile_path='./static/images/'+str(chooseFile.filename)

#         resembleFile=Resemble_prj.detectAndDisplay(chooseFile_path)
#         resembleFile_path='./statis/images/'+str(resembleFile.split('/')[-1])

#     return render_template('mainpage.html',chooseFile= chooseFile_path, resembleFile=resembleFile_path)

# # if __name__ == "__main__":
# #     app.run(host="127.0.0.1", port=5000)          



from flask import Flask,request
from . import Resemble_prj
from flask.templating import render_template

app = Flask(__name__)
@app.route('/', methods=['GET','POST'])
def hello():
    if request.method=='GET':
        return render_template('mainpage.html')
    
    elif request.method=='POST':
        chooseFile=request.files["chooseFile"]
        chooseFile.save('project/static/images/'+str(chooseFile.filename))
        chooseFile_path='project/static/images/'+str(chooseFile.filename)

        resembleFile=Resemble_prj.detectAndDisplay(chooseFile_path)
        resembleFile_path='./static/images/'+str(resembleFile.split('/')[-1])

    return render_template('mainpage.html',chooseFile= chooseFile_path, resembleFile=resembleFile_path)

# if __name__ == "__main__":
#     app.run(host="127.0.0.1", port=5000)            