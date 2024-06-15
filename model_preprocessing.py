from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from model_preparation import prepare_data
import pickle as pick
import pathlib

model = RandomForestRegressor(random_state=25)

DF = prepare_data('./train.csv')

X_train, X_test, y_train, y_test = train_test_split(
    DF.drop('target', axis=1),
    DF['target'],
    test_size=0.18,
    random_state=25
)

model.fit(X_train, y_train)

with open('./model.pkl', 'wb') as pickFile:
        pick.dump(model, pickFile)