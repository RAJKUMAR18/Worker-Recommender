import json
import requests
import pandas as pd
header = {'Content-Type': 'application/json', \
                  'Accept': 'application/json'}

df = pd.read_csv(../data1.csv, encoding="utf-8-sig")
df = df.head()

data = df.to_json(orient='records')
resp = requests.post("http://0.0.0.0:8000/predict", \
                    data = json.dumps(data),\
                    headers= header)

resp.json()
