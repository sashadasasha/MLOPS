import pandas as pd
import numpy as np
from pathlib import Path

np.random.seed(25)

loc, scale = 10, 1
mu, sigma = 3., 1. # mean and standard deviation

#генерация псевдоданных
samples_count = 5000
features = {
    "feat1": np.random.logistic(loc, scale, samples_count),
    "feat2": np.random.poisson(15, samples_count),
    "feat3": np.random.normal(loc, scale, samples_count),
    "feat4": np.random.lognormal(mu, sigma, samples_count),
}

features['target'] = (features["feat1"] * 3 +
                      features['feat2'] * 3 +
                      features["feat3"] * 2 + 
                      features["feat4"] * 4)

#тренировочный и тестовый датафреймы
train = pd.DataFrame(features).sample(frac=0.9, random_state=25)
test = pd.DataFrame(features).drop(train.index)

filepath_train = Path('./train.csv')
filepath_test = Path('./test.csv')

#Сохраняем файлы
train.to_csv(filepath_train, index=False)
test.to_csv(filepath_test, index=False)

print("Сгенерирована тренировочная выборка ", filepath_train)
print("Сгенерирована тестовая выборка ", filepath_test)