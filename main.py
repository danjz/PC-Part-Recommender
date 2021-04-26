from pcpartpicker import API
from controlledvocabulary import controlledvocabulary
import cgi
from art import *

# api: https://github.com/JonathanVusich/pcpartpicker/
form = cgi.FieldStorage()
api = API("uk")
all_data = api.retrieve("cpu", "case", "cpu-cooler", "video-card", "motherboard",  "memory", "internal-hard-drive", "wireless-network-card",
                        "power-supply", "monitor","keyboard","mouse")
components = api.retrieve("cpu", "cpu-cooler", "video-card", "motherboard", "memory", "internal-hard-drive", "wireless-network-card",
                        "power-supply")
peripheries = api.retrieve("case","monitor","keyboard","mouse")
Art = text2art("PC PART PICKER", font='block', chr_ignore=True)
b =  text2art("Gaming?")
c = text2art("Editing?")
art_8 = art("cute face 9")  # left hand
art_7=art("gimme") # right hand
art_5=art("cute face5")
art_2=art("cute face") # oh rly
art_6=art("french kiss")

def User():
    count = 0
    print(art_7, " Welcome! I am Bob, assisting you today!  ", art_8)
    print(" \n",art_5, " We will recommend you the best PC parts to pick from! ", art_8)
    print("\n", b)
    print(c)
    while count == 0:
        try:
            print(art_5)
            purpose = int(
                input("Will you be using your system for (1 or 2): \n 1. Gaming \n 2. Content Creation/Video Editing:\n"))
            if purpose in {1, 2}:
                try:
                    print()
                    print(art_7)
                    budget = int(input("Please enter your budget (£): "))
        # Must update division - 'time' and 'exp' are not taken into consideration atm must update but not sure expression<---
                    time = input("Do you mainly play at night (n) r during the day (d)")
                    exp = input("Are you buying PC parts for the first time (y/n)")
                    filters = input("Would you like to filter your search? (y/n)") #start of controlled vocab integration
                    if (filters == 'y'):
                        filter(budget, purpose)
                    else:
                        division(budget, purpose,3)          
                    count = count + 1
                except ValueError:
                    print("Please enter only numbers")
                    print(art_2)
                    User()
        except ValueError:
                    print("Please enter only numbers")
                    print(art_2)
                    User()



#controlled vocabulary functionality
def filter(budget, purpose):
    res = []
    print("The possible filters are (type number if you want that filter): ")
    print("1. PC Components")
    print("2. PC Peripheries")
    print("Type n if you don't want filters.")
    fin = input()
    if(fin == 'n'):
        division(budget,purpose,3)
    else:
        fin = fin.strip()
        for i in fin:
            res.append(int(i))
    if(len(res) == 0):
        return
    elif(len(res) == 1):
        if(res[0] == 1):
            division(budget, purpose, 1)
            #components filtering call
        elif(res[0]==2):
            division(budget, purpose, 2)
        elif(res[0]==3):
            division(budget, purpose, 3)
            #peripheries filtering call
    elif(len(res) == 2):
        division(budget,purpose,3)
    
    


def division(budget, purpose, filter):
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
        minpsu, maxpsu = 0.02 * budget, 0.04 * budget
        minwic, maxwic = 0.05 * budget, 0.08 * budget
        minmon, maxmon = 0.2 * budget, 0.25 * budget
        minkey, maxkey = 0.06 * budget, 0.1 * budget
        minmou, maxmou = 0.06 * budget, 0.1 * budget
    else:
        mincpu, maxcpu = 0.25 * budget, 0.30 * budget,
        mingpu, maxgpu, = 0.10 * budget, 0.14 * budget,
        mincase, maxcase = 0.03 * budget, 0.06 * budget
        mincooler, maxcooler = 0.025 * budget, 0.035 * budget
        minmobo, maxmobo = 0.09 * budget, 0.1 * budget
        minmem, maxmem = 0.1 * budget, 0.12 * budget
        minhdd, maxhdd = 0.1 * budget, 0.15 * budget
        minpsu, maxpsu = 0.04 * budget, 0.06 * budget
        minwic, maxwic = 0.05 * budget, 0.08 * budget
        minmon, maxmon = 0.05 * budget, 0.1 * budget
        minkey, maxkey = 0.01 * budget, 0.02 * budget
        minmou, maxmou = 0.01 * budget, 0.5 * budget

    all_items = {
        controlledvocabulary["PC Components"][0]: [mincpu, maxcpu],
        controlledvocabulary["PC Peripheries"][0]: [mincase, maxcase],
        controlledvocabulary["PC Components"][5]: [mincooler, maxcooler],
        controlledvocabulary["PC Components"][2]: [mingpu, maxgpu],
        controlledvocabulary["PC Components"][4]: [minmobo, maxmobo],
        controlledvocabulary["PC Components"][3]: [minmem, maxmem],
        controlledvocabulary["PC Components"][1]: [minhdd, maxhdd],
        controlledvocabulary["PC Components"][6]: [minwic, maxwic],
        controlledvocabulary["PC Components"][7]: [minpsu, maxpsu],
        controlledvocabulary["PC Peripheries"][1]: [minmon, maxmon],
        controlledvocabulary["PC Peripheries"][2]: [minkey, maxkey],
        controlledvocabulary["PC Peripheries"][3]: [minmou, maxmou]
        }
    comp_items = {
        controlledvocabulary["PC Components"][0]: [mincpu, maxcpu],
        controlledvocabulary["PC Components"][5]: [mincooler, maxcooler],
        controlledvocabulary["PC Components"][2]: [mingpu, maxgpu],
        controlledvocabulary["PC Components"][4]: [minmobo, maxmobo],
        controlledvocabulary["PC Components"][3]: [minmem, maxmem],
        controlledvocabulary["PC Components"][1]: [minhdd, maxhdd],
        controlledvocabulary["PC Components"][6]: [minwic, maxwic],
        controlledvocabulary["PC Components"][7]: [minpsu, maxpsu],
    }
    per_items = {
        controlledvocabulary["PC Peripheries"][0]: [mincase, maxcase],
        controlledvocabulary["PC Peripheries"][1]: [minmon, maxmon],
        controlledvocabulary["PC Peripheries"][2]: [minkey, maxkey],
        controlledvocabulary["PC Peripheries"][3]: [minmou, maxmou]
    }
    if(filter == 3):
        filterloader(all_data, all_items, relparts)
    elif(filter == 1):
        #load components only results
        filterloader(components,comp_items, relparts)
    elif(filter == 2):
        filterloader(peripheries,per_items, relparts)
                    
def print_parts(relparts, items):
    if len(relparts) != 0:
        print("(ღ˘◡˘ღ) We recommend the following parts:")

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


def filterloader(data, items, relparts):
    for key in data:
        added = 0
        counter = 0
        index = list(items).index(key)
        relparts.append([])
        # print(index)
        for i in data[key]:
            # use ".amount"
            # print(items[key][0])
            # print(i.price.amount)
            # print(items[key][1])
            try:    
                if items[key][0] < i.price.amount < items[key][1] and counter < 6:
                    #print(i)
                    relparts[index].append(i)
                    added += 1
                    counter += 1
            except IndexError:
                print("surely not")
                continue
    print_parts(relparts, items) 
User()
