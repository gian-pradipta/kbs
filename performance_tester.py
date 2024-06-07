import random
from naive_bayes import *
import copy

def test_accuracy(data) -> float:
    dataset = copy.deepcopy(data)
    banyak_data_testing = int(len(data) * 20 / 100)
    test_data : list = []
    for _ in range(banyak_data_testing):
        random_index = random.randint(0, len(dataset) - 1)
        popped = dataset.pop(random_index)
        test_data.append(popped)
    seperated_dataset : list = seperate_based_on_class(dataset, "class")
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
    seperated_dataset : list = seperate_based_on_class(dataset, "class")
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