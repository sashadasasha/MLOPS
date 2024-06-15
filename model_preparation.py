import pandas as pd

from sklearn.preprocessing import StandardScaler, MinMaxScaler

def prepare_data(path):
    DF = pd.read_csv(path, encoding='utf-8', sep=',')

    DF_ = DF.drop('target', axis = 1)

    col_name = ['feat1', 'feat2', 'feat3', 'feat4']

    standard = StandardScaler()
    standard.fit(DF_)

    stand_data = standard.transform(DF_[col_name])
    DF_stand = pd.DataFrame(stand_data, columns=col_name)

    scaler = MinMaxScaler()
    scaler.fit(DF_stand)

    scale_data = scaler.transform(DF_stand)
    DF_scale = pd.DataFrame(scale_data, columns=col_name)
    
    return pd.concat((DF_scale, DF['target']), axis=1)