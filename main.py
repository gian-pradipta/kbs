import json
import json
from naive_bayes import *
from data_provider import *
from performance_tester import *

def print_cantik(hashmap) -> None:
    pretty_dict = json.dumps(hashmap, indent=4)
    print(pretty_dict)


def main() -> None:
    dataset : list = get_dataset()
    print(f'Accuracy: {round(test_accuracy(dataset) * 100, 2)}%')
    print(f'Precision: {round(test_precision(dataset) * 100, 2)}%')


if __name__ == "__main__":
    main()
