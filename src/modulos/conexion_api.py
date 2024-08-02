# Definicion de funcion de extraccion API
import requests
import pandas as pd
import json
import warnings

warnings.simplefilter("ignore")

url_API="http://api.bcra.gob.ar/estadisticas/v2.0/principalesvariables"

def extraccion_API(url):
    response=requests.get(url, verify=False)
    if response.status_code==200:
        data=response.json()
        df=pd.json_normalize(data,record_path="results")
        df['valor']=round(df['valor'])
        df['fecha']=pd.to_datetime(df['fecha'])
        return df
    else:
        print(f"Error {response.status_code}")
        return None