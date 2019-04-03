# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 18:03:51 2019

@author: Alex Carneiro
"""

from urllib import request


sepal_lenth = "sepal_length=" + input("Sepal length: ")
sepal_width = "sepal_width=" + input("Sepal width: ")
petal_lenth = "petal_length=" + input("Petal length: ")
petal_width = "petal_width=" + input("Petal width: ")

url_path = 'http://localhost:5000/api?%s&%s&%s&%s'%(sepal_lenth,
                                                    sepal_width,
                                                    petal_lenth,
                                                    petal_width)

with request.urlopen(url_path) as response:
    result = str(response.read())

print("A classe para a flor com {%s, %s, %s, %s} é %s"%(sepal_lenth,
                                                        sepal_width,
                                                        petal_lenth,
                                                        petal_width,
                                                        result))
