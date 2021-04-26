from pcpartpicker import API
from math import sqrt
import pandas as pd
import csv
import numpy
from main import *



def handle_api_data():

    data = [all_data["cpu"], all_data["case"], all_data["cpu_cooler"], all_data["video_card"], 
    all_data["motherboard"], all_data["memory"], all_data["internal_hard_drive"], all_data["power_supply"]]

    cpu_dataset = []
    case_dataset = []
    cpu_cooler_dataset = []
    video_card_dataset = []
    motherboard_dataset = []
    memory_dataset = []
    internal_hard_drive_dataset = []
    power_supply_dataset = []


    for parts in data:
        for key in parts:
            for part in parts[key]:
                if not('0.00' in str(part.price)):
                    if key == 'cpu':
                            cpu_dataset.append([str(part.price.amount), part.brand + " " + part.model])
                    elif key == 'case':
                        case_dataset.append([str(part.price.amount), part.brand + " " + part.model])
                    elif key == 'cpu-cooler':
                        cpu_cooler_dataset.append([str(part.price.amount), part.brand + " " + part.model])
                    elif key == 'video-card':
                        video_card_dataset.append([str(part.price.amount), part.brand + " " + part.model])
                    elif key == 'motherboard':
                        motherboard_dataset.append([str(part.price.amount), part.brand + " " + part.model])
                    elif key == 'memory':
                        memory_dataset.append([str(part.price.amount), part.brand + " " + part.model])
                    elif key == 'internal-hard-drive':
                        internal_hard_drive_dataset.append([str(part.price.amount), part.brand + " " + part.model])
                    elif key == 'power-supply':
                        power_supply_dataset.append([str(part.price.amount), part.brand + " " + part.model])
                    else:
                        pass
                else:
                    pass

    return cpu_dataset, case_dataset, cpu_cooler_dataset, video_card_dataset, motherboard_dataset, memory_dataset, internal_hard_drive_dataset, power_supply_dataset


def handle_csv_data():

    cpu = pd.read_csv('cpu.csv', sep = ',', header = None)

    case = pd.read_csv('case.csv', sep = ',', header = None)

    cpu_cooler = pd.read_csv('cpu_cooler.csv', sep = ',', header = None)

    video_card = pd.read_csv('video_card.csv', sep = ',', header = None)

    motherboard = pd.read_csv('motherboard.csv', sep = ',', header = None)

    memory = pd.read_csv('memory.csv', sep = ',', header = None)

    internal_hard_drive = pd.read_csv('internal_hard_drive.csv', sep = ',', header = None)

    power_supply = pd.read_csv('power_supply.csv', sep = ',', header = None)

    cpu_dataset = []
    case_dataset = []
    cpu_cooler_dataset = []
    video_card_dataset = []
    motherboard_dataset = []
    memory_dataset = []
    internal_hard_drive_dataset = []
    power_supply_dataset = []

    for row in range(len(cpu)):
        cpu_dataset.append([cpu.loc[row][8], cpu.loc[row][0] + " " + cpu.loc[row][1]])

    for row in range(len(case)):
        case_dataset.append([case.loc[row][8], case.loc[row][0] + " " + case.loc[row][1]])

    for row in range(len(cpu_cooler)):
        cpu_cooler_dataset.append([cpu_cooler.loc[row][9], cpu_cooler.loc[row][0] + " " + cpu_cooler.loc[row][1]])

    for row in range(len(video_card)):
        video_card_dataset.append([video_card.loc[row][8], video_card.loc[row][0] + " " + video_card.loc[row][1]])

    for row in range(len(motherboard)):
        motherboard_dataset.append([motherboard.loc[row][7], motherboard.loc[row][0] + " " + motherboard.loc[row][1]])

    for row in range(len(memory)):
        memory_dataset.append([memory.loc[row][11], memory.loc[row][0] + " " + memory.loc[row][1]])

    for row in range(len(internal_hard_drive)):
        internal_hard_drive_dataset.append([internal_hard_drive.loc[row][9], internal_hard_drive.loc[row][0] + " " + internal_hard_drive.loc[row][1]])

    for row in range(len(power_supply)):
        power_supply_dataset.append([power_supply.loc[row][7], power_supply.loc[row][0] + " " + power_supply.loc[row][1]])

    return cpu_dataset, case_dataset, cpu_cooler_dataset, video_card_dataset, motherboard_dataset, memory_dataset, internal_hard_drive_dataset, power_supply_dataset



def calculate_distance(row1, row2):
    distance = 0.0

    for i in range(len(row1) - 1):
        try:
            distance = distance + (float(row1[i][3:].replace(',', '')) - float(row2[i][3:].replace(',', '')))**2
        except Exception as e:
            pass


    distance = sqrt(distance)

    return distance


def find_neighbors(train, test_row, num):
    distances = list()

    for train_row in train:
        distance = calculate_distance(test_row, train_row)
        distances.append((train_row, distance))

    distances.sort(key=lambda tup: tup[1])
    neighbors = list()

    for i in range(num):
        neighbors.append(distances[i][0])

    return neighbors


def predicts_class(train, test_row, num):
    neighbors = find_neighbors(train, test_row, num)
    output_vals = [row[-2] for row in neighbors]
    prediction = max(set(output_vals), key=output_vals.count)
    return prediction


def main(items, budget, purpose):

    # cpu_dataset, case_dataset, cpu_cooler_dataset, video_card_dataset, motherboard_dataset, memory_dataset, internal_hard_drive_dataset, power_supply_dataset = handle_csv_data()

    cpu_dataset, case_dataset, cpu_cooler_dataset, video_card_dataset, motherboard_dataset, memory_dataset, internal_hard_drive_dataset, power_supply_dataset = handle_api_data()

    cpu_row = [str(items['cpu'][0] + items['cpu'][1])]
    case_row = [str(items['case'][0] + items['case'][1])]
    cpu_cooler_row = [str(items['cpu-cooler'][0] + items['cpu-cooler'][1])]
    video_card_row = [str(items['video-card'][0] + items['video-card'][1])]
    motherboard_row = [str(items['motherboard'][0] + items['motherboard'][1])]
    memory_row = [str(items['memory'][0] + items['memory'][1])]
    internal_hard_drive_row = [str(items['internal-hard-drive'][0] + items['internal-hard-drive'][1])]
    power_supply_row = [str(items['power-supply'][0] + items['power-supply'][1])]

    cpu_prediction = predicts_class(cpu_dataset, cpu_row, 3)
    case_prediction = predicts_class(case_dataset, case_row, 3)
    cpu_cooler_prediction = predicts_class(cpu_cooler_dataset, cpu_cooler_row, 3)
    video_card_prediction = predicts_class(video_card_dataset, video_card_row, 3)
    motherboard_prediction = predicts_class(motherboard_dataset, motherboard_row, 3)
    memory_prediction = predicts_class(memory_dataset, memory_row, 3)
    internal_hard_drive_prediction = predicts_class(internal_hard_drive_dataset, internal_hard_drive_row, 3)
    power_supply_prediction = predicts_class(power_supply_dataset, power_supply_row, 3)

    print("Expected cpu: {}, Got: {} ".format(cpu_row[0], cpu_prediction))
    print("Expected case: {}, Got: {} ".format(case_row[0], case_prediction))
    print("Expected cpu_cooler: {}, Got: {} ".format(cpu_cooler_row[0], cpu_cooler_prediction))
    print("Expected video_card: {}, Got: {} ".format(video_card_row[0], video_card_prediction))
    print("Expected motherboard: {}, Got: {} ".format(motherboard_row[0], motherboard_prediction))
    print("Expected memory: {}, Got: {} ".format(memory_row[0], memory_prediction))
    print("Expected internal_hard_drive: {}, Got: {} ".format(internal_hard_drive_row[0], internal_hard_drive_prediction))
    print("Expected power_supply: {}, Got: {} ".format(power_supply_row[0], power_supply_prediction))

    total = round(float(cpu_prediction) +
                  float(case_prediction) +
                  float(cpu_cooler_prediction) +
                  float(video_card_prediction) +
                  float(motherboard_prediction) +
                  float(memory_prediction) +
                  float(internal_hard_drive_prediction) +
                  float(power_supply_prediction), 2)

    print('Total: {}'.format(total))
