# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 13:18:10 2019

@author: Alex Carneiro
"""

import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import MinMaxScaler
from sklearn.pipeline import Pipeline
from sklearn.externals import joblib

def read_input_attributes(filename="attributes.txt"):
    """Função de leitura do arquivo com os nomes dos atributos"""
    
    with open(filename, 'r') as file_attr:
        return [attr.replace('\n', '') for attr in file_attr.readlines()]

def test_model(data, model):
    """Função que treina e testa um modelo de machine learning"""
    
    input_attributes = read_input_attributes()
    input_data = data[input_attributes].values
    output_data = data['class']

    train_x, test_x, train_y, test_y = train_test_split(input_data,
                                                        output_data,
                                                        test_size=.3)
    
    model.fit(train_x, train_y)
    
    print("Acurácia do modelo = %.3f"%model.score(test_x, test_y))


def create_model(data, model):
    """Função que treina e salva um modelo de machine learning"""
    
    input_attributes = read_input_attributes()
    input_data = data[input_attributes].values
    output_data = data['class']
    
    model.fit(input_data, output_data)
    
    model_filename = "model.pkl"
    joblib.dump(model, model_filename)


data = pd.read_csv("iris.data")

model = Pipeline([("norm", MinMaxScaler()),
                  ("classifier", LogisticRegression())])

test_model(data, model)
#create_model(data, model)