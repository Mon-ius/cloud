# -*- coding:utf-8 -*-  
import os
from cloud import app
from flask_wtf import FlaskForm
from wtforms import SubmitField
from flask import request,flash,render_template,redirect
from flask_wtf.file import FileField, FileRequired, FileAllowed
from flask_uploads import UploadSet, configure_uploads, IMAGES,DATA ,\
 patch_request_class

FLASKR_SETTINGS=os.path.join(app.root_path, 'setting.cfg')
app.config.from_pyfile(FLASKR_SETTINGS, silent=True)
pathReal=app.config['UPLOADED_DATA_DEST']

Data_list = os.listdir(pathReal) #文件位置 
Data_file = UploadSet('data', DATA ) #指定文件类型

configure_uploads(app, Data_file)
patch_request_class(app) #文件大小

class UploadForm(FlaskForm):
    file = FileField(validators=[FileAllowed(Data_file, u'Data_file Only!'), \
            FileRequired(u'Choose a file!')])  #表单名
    submit = SubmitField(u'Upload')



@app.route('/del')
def del_file():
    Data_file_path=[Data_file.path(x) for x in Data_list]
    [os.remove(x) for x in Data_file_path]
    return render_template('del.html',Data_file_path=Data_file_path)

@app.route('/ds_upload', methods=['GET', 'POST'])
def ds_upload():
    form = UploadForm()
    file_urls= [Data_file.url(x)  for x in os.listdir(app.config['UPLOADED_DATA_DEST'])] 
    if form.validate_on_submit():
        filename = Data_file.save(form.file.data) #安全文件名
        if fn == filename :
            os.remove(Data_file.path(filename))
        fn = filename
        file_urls.append(Data_file.url(filename))
        flash(file_urls)
    else:
        file_url = None
        flash("wait")
    return render_template('ds_upload.html', form=form, file_urls=file_urls)

@app.route('/uploads', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        al=True
        for f in request.files.getlist('file'):
            ls = os.listdir(pathReal) #去重
            if f.filename not in ls:
                f.save(os.path.join(pathReal,f.filename))
                ls.append(f.filename)
            # Data_list.append(os.path.join(pathReal, f))
    flash("(This is just a demo. Selected files are <strong>not</strong> actually uploaded to analyse)")
    return render_template('upload.html')

@app.route('/')
def index():
    return render_template('index.html')
   


