import random

#Dictionary for determining which PIDs are currently in use.
PIDList = {}
PIDList[1] = False
#This is the student/process class. The class has a few characteristics: Starting time (Stime),
#Process ID (PID), the amount of time the process took until completion (Ptime), and the ending time for
# the process (Etime)
class Student:
    #__init__ is called when the object is created. When it is created, a process gets a start time and ID.
    def __init__(self, Stime, EvTime):
        self.Stime = Stime
        self.getPID()
        self.InClass = False
        self.InQueue = False
        self.WaitTime = EvTime/2
        self.FrontTime = 0
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
    def assignQueue(self, T, QList):
        self.QStime = T
        minlength = 100
        optQueue = -1
        for i in range(0, len(QList)):
            if len(QList[i]) =< minlength:
                minlength = len(QList[i])
                optQueue = i
        self.Q = QList[optQueue]
        QList[optQueue].append[self]
                

    def InFront(self, SQ):
        if SQ[0] == self:
            #self.FrontTime = 0
            return True
        return False

    def QueueTime(self, T):
        self.QueueTime = T - self.QStime
        return self.QueueTime

    def ReduceWTime(self, T):
        self.WaitTime = self.WaitTime - T

    #Takes a student out of the queue it is in and puts it in a classroom.
    def assignClassroom(self, Croom)

#There are all of the "lines" that students wait in before taking an exam.
#These include the entrance/exit queues, which are RR, and the main waiting lines
#which have varying scheduling algorithms
class StudentQueue:

    #Every queue has an algorithm and a list of students in it. All queues start empty.
    def __init__(self, Schedule):
        self.alg = Schedule
        self.studentList = []

    #Returns the number of students in the line.
    def getSize(self):
        return len(studentList)

    #Adds a student to the line, normally at the back.
    #Depending on the scheduling algorithm, the position of the student may be moved.
    def append(self, std):
        self.studentList.append(std)

    #Dependent on the scheduling algorithm: removes a process from the queue.
    def remove(self):
        if self.alg == "FCFS":
            return (self.studentList.pop(0))
        elif self.alg == "SPN":
            S = -1
            t = 0
            for i in range(0, len(studentList)):
                if self.studentList[i].WaitTime <= S or S == -1:
                    S = self.studentList[i].WaitTime
                    t = i
            return self.studentList.pop(t)
        #May not work depending on how returning works.
        elif self.alg == "RR":
            RRreturn = []
            #May not work depending on how list size is calculated
            for i in range(0, len(studentList)):
                self.studentList[i].ReduceWTime(TimeQuantum)
                if self.studentList[i] <= 0:
                    RRreturn.append(self.studentList.pop(i))
                    i = i - 1
            return RRreturn    #May not return based on size of RRreturn
                    

    def setTime(self, T):
        self.TimeQuantum = T
        

#Simple monitor that contains a process and can be equivalent to a critical section as well
#This is where a process enters and exits.
class Classroom:

    #All classrooms, when created, have no student in them.
    def __init__(self):
        self.isFull = False

    #Called whenever a student enters a given classroom.
    def fill(self):
        self.isFull = True

    #called whenever a student leaves a given classroom.
    def empty(self):
        self.isFull = False

E = 0
#Testing function/Simulation.
while(E < 100):
    x = Student(E)
    print("Student time = " + str(x.Stime) + " ID = " + str(x.PID))
    E = E + 1
    del x(E)
