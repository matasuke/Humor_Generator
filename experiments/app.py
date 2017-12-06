import os
import sys
import argparse
import flask
from flask import Flask, render_template, request, jsonify, Response, url_for
from werkzeug import secure_filename
import random
import json
import pandas as pd

from WEB_ENV import (
        EXP1_NUM,
        IMG_DIR_PATH,
        EXP1_DATA_PATH
    )

def get_data_exp1(data_path, image_dir, num):
    csv_data = pd.read_csv(data_path)
    data = csv_data.sample(num)
    
    images = [ os.path.join(image_dir, image.strip()).split('/', 1)[1] for image in data.iloc[:, 1]]
    captions = [ cap for cap in data.iloc[:, 2]]
    humor_captions = [ humor_cap for humor_cap in data.iloc[:, 3]]

    return images, captions, humor_captions

def get_image_list(image_dir):
    file_list = [ os.path.join(image_dir, img_path).split('/', 1)[1] for img_path in os.listdir(image_dir)]

    return file_list

def get_image_path(img_list, num):
    img_path = random.sample(img_list, num)

    return img_path


app = Flask(__name__)

@app.route('/', methods=['GET'])
def log_in():
    return render_template('index.html')

@app.route('/description', methods=['POST'])
def experiment_description():
    if request.method == 'POST':
        values = request.form

        if values['name'] and values['age'] and values['sex']:
            name = values['name']
            age = values['age']
            sex = values['sex']
            
            print(name)
            print(age)
            print(sex)

    return render_template('description.html')

@app.route('/pre-survey')
def pre_survey():
    return render_template('pre_survey.html')

@app.route('/experiment1', methods=['POST'])
def experiment1():
    if request.method == 'POST':
        values = request.form
        
        q1 = values['q1']
        q2 = values['q2']
        q3 = values['q3']
        q4 = values['q4']
        q5 = values['q5']
        q6 = values['q6']
        q7 = values['q7']
        q8 = values['q8']

    print(q1)
    print(q2)
    print(q3)
    print(q4)
    print(q5)
    print(q6)
    print(q7)
    print(q8)

    return render_template('experiment1_detail.html', experiment_no = 'システム評価実験1', experiment_url = 'experiment1_content')

@app.route('/experiment1_content', methods=['GET'])
def experiment1_content():
    
    images, captions, humor_captions = get_data_exp1(EXP1_DATA_PATH, IMG_DIR_PATH, EXP1_NUM)

    return render_template('experiment1.html', images=images, captions = captions, humor_captions = humor_captions)

if __name__=='__main__':

    img_list = get_image_list(IMG_DIR_PATH)

    app.run(debug=True)
