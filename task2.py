import csv# TODO импортировать необходимые молули
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    with open(INPUT_FILENAME) as f:  # TODO считать содержимое csv файла
        lines = [line for line in csv.DictReader(f)]

    with open(OUTPUT_FILENAME, 'w') as f:  # TODO Сериализовать в файл с отступами равными 4
        json.dump(lines, f, indent=4)

if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
