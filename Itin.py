import datetime

class Event:

    def __init__(self, time, loc, evType = 0):
        self.time = time
        self.loc = loc
        self.evType = evType

    def setType(self, evType):
        self.evType = evType

    def getType(self):
        return self.evType

    def __le__(self, other):
        if isinstance(other, Event):
            return self.time <= other.time
        return self.time <= other

    def __lt__(self, other):
        if isinstance(other, Event):
            return self.time < other.time
        return self.time < other

    def __ge__(self, other):
        if isinstance(other, Event):
            return self.time >= other.time
        return self.time >= other

    def __gt__(self, other):
        if isinstance(other, Event):
            return self.time > other.time
        return self.time > other

    def __sub__(self, other):
        if isinstance(other, Event):
            return self.time - other.time
        return self.time - other

    def __add__(self, other):
        if isinstance(other, Event):
            return self.time + other.time
        return self.time + other

    def __str__(self):
        return "Location: {} at time {}. (type {})".format(self.loc, self.time, self.evType)

class Itin:

    def __init__(self, id):
        self.id = id
        self.events = []

    def __eq__(self, id):
        return self.id == id

    def addEvent(self, time, loc, evType=0):
        ev = Event(time, loc, evType)
        self.events.append(ev)
        self.events.sort()

    def __str__(self):
        ans = "Passenger {} with itinerary:\n".format(self.id)
        for ev in self.events:
            ans += str(ev)+"\n"
        return ans

    def getEvent(self, time):
        if len(self.events) == 0:
            return None
        if self.events[0] > time:
            return None
        for i in range(len(self.events)-1):
            if self.events[i] <= time and self.events[i+1] >= time:
                return self.events[i]
        return self.events[-1]

    def relabel(self):
        if len(self.events) >= 1:
            for i in range(len(self.events)-1):
                if self.events[i].loc == self.events[i+1].loc:
                    self.events[i].setType(2)
            self.events[-1].setType(4)
            
        

def countPax(time, airports, itin):
    CAT = 6
    counts = {}
    for airport in airports:
        counts[airport] = [0]*CAT
    for id in itin:
        ev = itin[id].getEvent(time)
        if ev is not None:
            loc = ev.loc
            if loc in counts:
                delta = time-ev.time
                if delta < datetime.timedelta(hours=2):
                    if ev.evType == 0:
                        counts[loc][0] += 1
                    elif ev.evType == 2:
                        counts[loc][3] += 1
                elif delta < datetime.timedelta(hours=4):
                    if ev.evType == 0:
                        counts[loc][1] += 1
                    elif ev.evType == 2:
                        counts[loc][4] += 1
                else:
                    if ev.evType == 0:
                        counts[loc][2] += 1
                    elif ev.evType == 2:
                        counts[loc][5] += 1
    return counts
                    
            
    