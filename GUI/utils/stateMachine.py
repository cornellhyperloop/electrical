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

        self.currState = 0
        self.nextState = 1
        self.allStates = [1, 2, 3, 4, 5]

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
    

    def changeState(self, newState):

        self.currState = newState
    

    def stateTransition(self):

        self.updateThermistorData()

        # Replace with an actual state transition
        # Currently transitions from state 0 to state 1 unconditionally
        if self.currState == 0:
            self.nextState = 1
        
        elif self.currState == 1:
            pass
        
        elif self.currState == 2:
            # Code for activating cooling mechanism
            if (self.thermistor1 < self.overheatingTemp):
                self.nextState = 4
        
        elif self.currState == 3:
            self.nextState = 4
        
        elif self.currState == 4:
            # Code for starting the motors
            pass
        
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
            pass
        
        elif self.currState == 9:
            pass
        
        elif self.currState == 10:
            pass

        self.currState = self.nextState
    

    def run(self):

        while self.currState != 5: # example: keep running until state 5 is reached

            time.sleep(1)
            print(f'Thermistor 1 Value: {self.thermistor1}, Thermistor 2 Value: {self.thermistor2} ')
            self.stateTransition()


if __name__ == '__main__':
    fsm = FSM()
    fsm.run()
