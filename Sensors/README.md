# Hardware
The Hardware team's repo.

## Current Team Members

* Courtney Golden
* Jessica Yuan
* Nia Reid-Vicars
* Olivia McGoldrick
* Robert Fleming
* Ronin Sharma
* Tim Tran
* Winston Liu

## Semester Goals

This semester we will work closely with Software to integrate the sensors with the Odroid. We will wire the sensors to Arduinos for individual sensor testing, then combine all the sensors into one circuit, which will include multiple Arduinos, and then finally connect this circuit to the Odroid. We will also work on PCB design for possible integration with the BMS.

## Fall 2020 Sensors

_Inductive Proximity Sensor_: The purpose of this sensor is to detect metal objects approaching it without having the object make physical contact with the sensor. The sensing coil generates a high frequency magnetic field, and when a target approaches the magnetic field, an induction current flows in the target due to electromagnetic induction. As the target approaches the sensor, the induction current flow increases, causing the load on the oscillation circuit to increase as well. Then, the oscillation stops, and the sensor detects this change which outputs a detection signal.

_Ultrasonic Rangefinder_: The purpose of this sensor is to provide very short to long-range detection and ranging, in an incredibly small package. It can detect objects from 0-254 inches (6.45-meters) and provides sonar range information from 6-inches out to 254-inches with 1-inch resolution. An ultrasonic sensor can measure distance and is ideal for projects involving navigation and object avoidance. These sensors use sound to measure distance, meaning the availability of light is not a factor of their accuracy. The distance is found by emitting a pulse of ultrasonic sound that travels through the air until it hits an object. Once the pulse hits an object, it reflects off the object and returns to the sensor. 

_Vibration Sensor_: The purpose of this sensor is to use the piezoelectric effects to measure the changes within acceleration, pressure, temperature, force, and strain by changing electrical charge. These measurements are useful to detect imbalances or other issues in the asset and predict future breakdowns. The sensor either connects directly to an asset or monitors it wirelessly, and detects vibrations from the asset through various means. It can measure frequency (how often the vibration occurs) and intensity (vibration you have from a piece of equipment, the higher the intensity measurements will be).

_Pressure Sensor_: The purpose of this sensor is to measure the pressure of gasses and liquids. The sensor acts as a transducer and generates an electrical signal as a function of the pressure imposed. This sensor measures the absolute pressure of the air surrounding it, meaning it is dependent on both altitude and weather. Thus, it is important to read the temperature first before computing the pressure. 

_Tranmitter/Receiver Module_: The purpose of using this module is to send a message from one Arduino to another using 433 MHz. One board will be connected to a 433 MHz transmitter and will send the message, while the other Arduino board will be connected to a 433 MHz receiver to receive the messages. These transmitter/receiver modules are popular because of their low cost and ease to use, and can be used in all types of short-range, simplex-based communication between two microcontrollers.

_Retroreflective Sensor_: The purpose of this sensor is to provide an accurate detection of the target by having the sensor detect light or dark depending on the mode selected. Photoelectric Sensors detect objects, changes in surface conditions, and other items through a variety of optical properties. A Photoelectric Sensor consists primarily of an Emitter for emitting light and a Receiver for receiving light. When emitted light is interrupted or reflected by the sensing object, it changes the amount of light that arrives at the Receiver. The Receiver detects this change and converts it to an electrical output. The light source for the majority of Photoelectric Sensors is infrared or visible light. 

_Digital Light Sensor_: The purpose of this luminosity sensor is to detect different levels of light and change the voltage based on the brightness. This sensor may be useful to help sense the colored stripes on the track and is relatively cheap and easy to set up. Additionally, unlike other sensors, this particular sensor would allow us to measure infrared, full-spectrum, or human visible lights separately because it contains both infrared and full spectrum diodes.

