from pcpartpicker import API
from math import sqrt
import pandas as pd
import csv
import numpy
# from main import *



def handle_api_data(all_data):

    cpu_dataset = []
    case_dataset = []
    cpu_cooler_dataset = []
    video_card_dataset = []
    motherboard_dataset = []
    memory_dataset = []
    internal_hard_drive_dataset = []
    wireless_network_card_dataset = []
    power_supply_dataset = []
    monitor_dataset = []
    keyboard_dataset = []
    mouse_dataset = []



    for key in all_data:
        for part in all_data[key]:
            dataset = []
            if '0.00' in str(part.price) or part.price == None:
                pass
            else:
                if key == 'cpu':

                    # for Gaming
                    if part.integrated_graphics != None:
                        dataset.append(1)
                    else:
                        dataset.append(0)
                    # time of use and experience would have no impact on the cpu
                    dataset.append(None)
                    dataset.append(None)
                    # add price and component name
                    dataset.append(str(part.price.amount))
                    dataset.append(part.brand + " " + part.model)

                    cpu_dataset.append(dataset)

                elif key == 'case':

                    # time and tpye of use and experience would have no impact on the case, it is personal preference
                    dataset.append(None)
                    dataset.append(None)
                    dataset.append(None)
                    # add price and component name
                    dataset.append(str(part.price.amount))
                    dataset.append(part.brand + " " + part.model)

                    case_dataset.append(dataset)

                elif key == 'cpu-cooler':

                    # gaming or video editing would have no impact on the cpu_cooler
                    dataset.append(None)
                    # time of use
                    if part.decibels != None:
                        if part.decibels.max != None:
                            dataset.append(part.decibels.max)
                        else:
                            dataset.append(part.decibels.default)
                    else:
                        pass
                    # experience would have no impact on the cpu cooler
                    dataset.append(None)
                    # add price and component name
                    dataset.append(str(part.price.amount))
                    dataset.append(part.brand + " " + part.model)

                    cpu_cooler_dataset.append(dataset)

                elif key == 'video-card':

                    # for video is more useful as it stores image data
                    if part.vram.total != None and part.vram.total / 1000000000 > 6:
                        dataset.append(0)
                    else:
                        dataset.append(1)
                    # time of use and experience would have no impact on the video card
                    dataset.append(None)
                    dataset.append(None)
                    # add price and component name
                    dataset.append(str(part.price.amount))
                    dataset.append(part.brand + " " + part.model)

                    video_card_dataset.append(dataset)

                elif key == 'motherboard':

                    # for Gaming
                    if part.max_ram.total != None and part.max_ram.total / 1000000000 > 6:
                        dataset.append(1)
                    else:
                        dataset.append(0)
                    # time of use and experience would have no impact on the motherboard
                    dataset.append(None)
                    dataset.append(None)
                    # add price and component name
                    dataset.append(str(part.price.amount))
                    dataset.append(part.brand + " " + part.model)

                    motherboard_dataset.append(dataset)

                elif key == 'memory':

                    # for Gaming
                    if part.module_size.total != None and part.module_size.total / 1000000000 > 6:
                        dataset.append(1)
                    else:
                        dataset.append(0)
                    # time of use and experience would have no impact on the memory
                    dataset.append(None)
                    dataset.append(None)
                    # add price and component name
                    dataset.append(str(part.price.amount))
                    dataset.append(part.brand + " " + part.model)

                    memory_dataset.append(dataset)

                elif key == 'internal-hard-drive':

                    # for Content Creation and video editing
                    if part.capacity.total != None and part.capacity.total /1000000000000 > 0.5:
                        dataset.append(0)
                    else:
                        dataset.append(1)
                    # time of use and experience would have no impact on the internal_hard_drive
                    dataset.append(None)
                    dataset.append(None)
                    # add price and component name
                    dataset.append(str(part.price.amount))
                    dataset.append(part.brand + " " + part.model)

                    internal_hard_drive_dataset.append(dataset)

                elif key == 'wireless-network-card':

                    # time, mode of use and experience would have no impact on the power_supply
                    dataset.append(None)
                    dataset.append(None)
                    dataset.append(None)
                    # add price and component name
                    dataset.append(str(part.price.amount))
                    dataset.append(part.brand + " " + part.model)

                    wireless_network_card_dataset.append(dataset)


                elif key == 'power-supply':

                    # time, mode of use and experience would have no impact on the power_supply
                    dataset.append(None)
                    dataset.append(None)
                    dataset.append(None)
                    # add price and component name
                    dataset.append(str(part.price.amount))
                    dataset.append(part.brand + " " + part.model)

                    power_supply_dataset.append(dataset)

                elif key == 'monitor':

                    # time, mode of use and experience would have no impact on the monitor
                    dataset.append(None)
                    dataset.append(None)
                    dataset.append(None)
                    # add price and component name
                    dataset.append(str(part.price.amount))
                    dataset.append(part.brand + " " + part.model)

                    monitor_dataset.append(dataset)

                elif key == 'keyboard':

                    # mode of use would have no impact on the keyboard
                    dataset.append(None)
                    # time of use would impact the keyboard as a backlit one would be needed for the night
                    if part.backlight != None:
                        dataset.append(1)
                    else:
                        dataset.append(0)
                    # experience would have no impact on the keyboard
                    dataset.append(None)
                    # add price and component name
                    dataset.append(str(part.price.amount))
                    dataset.append(part.brand + " " + part.model)

                    keyboard_dataset.append(dataset)

                elif key == 'mouse':

                    # for gaming
                    if part.max_dpi != None and part.max_dpi > 400 and part.max_dpi < 1600:
                        dataset.append(1)
                    else:
                        dataset.append(0)
                    # time of use and experience would have no impact on the mouse
                    dataset.append(None)
                    dataset.append(None)
                    # add price and component name
                    dataset.append(str(part.price.amount))
                    dataset.append(part.brand + " " + part.model)

                    mouse_dataset.append(dataset)
                else:
                    pass

    return cpu_dataset, case_dataset, cpu_cooler_dataset, video_card_dataset, motherboard_dataset, memory_dataset, internal_hard_drive_dataset, wireless_network_card_dataset, power_supply_dataset, monitor_dataset, keyboard_dataset, mouse_dataset


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
    for row in neighbors:
        output_vals = [row[-1], row[-2]]
    name_prediction = max(set(output_vals), key=output_vals[0].count)
    price_prediction = max(set(output_vals), key=output_vals[1].count)
    prediction = [name_prediction, price_prediction]

    return prediction


def main(items, purpose, time, exp, all_data):

    cpu_dataset, case_dataset, cpu_cooler_dataset, video_card_dataset, motherboard_dataset, memory_dataset, internal_hard_drive_dataset, wireless_network_card_dataset, power_supply_dataset, monitor_dataset, keyboard_dataset, mouse_dataset = handle_api_data(all_data)

    if purpose == 1:
        purpose = 1
    else:
        purpose = 0

    if time == 'n':
        time = 1
    else:
        time = 0
    cpu_row = [str(items['cpu'][0] + items['cpu'][1]), purpose, None, None]
    case_row = [str(items['case'][0] + items['case'][1]), None, None, None]
    cpu_cooler_row = [str(items['cpu-cooler'][0] + items['cpu-cooler'][1]), None, time, None]
    video_card_row = [str(items['video-card'][0] + items['video-card'][1]), purpose, None, None]
    motherboard_row = [str(items['motherboard'][0] + items['motherboard'][1]), purpose, None, None]
    memory_row = [str(items['memory'][0] + items['memory'][1]), purpose, None, None]
    internal_hard_drive_row = [str(items['internal-hard-drive'][0] + items['internal-hard-drive'][1]), purpose, None, None]
    wireless_network_card_row = [str(items['wireless-network-card'][0] + items['wireless-network-card'][1]), None, None, None]
    power_supply_row = [str(items['power-supply'][0] + items['power-supply'][1]), None, None, None]
    monitor_row = [str(items['monitor'][0] + items['monitor'][1]), None, None, None]
    keyboard_row = [str(items['keyboard'][0] + items['keyboard'][1]), None, time, None]
    mouse_row = [str(items['mouse'][0] + items['mouse'][1]), purpose, None, None]

    cpu_prediction = predicts_class(cpu_dataset, cpu_row, 3)
    case_prediction = predicts_class(case_dataset, case_row, 3)
    cpu_cooler_prediction = predicts_class(cpu_cooler_dataset, cpu_cooler_row, 3)
    video_card_prediction = predicts_class(video_card_dataset, video_card_row, 3)
    motherboard_prediction = predicts_class(motherboard_dataset, motherboard_row, 3)
    memory_prediction = predicts_class(memory_dataset, memory_row, 3)
    internal_hard_drive_prediction = predicts_class(internal_hard_drive_dataset, internal_hard_drive_row, 3)
    wireless_network_card_prediction = predicts_class(wireless_network_card_dataset, wireless_network_card_row, 3)
    power_supply_prediction = predicts_class(power_supply_dataset, power_supply_row, 3)
    monitor_prediction = predicts_class(monitor_dataset, monitor_row, 3)
    keyboard_prediction = predicts_class(keyboard_dataset, keyboard_row, 3)
    mouse_prediction = predicts_class(mouse_dataset, mouse_row, 3)

    recommendation = [cpu_prediction, case_prediction, cpu_cooler_prediction, video_card_prediction, motherboard_prediction, memory_prediction, internal_hard_drive_prediction, wireless_network_card_prediction, power_supply_prediction, monitor_prediction, keyboard_prediction, mouse_prediction]
    return recommendation
