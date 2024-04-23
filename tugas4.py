import pandas as pd
import random
import json

file_path = 'data.csv'
df = pd.read_csv(file_path)
dataset_dict = df.to_dict(orient="records")
print(dataset_dict[0])