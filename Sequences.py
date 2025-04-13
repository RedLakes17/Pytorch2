#Creemos una secuencia con un dataframe
import numpy as np

def Sequences(df,seq_lenght):
    xs, ys=[],[]
    for i in range(len(df)-seq_lenght):
        x=df.iloc[i:(i+seq_lenght),1]
        y=df.iloc[i+seq_lenght,1]
        xs.append(x)
        ys.append(y)
    return np.array(xs), np.array(ys)
