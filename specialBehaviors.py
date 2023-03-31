from Queue import Queue, arrival, departure, emptyQueue, getSize, inFront, moveToRear, sweepQueue, sweepMovingToRear

def sweepToGetMoney (queue):
    auxQueue = Queue()
    total = 0
    while not emptyQueue(queue):
        data = departure(queue)
        if data == 'Car':
            total += 47
        elif data == 'Van':
            total += 59
        elif data == 'Truck':
            total += 71
        elif data == 'Bus':
            total += 64
        arrival(auxQueue, data)
        
    while not emptyQueue(auxQueue):
        data = departure(auxQueue)
        arrival(queue, data)
        
    return total

def sweepTypeOfCar(queue):
    auxQueue = Queue()
    cars = 0
    vans = 0
    trucks = 0
    buses = 0
    
    while not emptyQueue(queue):
        data = departure(queue)
        if data == "Car":
            cars += 1
        elif data == "Van":
            vans += 1
        elif data == "Truck":
            trucks += 1
        elif data == "Bus":
            buses += 1
        arrival(auxQueue, data)
        
    while not emptyQueue(auxQueue):
        data = departure(auxQueue)
        arrival(queue, data)
        
    print(f"Cars: {cars}\nVans: {vans}\nTrucks: {trucks}\nBuses: {buses}")

def getCabinWithMostEarnings (firstToll, secondToll, thirdToll):
    firstCabinEarnings = {"Cabin": "First Toll Cabin", "Earnings": sweepToGetMoney(firstToll)}
    secondCabinEarnings = {"Cabin": "Second Toll Cabin", "Earnings": sweepToGetMoney(secondToll)}
    thirdCabinEarnings = {"Cabin": "Third Toll Cabin", "Earnings": sweepToGetMoney(thirdToll)}
    
    if (firstCabinEarnings["Earnings"] >= secondCabinEarnings["Earnings"] and firstCabinEarnings["Earnings"] >= thirdCabinEarnings["Earnings"]):
        maxEarnings = firstCabinEarnings
    elif (secondCabinEarnings["Earnings"] >= firstCabinEarnings["Earnings"] and secondCabinEarnings["Earnings"] >= thirdCabinEarnings["Earnings"]):
        maxEarnings = secondCabinEarnings
    else:
        maxEarnings = thirdCabinEarnings
        
    return maxEarnings
        