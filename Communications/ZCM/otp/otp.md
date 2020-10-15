The OTP packet type is designed for communications between the odroid and the pilot computer. It contains the following data necessarily for pilot decision making:

- state: The current state as estimated by the odroid (encoded as an integer)
- roll: The roll value resulting from sensor data (float)
- pitch: The pitch value resulting from sensor data (float)
- yaw: The yaw value resulting from sensor data (float)
- acceleration: The current pod acceleration value resulting from sensor data (float)
- position: The current pod position as calculated by the odroid (float)
- angular rate: The angular rate value resulting from sensor data (float)
