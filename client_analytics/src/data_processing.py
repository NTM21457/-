import pandas as pd

def load_data(filepath):
    df = pd.read_csv(filepath)
    return df

def get_insights(df):
    df['баланс'] = pd.to_numeric(df['баланс'], errors='coerce')
    average=df['баланс'].mean()
    average2=df['возраст'].mean()
    average3=df['доход'].mean()
    average=pd.DataFrame({
        'клиент': ['Среднее'],
        'возраст': [average2],
        'регион': [None],
        'баланс': [average],
        'доход': [average3]
    })
    df2 = pd.concat([df, average])
    return df2