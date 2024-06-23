#!/bin/bash

echo "Запуск создания данных"
python3 ./data_creation.py || { echo "Ошибка при выполнении data_creation.py"; exit 1; }

echo "Запуск предобработки данных"
python3 ./model_preprocessing.py || { echo "Ошибка при выполнении model_preprocessing.py"; exit 1; }

echo "Запуск подготовки и обучения модели"
python3 ./model_preparation.py || { echo "Ошибка при выполнении model_preparation.py"; exit 1; }

echo "Запуск тестирования модели"
python3 ./model_testing.py || { echo "Ошибка при выполнении model_testing.py"; exit 1; }