
from pcpartpicker import API
import cgi
import ml
from art import *

# api: https://github.com/JonathanVusich/pcpartpicker/
form = cgi.FieldStorage()
api = API("uk")
all_data = api.retrieve("cpu", "case", "cpu-cooler", "video-card", "motherboard", "memory", "internal-hard-drive", "power-supply")
Art=text2art("PC PART PICKER",font='block',chr_ignore=True)
b = art = text2art("Gaming?")
c = art = text2art("Editing?")
print()

def User():
    count = 0
    print("(っ◕‿◕)っ Welcome! I am Bob, assisting you today! (｡◕‿◕｡) ")
    print(" \n(っ◕‿◕)っ We will recommend you the best PC parts to pick from! (ღ˘◡˘ღ)  ")
    print("\n", b)
    print(c)
    while count == 0:
        try:
            purpose = int(input("(っ◕‿◕)っ Will you be using your system for (1 or 2):  \n 1. Gaming (ღ˘◡˘ღ) \n 2. Content Creation/Video Editing ✿◕ ‿ ◕✿ \n"))
            if purpose == 1 or purpose == 2:
                try:
                    budget = int(input("(っ◕‿◕)っ Please enter your budget (£) ❀◕ ‿ ◕❀  : "))
                    division(budget, purpose)
                    count+=1
                    exit = input("Press ENTER to exit the program")
                    print()
                except ValueError:
                    print("Please enter only numbers")
                    User()
        except ValueError:
            print("Please enter only numbers")
            User()
    
# Must update division - 'time' and 'exp' are not taken into consideration atm must update but not sure expression<---
          #  time = input("Do you mainly play at night (n) r during the day (d)")
         #   exp = input("Are you buying PC parts for the first time (y/n)")

    #ml.main(items, budget, purpose)


def division(budget, purpose):
    relparts = []
    current_cost = 0
    if purpose == 1:
        mincpu, maxcpu = 0.2 * budget, 0.25 * budget
        mingpu, maxgpu, = 0.25 * budget, 0.3 * budget
        mincase, maxcase = 0.03 * budget, 0.06 * budget
        mincooler, maxcooler = 0.025 * budget, 0.035 * budget
        minmobo, maxmobo = 0.09 * budget, 0.15 * budget
        minmem, maxmem = 0.06 * budget, 0.1 * budget
        minhdd, maxhdd = 0.04 * budget, 0.07 * budget
        minpsu, maxpsu = 0.04 * budget, 0.08 * budget
    else:
        mincpu, maxcpu = 0.25 * budget, 0.30 * budget,
        mingpu, maxgpu, = 0.10 * budget, 0.14 * budget,
        mincase, maxcase = 0.03 * budget, 0.06 * budget
        mincooler, maxcooler = 0.025 * budget, 0.035 * budget
        minmobo, maxmobo = 0.09 * budget, 0.1 * budget
        minmem, maxmem = 0.1 * budget, 0.12 * budget
        minhdd, maxhdd = 0.1 * budget, 0.15 * budget
        minpsu, maxpsu = 0.04 * budget, 0.06 * budget

    items = {
        "cpu": [mincpu, maxcpu],
        "case": [mincase, maxcase],
        "cpu-cooler": [mincooler, maxcooler],
        "video-card": [mingpu, maxgpu],
        "motherboard": [minmobo, maxmobo],
        "memory": [minmem, maxmem],
        "internal-hard-drive": [minhdd, maxhdd],
        "power-supply": [minpsu, maxpsu]}

    for key in all_data:
        added = 0
        counter = 0
        index = list(items).index(key)
        relparts.append([])
        for i in all_data[key]:
            # use ".amount"

            if items[key][0] < i.price.amount < items[key][1] and counter < 6:
                # print(i)
                relparts[index].append(i)
                added += 1
                counter += 1

    # print(relparts[0])
    print_parts(relparts, items, budget, purpose)

def print_parts(relparts, items, budget, purpose):
    
    if len(relparts) != 0:
        print( "(ღ˘◡˘ღ) We recommend the following parts:")

        for item in relparts:
            index = relparts.index(item)
            print("\n")
            print(list(items)[index].upper())
            print("==================================")
            if len(item) == 0:
                print("We don't have that part right now")
            else:
                for i in item:
                    # print(i)
                    print(i.brand, i.model, "|" + " Price: ", i.price)
    return items
    ml.main(items, budget, purpose)

User()
