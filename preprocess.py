import csv
import pandas as pd


def _convert(size, box):
    dw = 1. / size[0]
    dh = 1. / size[1]
    x = (box[0] + box[1]) / 2.0
    y = (box[2] + box[3]) / 2.0
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x * dw
    w = w * dw
    y = y * dh
    h = h * dh
    return x, y, w, h


def _reformat_annotations(csv_reader, subset):
    """ Read annotations from the csv_reader.
    """

    for row in csv_reader:
        img_file, x1, y1, x2, y2, class_name, width, height = row[:]
        x1 = int(x1)
        x2 = int(x2)
        y1 = int(y1)
        y2 = int(y2)
        width = int(width)
        height = int(height)
        img_name = img_file[:-4]
        x_cent, y_cent, w, h = _convert((width, height), (x1, x2, y1, y2))

        with open(f'C:/Users/ronta/PycharmProjects/MultiOD/data/labels/{subset}/{img_name}.txt', "a") as file:
            file.write(f"0 {x_cent} {y_cent} {w} {h}\n")


def read_ref_annotations():
    for subset in ['train', 'val', 'test']:
        with open(f'C:/Users/ronta/PycharmProjects/MultiOD/data/annotations_{subset}.csv', 'r', newline='') as file:
            _reformat_annotations(csv.reader(file, delimiter=','), subset)


read_ref_annotations()


def create_train_test_texts():
    for subset in ['train', 'test', 'val']:
        PATH = f'C:/Users/ronta/PycharmProjects/MultiOD/data/images/{subset}/'

        df = pd.read_csv(f'C:/Users/ronta/PycharmProjects/MultiOD/data/annotations_{subset}.csv', header=None,
                         usecols=[0])
        img_set = set(df[0])
        for img in img_set:
            with open(f'{subset}.txt', 'a') as file:
                file.write(PATH + f'{img}\n')


# create_train_test_texts()

