import random

#Dictionary for determining which PIDs are currently in use.
PIDList = {}
PIDList[1] = False
#This is the student/process class. The class has a few characteristics: Starting time (Stime),
#Process ID (PID), the amount of time the process took until completion (Ptime), and the ending time for
# the process (Etime)
class Student:
    #__init__ is called when the object is created. When it is created, a process gets a start time and ID.
    def __init__(self, Stime):
        self.Stime = Stime
        self.getPID()
        self.InClass = False
        self.InQueue = False
        self.TestSpeed = random.randint(1, 101)
        
    #__del__ is called when the object is deleted. When it is deleted, the ID returns
    # to the pool and the ending time is assigned, as well as the process time being calculated.
    def __del__(self, ETime):
        self.EndTime = ETime
        PIDList[self.PID] = False
        print(getPTime)

    #This function gets the first available PID from the availability pool. If none are available,
    #creates a new one at the lowest possible ID number
    def getPID(self):
        i = 1;
        foundPID = False
        while(i <= len(PIDList)):
            if PIDList[i] == False:
                self.PID = i
                PIDList[i] = True
                foundPID = True
                break
            else:
                i = i + 1
        if not foundPID:
            self.PID = i
            PIDList[i] = True

    #This function calculates the turnaround time.
    def getPTime(self):
        self.PTime = self.EndTime - self.Stime
        return self.PTime

    #Places a student object in a queue.
    def assignQueue(self):

    #Takes a student out of the queue it is in and puts it in a classroom.
    def assignClassroom(self):

E = 0
#Testing function/Simulation.
while(E < 100):
    x = Student(E)
    print("Student time = " + str(x.Stime) + " ID = " + str(x.PID))
    E = E + 1
    del x(E)
