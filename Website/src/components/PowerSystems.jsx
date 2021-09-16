import React, { Component } from 'react';
import '../App.css';

export default class PowerSystems extends Component {
    render() {
        if (this.props.display === 4) {
            return (
                <div className="PowerSystems">
                    <header class="bg-white shadow">
                        <div class="max-w-7xl mx-auto py-6 px-4 sm:px-6 lg:px-8">
                            <h1 class="text-3xl font-bold text-gray-900">Power Systems</h1>
                        </div>
                    </header>
                    <main>
                        <div class="max-w-3xl mx-auto py-6 sm:px-6 lg:px-8">
                            <div class="px-4 py-6 sm:px-0">
                                <h2 class="text-2xl py-4 font-bold text-gray-900">The Power Systems Team</h2>
                                <p class="py-2">
                                    <b>Robert Fleming:</b> An ECE major, class of 2023. Created and designed circuits for the battery systems and 
                                    determined what power supply to use for them.
                                </p>
                                <p class="py-2">
                                    <b>Max Garval:</b> An ECE major, class of 2024. Worked with Arduinos and batteries to power a variety of sensors.
                                </p>
                                <p class="py-2">
                                    Our pod is completely battery operated. There are three main components that require power: the sensor systems, 
                                    braking mechanisms, and the motors.
                                </p>
                                <img class="py-3" src="https://hyperloop.cornell.edu/electrical/img/Max_and_Tim_working.png" alt="Power Systems Team" />
                                <h2 class="text-1xl py-4 font-bold text-gray-900">Sensors</h2>
                                <p>
                                    For the sensor systems, we used four Arduino Mega boards each powered by four AA batteries connected by a 100 ohm 
                                    resistor to the Vin pin on the Arduino board and connected to an array of ground pins which is grounded by the Arduino 
                                    GND pin as displayed in the image below.
                                </p>
                                <img class="py-3" src="https://hyperloop.cornell.edu/electrical/img/Arduino_diagram.png" alt="Arduino Diagram" />

                                <h2 class="text-1xl py-4 font-bold text-gray-900">Braking</h2>
                                <p>
                                    For the braking system, we also used a battery pack of 4 AAs connected directly to the relay 
                                    module which is also connected to both an Arduino board for control and the solenoid itself in 
                                    order to actuate the pneumatic brakes. This can be seen in the diagram below.
                                </p>
                                <img class="py-3 px-48 h-96" src="https://hyperloop.cornell.edu/electrical/img/Relay_circuit.jpg" alt="Relay Circuit" />

                                <h2 class="text-1xl py-4 font-bold text-gray-900">Motors</h2>
                                <p>
                                    In order to power the motors we used 248 Li-Ion batteries for each engine, in modules of 62 cells. 
                                    Two modules are in series with each other which are in parallel with another two modules which are in 
                                    series to meet the current and voltage requirements of the motor. We replicated this setup for each motor. 
                                    This battery pack is connected to the motor controller which is connected to the actual motors. These setups 
                                    are depicted in the diagram below.
                                </p>

                            </div>
                        </div>
                    </main>
                </div>
            )
        } else {
            return <div className="PowerSystems"></div>
        }

    }
}
