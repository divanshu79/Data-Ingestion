import pandas as pd
import os

df = pd.read_excel('ISO10383_MIC.xls', sheet_name="MICs List by CC")
# print(df.head())
try:
    os.remove('file.json')
except:
    pass

file = df.to_json(path_or_buf='file.json', orient='records')
