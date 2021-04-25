from pcpartpicker import API
from math import sqrt
import pandas as pd
import csv
import numpy
import recommend

# items, budget, purpose, all_data = recommend.User()


def handle_api_data():
    api = API('uk')
    cpu = api.retrieve('cpu')
    case = api.retrieve('case')
    cpu_cooler = api.retrieve('cpu-cooler')
    video_card = api.retrieve('video-card')
    motherboard = api.retrieve('motherboard')
    memory = api.retrieve('memory')
    internal_hard_drive = api.retrieve('internal-hard-drive')
    power_supply = api.retrieve('power-supply')

    data = [cpu, case, cpu_cooler, video_card, motherboard, memory, internal_hard_drive, power_supply]


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


def main():

    # cpu_dataset, case_dataset, cpu_cooler_dataset, video_card_dataset, motherboard_dataset, memory_dataset, internal_hard_drive_dataset, power_supply_dataset = handle_csv_data()
    # print(cpu_dataset)

    cpu_dataset, case_dataset, cpu_cooler_dataset, video_card_dataset, motherboard_dataset, memory_dataset, internal_hard_drive_dataset, power_supply_dataset = handle_api_data()
    # print(case_dataset)

    # cpu_row = [items['cpu'][0] + items['cpu'][1]]
    # case_row = [items['case'][0] + items['case'][1]]
    # cpu_cooler_row = [items['cpu-cooler'][0] + items['cpu-cooler'][1]]
    # video_card_row = [items['video-card'][0] + items['video-card'][1]]
    # motherboard_row = [items['motherboard'][0] + items['motherboard'][1]]
    # memory_row = [items['memory'][0] + items['memory'][1]]
    # internal_hard_drive_row = [items['internal-hard-drive'][0] + items['internal-hard-drive'][1]]
    # power_supply_row = [items['power-supply'][0] + items['power-supply'][1]]
    # print(cpu_dataset[2])
    # print(cpu_row)

    cpu_prediction = predicts_class(cpu_dataset, cpu_dataset[0], 3)
    case_prediction = predicts_class(case_dataset, case_dataset[0], 3)
    cpu_cooler_prediction = predicts_class(cpu_cooler_dataset, cpu_cooler_dataset[0], 3)
    video_card_prediction = predicts_class(video_card_dataset, video_card_dataset[0], 3)
    motherboard_prediction = predicts_class(motherboard_dataset, motherboard_dataset[0], 3)
    memory_prediction = predicts_class(memory_dataset, memory_dataset[0], 3)
    internal_hard_drive_prediction = predicts_class(internal_hard_drive_dataset, internal_hard_drive_dataset[0], 3)
    power_supply_prediction = predicts_class(power_supply_dataset, power_supply_dataset[0], 3)

    print("Expected cpu: {}, Got: {} ".format(cpu_dataset[0][0], cpu_prediction))
    print("Expected case: {}, Got: {} ".format(case_dataset[0][0], case_prediction))
    print("Expected cpu_cooler: {}, Got: {} ".format(cpu_cooler_dataset[0][0], cpu_cooler_prediction))
    print("Expected video_card: {}, Got: {} ".format(video_card_dataset[0][0], video_card_prediction))
    print("Expected motherboard: {}, Got: {} ".format(motherboard_dataset[0][0], motherboard_prediction))
    print("Expected memory: {}, Got: {} ".format(memory_dataset[0][0], memory_prediction))
    print("Expected internal_hard_drive: {}, Got: {} ".format(internal_hard_drive_dataset[0][0], internal_hard_drive_prediction))
    print("Expected power_supply: {}, Got: {} ".format(power_supply_dataset[0][0], power_supply_prediction))


main()
