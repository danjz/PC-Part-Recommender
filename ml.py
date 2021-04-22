from pcpartpicker import API
from math import sqrt
import pandas as pd
import csv
import numpy
import recommend

items, budget, purpose = recommend.User()


def calculate_distance(row1, row2):
    distance = 0.0

    for i in range(len(row1 - 1)):
        distance = distance + (row1[i] - row2[i])**2

    distance = sqrt(distance)

    return distance


def find_neighbors(train, test_row, num):
    distances = list()

    for train_row in train:
        distance = calculate_distance(test_row, train_row)
        distances.append(train_row, distance)

    distances.sort(key=lambda tup: tup[1])
    neighbors = list()

    for i in range(num):
        neighbors.append(distances[i][0])

    return neighbors


def predicts_class(train, test_row, num):
    neighbors = find_neighbors(train, test_row, num)
    output_vals = [row[-1] for row in neighbors]
    prediction = max(set(output_vals), key=output_vals.count)
    return prediction


cpu = pd.read_csv('cpu.csv', sep = ',', header = None)

case = pd.read_csv('case.csv', sep = ',', header = None)

cpu_cooler = pd.read_csv('cpu_cooler.csv', sep = ',', header = None)

video_card = pd.read_csv('video_card.csv', sep = ',', header = None)

motherboard = pd.read_csv('motherboard.csv', sep = ',', header = None)

memory = pd.read_csv('memory.csv', sep = ',', header = None)

internal_hard_drive = pd.read_csv('internal_hard_drive.csv', sep = ',', header = None)

power_supply = pd.read_csv('power_supply.csv', sep = ',', header = None)

# print(cpu)
# print(case)
# print(cpu_cooler)
# print(video_card)
# print(motherboard)
# print(memory)
# print(internal_hard_drive)
# print(power_supply)

dfs = [cpu, case, cpu_cooler, video_card, motherboard, memory, internal_hard_drive, power_supply]

dataset = []

for df in dfs:
    for row in range(len(df)):
        # print(df.loc[row])
    # print(df.name)
        dataset.append([df.loc[row][7], df.loc[row][0] + " " + df.loc[row][1]])

print(dataset)

test_row = []
