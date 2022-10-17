"""
A module that contains the FSM class.
"""

import time

class FSM:

    # UPDATE CONSTANTS
    maxPressure = 0
    minSideDistance = 0
    maxEndDistance = 0
    maxAcceleration = 0
    overheatingTemp = 35
    extremeOverheatingTemp = 55

    def __init__(self):
        """
        Possible States:
            State 0: Pod On
            State 1: Verification
            State 2: Overheating
            State 3: Pre-Acceleration
            State 4: Acceleration
            State 5: Cruise
            State 6: Deceleration
            State 7: Crawl
            State 8: Stop
            State 9: Emergency
            State 10: Pod Off
        """

        # self.allStates = {
        #     0: 'Pod On',
        #     1: 'Verification',
        #     2: 'Overheating',
        #     3: 'Pre-Acceleration',
        #     4: 'Acceleration',
        #     5: 'Cruise',
        #     6: 'Deceleration',
        #     7: 'Crawl',
        #     8: 'Stop',
        #     9: 'Emergency',
        #     10: 'Pod Off'
        # }

        ## temporary 
        self.allStates = {
            0: 'Stop',
            1: 'Crawl',
            2: 'Deceleration',
            3: 'Cruise',
            4: 'Emergency',
            5: 'Verification',
            6: 'Pre-Acceleration',
            7: 'Acceleration',
            8: 'Overheating',
            9: 'Extreme Overheating'
        }

        self.currState = self.allStates[0]
        self.nextState = self.allStates[1]

        self.thermistor1 = 0
        self.thermistor2 = 0

        self.pressureSensor1 = 0

        self.shortDistance1 = 0

        self.longDistance1 = 0

        self.acceleration = 0
        self.avgAcceleration = 0


    def updateThermistorData(self):

        # Ultimately, this function should load the new thermistor readings
        self.thermistor1 = 10
        self.thermistor2 = 20


    def setState(self, newState):

        self.currState = newState

    def getState(self):

        return self.currState

    def stateTransition(self):

        self.updateThermistorData()

        # Replace with an actual state transition
        # Currently transitions from state 0 to state 1 unconditionally
        if self.currState == 0:
            if self.thermistor1<self.overheatingTemp and self.thermistor2<overheatingTemp and self.pressureSensor1<self.maxPressure and self.longDistance1< self.maxEndDistance and self.shortDistance1>self.minSideDistance and self.avgAcceleration<self.maxAcceleration:
                self.nextState = 1

        elif self.currState == 1:
            if self.thermistor1>=self.overheatingTemp and self.thermistor2>=overheatingTemp:
                self.nextState=2

        elif self.currState == 2:
            # Code for activating cooling mechanism
            if (self.thermistor1 < self.overheatingTemp):
                self.nextState = 4

        elif self.currState == 3:
            if self.longDistance1< self.maxEndDistance and self.thermistor1<self.overheatingTemp:
                self.nextState = 4

        elif self.currState == 4:
            # Code for starting the motors
            if self.avgAcceleration>=self.maxAcceleration:
                self.nextState=5

        elif self.currState == 5:
            if (self.thermistor1 >= self.extremeOverheatingTemp or self.pressureSensor1 >= self.maxPressure):
                self.nextState = 9
            elif (self.thermistor1 > self.overheatingTemp):
                self.nextState = 2
            elif (self.shortDistance1 < self.minSideDistance):
                # Code for adjusting the orientation of the pod
                pass
            elif (self.longDistance1 >= self.maxEndDistance):
                self.nextState = 7
            elif (self.acceleration >= self.maxAcceleration):
                self.nextState = 6

        elif self.currState == 6:
            if (self.acceleration < self.avgAcceleration):
                self.nextState = 5

        elif self.currState == 7:
            if (self.acceleration == 0):
                self.nextState = 8

        elif self.currState == 8:
            if self.thermistor1>=self.overheatingTemp or self.thermistor2>=overheatingTemp or self.pressureSensor1>=self.maxPressure or self.longDistance1>=self.maxEndDistance or self.shortDistance1<=self.minSideDistance or self.avgAcceleration>self.maxAcceleration:
                self.nextState=10

        elif self.currState == 9:
            if self.thermistor1>=self.overheatingTemp or self.thermistor2>=overheatingTemp or self.pressureSensor1>=self.maxPressure or self.longDistance1>=self.maxEndDistance or self.shortDistance1<=self.minSideDistance or self.avgAcceleration>self.maxAcceleration:
                self.nextState=10

        elif self.currState == 10:
            if self.thermistor1<self.overheatingTemp and self.thermistor2<overheatingTemp and self.pressureSensor1<self.maxPressure and self.longDistance1< self.maxEndDistance and self.shortDistance1>self.minSideDistance and self.avgAcceleration<self.maxAcceleration:
                self.nextState=0

        self.currState = self.nextState
        print(str(self.nextState))


    def run(self):

        while self.currState != 5: # example: keep running until state 5 is reached

            time.sleep(1)
            print(f'Thermistor 1 Value: {self.thermistor1}, Thermistor 2 Value: {self.thermistor2} ')
            self.stateTransition()

    def runOneIteration(self):

        self.stateTransition()

if __name__ == '__main__':
    fsm = FSM()
    fsm.run()
