import React, { Component } from 'react';
import '../App.css';

export default class SensorsSP21 extends Component {
    constructor(props) {
        super(props);
        this.state = {
            pageData: "test"
        }
    }

    componentDidMount() {
        fetch("./data/SensorsSP21.json").then(
            (result) => result.json()).then(
                (data) => this.setState({ pageData: data })
            )
    }

    render() {
        if (this.props.display === 7) {
            let pageData = this.state.pageData;
            return (
                <div className="SensorsSP21">
                    <header class="bg-white shadow">
                        <div class="max-w-7xl mx-auto py-6 px-4 sm:px-6 lg:px-8">
                            <h1 class="text-3xl font-bold text-gray-900">{pageData.header}</h1>
                        </div>
                    </header>
                    <main>
                        <div class="max-w-3xl mx-auto py-6 sm:px-6 lg:px-8">
                            <div class="px-4 py-6 sm:px-0">
                                <h2 class="text-2xl py-4 font-bold text-gray-900">About us</h2>
                                <p class="py-2">
                                    {pageData.AboutUs}
                                </p>
                                <h2 class="text-2xl py-4 font-bold text-gray-900">What we accomoplished this semester</h2>
                                <p class="py-2">
                                    {pageData.Accomplishments}
                                </p>
                                <h2 class="text-2xl py-4 font-bold text-gray-900">Demos and Photos from the Semester</h2>
                                <div class="col-lg-8 col-md-10 mx-auto">
          <li> Sensor circuits: </li>
          <ul>
            <li>Multiple photoresistor and inductive proximity sensor circuit:</li>
                    <img src="img/photoresistors.jpg" alt="???" />
            <li>Long distance rangefinder circuit:</li>
                    <img src="img/rangefinder.jpg" alt="???"/>
            <li>Transmitter-receiver circuit:</li>
                    <img src="img/transmitter.jpg" alt="???"/>
            <li>Vibration sensor circuit:</li>
                    <img src="img/vibration.jpg" alt="???"/>
        </ul>
        <li>Sensor Demos:</li>
            <ul>
              <li>Ultrasonic sensor demo: </li>
              <video width="50%" height="50%" controls>
        <source src="img/US Video Demo.mp4" />
      </video>
           <li> Vibration sensor demo: </li>
              <video width="50%" height="50%" controls>
										<source src="img/VS Video Demo.mp4" />
							</video>
        </ul>
      </div>
      <div className="container">
        <div className="row">
          <div className="col-lg-8 mx-auto">
            <h2>Wire the sensors to the Odroid above and below the chassis</h2>
          </div>
          <div className="col-lg-8 col-md-10 mx-auto">
            <li> Sensor layout drawings:</li>
            <img src="img/sensor side view.jpg" style={{width: '435px', height: '290px'}} alt="???"/>
            <img src="img/sensor top view.jpg" style={{width: '435px', height: '290px'}} alt="???"/>
          </div>
        </div>
      </div>
      <div class="container">
    <div class="row">
    <div class="col-lg-8 mx-auto">
        <a name="section2">
        <h2 class="text-2xl py-4 font-bold text-gray-900">Test the new sensors with Arduinos:</h2>
    </a></div><a name="section2">
      <div class="col-lg-8 col-md-10 mx-auto">
        <p> We worked with the following sensors: </p>
        <ul>
        <h1 class="text-1xl py-4 font-bold text-gray-900">Thermistors</h1>
            <ul>
            <h1 class="text-1l py-4 font-bold text-gray-900">What is it: </h1>
                <ul>
                  <li>10kohm NTC thermistors </li>
			<img src="img/thermistor.jpg" alt="???"/>
			<img src="img/thermistor_arduino.png" alt="???"/>
                </ul>
                <h1 class="text-1l py-4 font-bold text-gray-900">Why are we using it: </h1>
                  <ul>
                      <li>Our pod design will use a large number of thermistors.</li>
                      <li>At least one being placed inside each battery pack to monitor the temperature of each pack and ensure that the batteries do not overheat.</li>
                      <li>These thermistors monitor temperature for both safety and telemetry purposes. </li>
                      <li>Each thermistor is connected to the front Arduino Mega board, and read in using the analogRead() function. </li>
                      <li>Calculations are then performed to convert the temperature reading into a usable value to be interpreted by software and emergency braking flag conditions. </li>
                  </ul>
            </ul>
            <h1 class="text-1xl py-4 font-bold text-gray-900">Retroreflective Sensor</h1>
            <ul>
            <h1 class="text-1l py-4 font-bold text-gray-900">What is it: </h1>
                  <ul>
                  <li>Marshall Wolf SA1E-PN2 sensors </li>
			 <img src="img/retroreflective.jpg" alt="???"/>
			<img src="img/retroreflective_arduino.jpg" alt="???"/>
        </ul>
        <h1 class="text-1l py-4 font-bold text-gray-900">Why are we using it: </h1>
                    <ul>
                     <li> The pod will use two retroreflective sensors to collect data about the pod’s position.  </li>
                     <li> We will connect them to the Arduino and used them to perform safety checks.  </li>
                     <li> These sensors will be used to determine the striped track patterns along the tube. </li>
                     <li> This will help verify that the pod was moving in the correct direction and with the correct orientation,
                       as we ensured that the pod was continuously detecting more patterns. </li>
                    </ul>

              
            </ul>
            <h1 class="text-1xl py-4 font-bold text-gray-900">IMU</h1>
            <ul>
            <h1 class="text-1l py-4 font-bold text-gray-900">What is it: </h1>
                <ul>
                  <li>Vectornav’s VN-100 Rugged Intertial Measurement Unit (IMU)</li>
			<img src="img/IMU.png" alt="???"/>
			
                </ul>
                <h1 class="text-1l py-4 font-bold text-gray-900">Why are we using it: </h1>
                <ul>
                  <li>We will use an IMU to monitor the pod’s movement. </li>
                  <li>The Inertial Measurement Unit (IMU) is was connected to the ODroid via USB and is used to collect information about the pod’s position, 
                  velocity, acceleration, yaw, pitch, roll, and angular rate.</li>
                  <li>We can use this data to perform numerous safety checks, including ensuring that the pod does not shake too much during motion.</li>
                  <li>We can use the velocity data, along with timing data, to calculate the distance traveled along the track.  </li>
                </ul>
            </ul>
      
      
            <h1 class="text-1xl py-4 font-bold text-gray-900">Ultrasonic Rangefinder</h1>
            <ul>
            <h1 class="text-1l py-4 font-bold text-gray-900">What is it: </h1>
                <ul>
                  <li>Matibox Ultrasonic Rangefinder</li>
                </ul>
                <h1 class="text-1l py-4 font-bold text-gray-900">Why are we using it: </h1>
                <ul>
                  <li>The Ultrasonic Rangefinder provides very short to long-range detection and ranging, in an incredibly small package. </li>
                  <li>It will be used to determine when the pod is approaching a turn.</li>
                  <li>It can detect objects from 0-254 inches (6.45-meters) and provides sonar range information from 6-inches out to 254-inches with 1-inch resolution.</li>
                  <li>The interface output formats included are pulse width output (PWM), analog voltage output (Vcc/512 volts per inch), and serial digital output (9600 baud).</li>
                  <li>An ultrasonic sensor is something that can measure distance and ideal for projects involving navigation and object avoidance.</li>
                  <li>They use sound to measure distance, meaning the availability of light is not a factor of their accuracy.</li>
                  <li>The distance is found by emitting a pulse of ultrasonic sound that travels through the air until it hits an object. Once the pulse hits an object, it reflects off the object and returns to the sensor.</li>     
                </ul>
              
            </ul>
      
      
            <h1 class="text-1xl py-4 font-bold text-gray-900">Vibration Sensor</h1>
            <ul>
            <h1 class="text-1l py-4 font-bold text-gray-900">What is it: </h1>
                <ul>
                  <li>SW-420 Vibration Sensor</li>
			<img src="img/vibration_sensor.jpg"  alt="???"/>
			<img src="img/vibration_arduino.jpg"  alt="???"/>
                </ul>
                <h1 class="text-1l py-4 font-bold text-gray-900">Why are we using it: </h1>
                <ul>
                  <li>The vibration sensor is also called a piezoelectric sensor. These sensors are flexible devices that use the piezoelectric effects while measuring the changes within acceleration, pressure, temperature, force, and strain by changing electrical charge. </li>
                </ul>
            </ul>
      
      
            <h1 class="text-1xl py-4 font-bold text-gray-900">Transmitter Receiver Module</h1>
            <ul>
            <h1 class="text-1l py-4 font-bold text-gray-900">What is it: </h1>
                <ul>
                  <li>NRF24L01 Transmitter-Reciever Module</li>
                </ul>
                <h1 class="text-1l py-4 font-bold text-gray-900">Why are we using it: </h1>
                <ul>
                  <li>This module will allow us to send messages between Arduinos. </li>
                  <li>There is an option to use an external antenna to extend the range if needed.</li>
                </ul>
            </ul>
      
      
            <h1 class="text-1xl py-4 font-bold text-gray-900">Pressure Sensor</h1>
            <ul>
            <h1 class="text-1l py-4 font-bold text-gray-900">What is it: </h1>
                <ul>
                  <li>EB100 Miniature Pressure Sensor</li>
                </ul>
                <h1 class="text-1l py-4 font-bold text-gray-900">Why are we using it: </h1>
                <ul>
                  <li>The pressure sensors are used to track real time changes in pressure within the pod, specifically located in the pneumatics and propulsion systems.</li>
                  <li>These sensors are used as a safety check to prevent any internal pressure build up inside the pod, as well as to check for leaks.</li>
                  <li>Each sensor is connected to an Arduino board according to its placement on the pod, and is read in analog.</li>
                  <li>The EB100 is lightweight and operates at a wide range of temperatures, from -40 to 125 C, which is essential to avoid damage in the case of overheating in the pod. </li>
                  <li>This sensor can detect pressures from 0 - 300 to 0 - 5000 psi with an accuracy of 0.25% while outputting a range of 8-30 VDC. </li>
                </ul>
            </ul>
      
      
            <h1 class="text-1xl py-4 font-bold text-gray-900">Inductive Proximity Sensor</h1>
            <ul>
            <h1 class="text-1l py-4 font-bold text-gray-900">What is it: </h1>
                <ul>
                  <li>LJ1283-4-Z/by Inductive Proximity Sensor</li>
                </ul>
                <h1 class="text-1l py-4 font-bold text-gray-900">Why are we using it: </h1>
                <ul>
                  <li>There will be four inductive proximity sensors, one placed at each corner of the pod. </li>
                  <li>These sensors will be used in conjunction with the retroreflective sensors as well as the IMU to help determine if we are on the track. </li>
                  <li>The sensor is triggered when it gets too close to a metal object so if the pod tilts too close to the beam of the track then it will get triggered. </li>
 
                </ul>
            </ul>
        </ul>
      </div>
    </a>
</div>
</div>
                            </div>
                        </div>
                    </main>
                </div>
            )
        } else {
            return <div className="SensorsSP21"></div>
        }

    }
}
