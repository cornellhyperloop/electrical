"""
A module that contains the FSM class.
"""

import time


class FSM:

    def __init__(self):

        self.currState = 0
        self.nextState = 1
        self.allStates = [1, 2, 3, 4, 5]

        self.thermistor1Value = 0
        self.thermistor2Value = 0
    

    def updateThermistorData(self):

        # Ultimately, this function should load the new thermistor readings
        self.thermistor1Value = 10
        self.thermistor2Value = 20
    

    def changeState(self, newState):

        self.currState = newState
    

    def stateTransition(self):

        self.updateThermistorData()

        # Replace with an actual state transition
        # Currently transitions from state 0 to state 1 unconditionally
        if self.currState == 0: 
            self.nextState = 1
        
        elif self.currState:
            self.nextState = 2

        self.currState = self.nextState
    

    def run(self):

        while self.currState != 5: # example: keep running until state 5 is reached

            time.sleep(1)
            print(f'Thermistor 1 Value: {self.thermistor1Value}, Thermistor 2 Value: {self.thermistor2Value} ')
            self.stateTransition()


if __name__ == '__main__':
    fsm = FSM()
    fsm.run()
