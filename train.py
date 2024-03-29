import csv #handle the dataset
import random

# Handle the data
with open('train.data', 'rb') as csvfile:
    lines = csv.reader(csvfile)
    for row in lines:
        print(', ').join(row)

def loadDataset(filename, split, trainingSet = [], testSet = []):
    with open(filename, 'rb') as csvfile:
        lines = csv.reader(csvfile)
        dataset = list(lines)
        for x in range(len(dataset) - 1):
            for y in range(4):
                dataset[x][y] = float(dataset[x][y])
            if random.random() < split:
                trainingSet.append(dataset[x])
            else:
                testSet.append(dataset[x])