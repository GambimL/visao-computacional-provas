from imagem import imagem
import cv2
from flask import Flask, render_template, redirect, request, Response
import numpy as np


app = Flask(__name__)
webcam = cv2.VideoCapture(0)

def generate_frames():
    while True:
        validation, frame = webcam.read()
        if not validation:
            break
        else:
           ret, buffer =  cv2.imencode('.jpg', frame)
           frame = buffer.tobytes()
        yield(b'--frame\r\n' b'contente-type: image/jpeg\r\n\r\n' + frame + b'\r\n')
        



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/corretor', methods = ['POST', ])
def corretor():
    if request.method == 'POST':
        cv2image = request.files['img']
        ANSWER_KEY = [{0: 0, 1: 0, 2: 0, 3: 3, 4: 1, 5: 3, 6: 3, 7: 2, 8: 2, 9: 2}, 
                  {0: 1, 1: 0, 2: 0, 3: 3, 4: 1, 5: 3, 6: 3, 7: 2, 8: 2, 9: 2}]
    
        img = cv2.imread('IMG_6841 (1).JPG')
        image = imagem(img)
        processadas, papers = image.pre_processa_imagem()
        pontuação, papers = image.processa_imagem(ANSWER_KEY, processadas, papers)
        imagem_pronta = cv2.hconcat(papers)
        cv2.imshow('', imagem_pronta)
        cv2.waitKey(0)

    return redirect('/corrigirprovas')


@app.route('/video')
def video():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/corrigirprovas')
def corrigir():
    return render_template('corrigirprovas.html')

@app.route('/criarprovas')
def criar_provas():
    return render_template('criarprovas.html')


if __name__ == "__main__":
    app.run(debug=True)