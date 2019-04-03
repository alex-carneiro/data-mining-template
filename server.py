# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 13:06:13 2019

@author: Alex Carneiro
"""

import numpy as np

from sklearn.externals import joblib

from flask import Flask, request

from model_build import read_input_attributes


app = Flask("Data Mining API")

@app.route("/")
def hello():
    """Função que apresenta uma mensagem de boas vindas à API"""
    
    return "Bem vindo à API de Data Mining"


@app.route("/api")
def api():
    """Função que recebe os atributos e aplica o modelo de Machine Learning"""
    
    input_attributes = read_input_attributes() # lista de atributos
    input_vector = [] # dados de entrada
    
    # leitura dos dados enviados pela URL
    for attr in input_attributes:
        input_vector.append(float(request.args.get(attr)))
    
    # conversão da lista de dados para um array do Numpy
    input_array = np.array(input_vector).reshape((1, -1))
    
    # carregamento do modelo de machine learning
    model_filename = "model.pkl"
    model = joblib.load(model_filename)
    
    # aplicação do modelo
    prediction = model.predict(input_array)
    
    # devolve o resultado obtido pelo modelo
    return str(prediction[0])

app.run()
