#!/bin/bash

#Загрузка синтетических данных
echo 'Start generate test data'
python3 ~/mlops/data_creation.py
echo 'Finish generate test data'

#Подготовка  модели
echo 'Start preprocessing model'
python3 ~/mlops/model_preprocessing.py
echo 'Finish preprocessing model'

#Тестирование модели
echo 'Start test model'
python3 ~/mlops/model_testing.py
echo 'Finish test model'