import pickle as pick
from model_preparation import prepare_data

def load_model(model_path):
    with open(model_path, 'rb') as f:
        model = pick.load(f)
    return model

model_path = './model.pkl'
data_path = './test.csv'
model = load_model(model_path)
DF = prepare_data(data_path)

X_test, y_test = DF.drop('target', axis=1), DF['target']

y_pred = model.predict(X_test)

with open('./submissions.txt', 'w') as f:
    f.write(str(y_pred))