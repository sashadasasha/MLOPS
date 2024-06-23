#!/bin/bash

# Получение пути к директории Jenkins Home
JENKINS_HOME="$JENKINS_HOME"

# Путь к каталогу сборки
BUILD_DIR="../"

# Создание каталога build в корневом каталоге
mkdir -p "$BUILD_DIR" || { echo "Ошибка при создании каталога 'build'."; exit 1; }


# Создание виртуального окружения
python3 -m venv "$BUILD_DIR/venv" || { echo "Ошибка при создании виртуального окружения."; exit 1; }

# Активация виртуального окружения
source "$BUILD_DIR/venv/bin/activate" || { echo "Ошибка при активации виртуального окружения."; exit 1; }

# Установка зависимостей
pip install -r "$BUILD_DIR/requirements.txt" || { echo "Ошибка при установке зависимостей."; exit 1; }

echo "Запуск создания данных"
python3 ../data_creation.py || { echo "Ошибка при выполнении data_creation.py"; exit 1; }

echo "Запуск предобработки данных"
python3 ../model_preprocessing.py || { echo "Ошибка при выполнении model_preprocessing.py"; exit 1; }

echo "Запуск подготовки и обучения модели"
python3 ../model_preparation.py || { echo "Ошибка при выполнении model_preparation.py"; exit 1; }

echo "Запуск тестирования модели"
python3 ../model_testing.py || { echo "Ошибка при выполнении model_testing.py"; exit 1; }