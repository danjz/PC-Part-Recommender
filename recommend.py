from pcpartpicker import API
#api: https://github.com/JonathanVusich/pcpartpicker/

api = API("uk")
all_data = api.retrieve("cpu", "case", "cpu-cooler", "video-card", "motherboard", "memory", "internal-hard-drive", "power-supply")
def User():
    purpose = int(input("Will you be using your system for (1 or 2): \n 1. Gaming \n 2. Content Creation/Video Editing:\n"))
    budget = int(input("Please enter your budget (£): "))
    items = division(budget, purpose)
    return items, budget, purpose


def division(budget, purpose):
    relparts = []
    current_cost = 0
    if purpose == 1:
        mincpu,maxcpu = 0.2*budget,0.25*budget
        mingpu,maxgpu, = 0.25*budget, 0.3*budget
        mincase,maxcase = 0.03*budget, 0.06*budget
        mincooler,maxcooler = 0.025*budget, 0.035*budget
        minmobo,maxmobo = 0.09*budget, 0.15*budget
        minmem,maxmem = 0.06*budget, 0.1*budget
        minhdd,maxhdd = 0.04*budget, 0.07*budget
        minpsu,maxpsu = 0.04*budget, 0.08*budget
    else:
        mincpu, maxcpu =  0.25*budget, 0.30*budget,
        mingpu, maxgpu, = 0.10*budget, 0.14*budget,
        mincase,maxcase = 0.03*budget, 0.06*budget
        mincooler,maxcooler = 0.025*budget, 0.035*budget
        minmobo,maxmobo = 0.09*budget, 0.1*budget
        minmem,maxmem = 0.1*budget, 0.12*budget
        minhdd,maxhdd = 0.1*budget, 0.15*budget
        minpsu,maxpsu = 0.04*budget, 0.06*budget


    items = {
    "cpu":[mincpu, maxcpu],
    "case":[mincase,maxcase],
    "cpu-cooler":[mincooler,maxcooler],
    "video-card":[mingpu,maxgpu],
    "motherboard":[minmobo,maxmobo],
    "memory":[minmem,maxmem],
    "internal-hard-drive":[minhdd,maxhdd],
    "power-supply":[minpsu,maxpsu]}

    for key in all_data:
        added = 0
        counter = 0
        index  = list(items).index(key)
        relparts.append([])
        for i in all_data[key]:
            #use ".amount"

            if items[key][0] < i.price.amount < items[key][1] and counter <6:
                    #print(i)
                    relparts[index].append(i)
                    added+=1
                    counter+=1

    #print(relparts[0])
    if len(relparts)!=0:
        print("We recommend the following parts:")
        for item in relparts:
            index = relparts.index(item)
            print("\n")
            print(list(items)[index].upper())
            print("==================================")
            if len(item)==0:
                print("We dont have that part right now")
            else:
                for i in item:
                    #print(i)
                    print(i.brand, i.model,"|"+" Price: ",i.price)

    return items
