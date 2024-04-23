import pandas as pd
import random
import json

file_path = 'data.csv'
df = pd.read_csv(file_path)
dataset_dict = df.to_dict(orient="records")

max_value = dict()
min_value = dict()
rentang = dict()

for column in df.columns:
    if column in ["diagnosis", "id", "Unnamed: 32"]:
        continue
    max_value[column] = df[column].max()
    min_value[column] = df[column].min()
    rentang[column] = abs(max_value[column] - min_value[column])

total_fitur = len(rentang)

def find_highest_similarity(kasus_baru):
    highest = 0
    highestRecord = 0
    for record in dataset_dict:
        similarity = 0
        for fitur, val in record.items():
            if fitur in ["diagnosis", "id", "Unnamed: 32"]:
                continue
            distance = abs(record[fitur] - kasus_baru[fitur]) / rentang[fitur]
            s = 1 - distance
            similarity += s
        if similarity / total_fitur >= highest:
            highest = similarity / total_fitur
            highestRecord = record
    
    return {"similarty_rate": highest, "record": highestRecord}

def generate_kasus_baru():
    kasus_baru = {
    'radius_mean': 15, 
    'texture_mean': 10, 
    'perimeter_mean': 50, 
    'area_mean': 200, 
    'smoothness_mean': 0.1, 
    'compactness_mean': 0.4, 
    'concavity_mean': 0.3, 
    'concave points_mean': 0.2,
    'symmetry_mean': 0.2, 
    'fractal_dimension_mean': 0.1, 
    'radius_se': 2.3, 
    'texture_se': 4, 
    'perimeter_se': 20,
    'area_se': 530, 
    'smoothness_se': 0.03, 
    'compactness_se': 0.130, 
    'concavity_se': 0.2, 
    'concave points_se': 0.03, 
    'symmetry_se': 0.07, 
    'fractal_dimension_se': 0.03, 
    'radius_worst': 28, 
    'texture_worst': 14, 
    'perimeter_worst': 65, 
    'area_worst': 2500, 
    'smoothness_worst': 0.1, 
    'compactness_worst': 1, 
    'concavity_worst': 1, 
    'concave points_worst': 0.291, 
    'symmetry_worst': 0.5073, 
    'fractal_dimension_worst': 0.15
}
    for fitur in kasus_baru.keys():
        kasus_baru[fitur] = random.uniform(min_value[fitur], max_value[fitur])
    return kasus_baru

def print_cantik(hashmap):
    pretty_dict = json.dumps(hashmap, indent=4)
    print(pretty_dict)

kasus_baru = generate_kasus_baru()
print_cantik(kasus_baru)
record_with_highest_similarity = find_highest_similarity(kasus_baru)
print_cantik(record_with_highest_similarity)