#Creado por Enrique Vergara
#!/usr/bin/env python
# -*- coding: utf-8 -*- 
from distutils.log import debug
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/enunciados')
def enunciados():
    return render_template('enunciados.html')

@app.route('/solutions')
def solution():
    return render_template('solution.html')

if __name__ == '__main__':
    app.run(debug=True)
    #app.run(host='0.0.0.0', port=5000)