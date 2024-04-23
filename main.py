import json
import pandas as pd
import random
import json
import copy

def print_cantik(hashmap) -> None:
    pretty_dict = json.dumps(hashmap, indent=4)
    print(pretty_dict)

def get_dataset() -> list:
    with open("dataset.json", "r") as f:
        data = f.read()
        kamus_x = json.loads(data)
        return kamus_x

def seperate_based_on_class(data: list) -> list:
    class_seperated : dict = {}
    for x in data:
        if x['class'] not in class_seperated:
            class_seperated[x['class']] = [x]
        else:
            class_seperated[x['class']].append(x)
    return class_seperated

def get_probability(dataset : dict, feature : str, value : int =None, given : int=None) -> float:
    total = 1
    len_all = 0
    for target, data in dataset.items():
        len_all += len(data)
        if given and target != given:
            continue
        for case in data:
            try:
                if int(case[feature]) == int(value):
                    total += 1
            except:
                continue
    return total / len_all

def get_prior_probability(dataset: list, target) -> float:
    len_all = 0
    for key ,data in dataset.items():
        len_all += len(data)
    return len(dataset[target]) / len_all

def do_naive_bayes(dataset: list, features : dict) -> dict:
    probabilities = {}
    for target in dataset:
        probabilities[target] = get_prior_probability(dataset, target)
        for feature, value in features.items():
            probabilities[target] *= get_probability(dataset, feature, value, target)
    return probabilities

def generate_new_case() -> dict :
    case_template = {'Clump_thickness': 2, 'Uniformity_of_cell_size': 1, 'Uniformity_of_cell_shape': 1, 'Marginal_adhesion': 1, 'Single_epithelial_cell_size': 2, 'Bare_nuclei': 1.0, 'Bland_chromatin': 1, 'Normal_nucleoli': 1, 'Mitoses': 1, 'class': 2}
    for key in case_template.keys():
        case_template[key] = random.randint(1, 10)
    del case_template['class']
    return case_template

def test_accuracy(data) -> float:
    dataset = copy.deepcopy(data)
    banyak_data_testing = int(len(data) * 20 / 100)
    test_data : list = []
    for _ in range(banyak_data_testing):
        random_index = random.randint(0, len(dataset) - 1)
        popped = dataset.pop(random_index)
        test_data.append(popped)
    seperated_dataset : list = seperate_based_on_class(dataset)
    correct_result = 0
    for case in test_data:
        expected_value : int = case['class']
        del case['class']
        result = do_naive_bayes(seperated_dataset, case) 
        hasil_akhir = ""
        if result[2] <= result[4]:
            hasil_akhir = 4
        else:
            hasil_akhir = 2
        if (expected_value == hasil_akhir):
            correct_result += 1
    return correct_result / banyak_data_testing

def test_precision(data) -> float:
    dataset = copy.deepcopy(data)
    banyak_data_testing = int(len(data) * 20 / 100)
    test_data : list = []
    for _ in range(banyak_data_testing):
        random_index = random.randint(0, len(dataset) - 1)
        popped = dataset.pop(random_index)
        test_data.append(popped)
    seperated_dataset : list = seperate_based_on_class(dataset)
    true_positives = 0
    false_positives = 0
    for case in test_data:
        expected_value : int = case['class']
        del case['class']
        result = do_naive_bayes(seperated_dataset, case) 
        hasil_akhir = ""
        if result[2] <= result[4]:
            hasil_akhir = 4
        else:
            hasil_akhir = 2
        if hasil_akhir == expected_value and hasil_akhir == 4:
            true_positives += 1
        if hasil_akhir != expected_value and hasil_akhir == 4:
            false_positives += 1
    return true_positives/(false_positives + true_positives)


def main() -> None:
    dataset : list = get_dataset()
    print(f'Accuracy: {round(test_accuracy(dataset) * 100, 2)}%')
    print(f'Precision: {round(test_precision(dataset) * 100, 2)}%')
    # seperated_dataset : list = seperate_based_on_class(dataset)

    # while True:
    #     new_case = generate_new_case()
    #     print_cantik(new_case)
    #     result = do_naive_bayes(seperated_dataset, new_case)
    #     hasil_akhir = ""
    #     if result[2] <= result[4]:
    #         hasil_akhir = ("Malignant")
    #     else:
    #         hasil_akhir = ("Benign")
    #     print(hasil_akhir)
    #     print()
    #     if hasil_akhir == "Benign":
    #         break
if __name__ == "__main__":
    main()
