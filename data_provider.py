import json
import random

def get_dataset() -> list:
    with open("dataset.json", "r") as f:
        data = f.read()
        kamus_x = json.loads(data)
        return kamus_x
    
def seperate_based_on_class(data: list, target: str) -> list:
    class_seperated : dict = {}
    for x in data:
        if x[target] not in class_seperated:
            class_seperated[x[target]] = [x]
        else:
            class_seperated[x[target]].append(x)
    return class_seperated

def generate_new_case() -> dict :
    case_template = {'Clump_thickness': 2, 'Uniformity_of_cell_size': 1, 'Uniformity_of_cell_shape': 1, 'Marginal_adhesion': 1, 'Single_epithelial_cell_size': 2, 'Bare_nuclei': 1.0, 'Bland_chromatin': 1, 'Normal_nucleoli': 1, 'Mitoses': 1, 'class': 2}
    for key in case_template.keys():
        case_template[key] = random.randint(1, 10)
    del case_template['class']
    return case_template