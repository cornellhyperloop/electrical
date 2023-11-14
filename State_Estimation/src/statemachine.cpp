#include <stdio.h>
#include <stdlib.h>
#include "constants.hpp"
#include "helperFunctions.hpp"
#include "SerialClass.h"
#include <iostream>

Serial::Serial(const char *portName)
{
  // We're not yet connected
  this->connected = false;

  // Try to connect to the given port throuh CreateFile
  this->hSerial = CreateFile(portName,
                             GENERIC_READ | GENERIC_WRITE,
                             0,
                             NULL,
                             OPEN_EXISTING,
                             FILE_ATTRIBUTE_NORMAL,
                             NULL);

  // Check if the connection was successfull
  if (this->hSerial == INVALID_HANDLE_VALUE)
  {
    // If not success full display an Error
    if (GetLastError() == ERROR_FILE_NOT_FOUND)
    {

      // Print Error if neccessary
      printf("ERROR: Handle was not attached. Reason: %s not available.\n", portName);
    }
    else
    {
      printf("ERROR!!!");
    }
  }
  else
  {
    // If connected we try to set the comm parameters
    DCB dcbSerialParams = {0};

    // Try to get the current
    if (!GetCommState(this->hSerial, &dcbSerialParams))
    {
      // If impossible, show an error
      printf("failed to get current serial parameters!");
    }
    else
    {
      // Define serial connection parameters for the arduino board
      dcbSerialParams.BaudRate = CBR_9600;
      dcbSerialParams.ByteSize = 8;
      dcbSerialParams.StopBits = ONESTOPBIT;
      dcbSerialParams.Parity = NOPARITY;
      // Setting the DTR to Control_Enable ensures that the Arduino is properly
      // reset upon establishing a connection
      dcbSerialParams.fDtrControl = DTR_CONTROL_ENABLE;

      // Set the parameters and check for their proper application
      if (!SetCommState(hSerial, &dcbSerialParams))
      {
        printf("ALERT: Could not set Serial Port parameters");
      }
      else
      {
        // If everything went fine we're connected
        this->connected = true;
        // Flush any remaining characters in the buffers
        PurgeComm(this->hSerial, PURGE_RXCLEAR | PURGE_TXCLEAR);
        // We wait 2s as the arduino board will be reseting
        Sleep(ARDUINO_WAIT_TIME);
      }
    }
  }
}

Serial::~Serial()
{
  // Check if we are connected before trying to disconnect
  if (this->connected)
  {
    // We're no longer connected
    this->connected = false;
    // Close the serial handler
    CloseHandle(this->hSerial);
  }
}

int Serial::ReadData(char *buffer, unsigned int nbChar)
{
  // Number of bytes we'll have read
  DWORD bytesRead;
  // Number of bytes we'll really ask to read
  unsigned int toRead;

  // Use the ClearCommError function to get status info on the Serial port
  ClearCommError(this->hSerial, &this->errors, &this->status);

  // Check if there is something to read
  if (this->status.cbInQue > 0)
  {
    // If there is we check if there is enough data to read the required number
    // of characters, if not we'll read only the available characters to prevent
    // locking of the application.
    if (this->status.cbInQue > nbChar)
    {
      toRead = nbChar;
    }
    else
    {
      toRead = this->status.cbInQue;
    }

    // Try to read the require number of chars, and return the number of read bytes on success
    if (ReadFile(this->hSerial, buffer, toRead, &bytesRead, NULL))
    {
      return bytesRead;
    }
  }

  // If nothing has been read, or that an error was detected return 0
  return 0;
}

bool Serial::WriteData(const char *buffer, unsigned int nbChar)
{
  DWORD bytesSend;

  // Try to write the buffer on the Serial port
  if (!WriteFile(this->hSerial, (void *)buffer, nbChar, &bytesSend, 0))
  {
    // In case it don't work get comm error and return false
    ClearCommError(this->hSerial, &this->errors, &this->status);

    return false;
  }
  else
    return true;
}

bool Serial::IsConnected()
{
  // Simply return the connection status
  return this->connected;
}

int readData()
{
  double startTime = GetTickCount();
  Serial *SP = new Serial("\\\\.\\COM3"); // adjust as needed

  if (SP->IsConnected())
    printf("We're connected");

  char incomingData[256] = ""; // don't forget to pre-allocate memory
  // printf("%s\n",incomingData);
  int dataLength = 255;
  int readResult = 0;

  while (SP->IsConnected())
  {
    double currTime = GetTickCount() - startTime;
    readResult = SP->ReadData(incomingData, dataLength);
    // printf("Bytes read: (0 means no data available) %i\n",readResult);
    incomingData[readResult] = 0;

    printf("%s", incomingData);

    Sleep(500);
    if (currTime >= 1000)
    {
      break;
    }
  }
  return readResult;
}

bool writeData(const char *buffer, unsigned int nbChar)
{
  double startTime = GetTickCount();
  Serial *SP = new Serial("\\\\.\\COM3"); // adjust as needed

  if (SP->IsConnected())
    printf("We're connected");

  bool writeResult;

  while (SP->IsConnected())
  {
    double currTime = GetTickCount() - startTime;
    writeResult = SP->WriteData(buffer, nbChar);

    printf("%d", writeResult);

    Sleep(500);
    if (currTime >= 1000)
    {
      break;
    }
  }
  return writeResult;
}

states verifySensors(double acceleromter[], double thermistor, double lidar_distance[], double ultrasonic)
{
  // TODO: Add more sensor parameters as needed with average values,
  // create functionality for average data value
  // double sensor1, sensor2 are average values of sensors over x amount of time
  // If sensors function correctly, go to PreAcceleration, otherwise go to Stop
  // TODO: Implement and return correct state
  // Accelerometer - 9 output values
  // Thermistor - 1 output value
  // Lidar - 2 output values
  // Ultrasonic - 1 output value

  // Accelerometer
  // std::this_thread::sleep_for(std::chrono::milliseconds(1000));

  for (int i = 0; i < 9; i++)
  {
    printf("%f\n", acceleromter[i]);
    if (acceleromter[i] < accelerometerMin[i] || acceleromter[i] > accelerometerMax[i])
      return Stop;
  }

  // Thermistor
  printf("%f\n", thermistor);
  if (thermistor < thermistorMin || thermistor > thermistorMax)
    return Stop;

  // Lidar for Distance
  for (int i = 0; i < 2; i++)
  {
    printf("%f\n", lidar_distance[i]);
    if (lidar_distance[i] < lidar_distanceMin[i] || lidar_distance[i] > lidar_distanceMax[i])
      return Stop;
  }

  // Ultrasonic
  printf("%f\n", ultrasonic);
  if (ultrasonic < ultrasonicMin || ultrasonic > ultrasonicMax)
    return Stop;
  printf("It has successfully passed\n");
  return PreAcceleration;
}

bool checkDistance(double totalDist, double travelDist, const float epsilon = 1E-5f)
{
  // TODO: Calibrate epsilon value after confirming with the mechanical team
  // Check if the pod has reached the total distance
  return (abs(totalDist - travelDist) <= epsilon);
}

states openBrakes()
{
  // Go to Emergency if does not work, otherwise go to Acceleration
  // Add manual interrupt to go into Emergency state
  // Check if there is a sensor/mechanism to get feedback on the Brake states, i.e opened/closed.
  // TODO: Implement and return correct state

  if (!writeData((char *)"Open", 4)) {
    printf("Error: Couldn't write data succesfully");
  }

  double relay_status = 0; // assuming 0 for open, 1 for close
  // ReadData(); // read relay status from arduino

  if (relay_status == 1)
  {
    return Emergency;
  }
  return Acceleration;

}

void closeBrakes()
{
  // TODO: Implement closeBrakeMain in helperFunctions.h
  // bool brakeClosed = closeBrakeMain(); // Commented for now since it's causing causing compilation errors due to function not being defined
  // Use bool brakeClosed to verify if the sensor implementation works correctly

  // TODO: Test functionality of writing to Serial
  if (!writeData((char *)"Close", 5)) {
    printf("Error: Couldn't write data succesfully");
  }

  // TODO: extract data of relay
  // serial.ReadData();
  double relay_status; // assuming 0 for open, 1 for close
  if (relay_status == 1)
  {
    return;
  }
  return;

  // return Emergency;
}

states accelerate(double sensorVelocity, double traveledDist)
{
  // Go to Emergency if does not work, otherwise go to Cruise or Deceleration
  // Add a while loop to stay in this case till it reaches the required velocity
  // Add manual interrupt to go into Emergency state
  // TODO: Implement and return correct state
  if (checkDistance(traveledDist, totalDist - decelRange))
  {
    return Deceleration;
  }
  else
  {
    if (sensorVelocity < desiredVelocity)
    {
      return Acceleration;
    }
    else
    {
      return Cruise;
    }
  }
  return Emergency;
}

states cruise(double sensorVelocity, double traveledDist)
{
  // Go to Emergency if does not work, otherwise go to Deceleration
  // Maintain the desired velocity while constantly reading form the sensor
  // Add manual interrupt to go into Emergency state
  // TODO: Implement and return correct state
  // logic is taken care off in acceleration!
  return accelerate(sensorVelocity, traveledDist);
}

states decelerate(double traveledDist)
{
  // Go to Emergency if does not work, otherwise go to Deceleration
  // Add a while loop to stay in this case till it needs to start to slow down
  // Add manual interrupt to go into Emergency state
  // TODO: Implement and return correct state
  closeBrakes();
  if (checkDistance(traveledDist, totalDist))
  {
    return Stop;
  }
  else
  {
    return Deceleration;
  }
  return Emergency;
}

states stop(double traveledDist)
{
  // Go to Crawl if does not work, otherwise go to PodOff
  // Add manual interrupt to go into Emergency state
  // TODO: Implement and return correct state
  if (checkDistance(traveledDist, totalDist))
  {
    return PodOff;
  }
  else
  {
    return Crawl;
  }
  return Emergency;
}

states emergency()
{
  // Close brakes rapidly and stop any propulsion
  decelerate(0.0);
  closeBrakes();
  return Stop;
}

void turnOff()
{
  // TODO: Implement killPower in helperFunctions.h
  // killPower(); // Commented out for now since it's causing compilation errors due to function not being defined
}

int main()
{
  states curr = Verification;
  states prev = Verification;
  // traveledDist = Serial Read for LIDAR to get Traveled Distance
  double traveledDist = 0.0;

  while (1)
  {
    switch (curr)
    {
    case Verification:
    {
      // Task 1: Turn on all sensors and motor(if necessary)
      /* Task 2: Make a verifySensors function to check they're all on,
                  and ensure readings are in a reasonable range.
      **/
      
      //  Update function call for verifySensors() with  appropriate parameters
      curr = verifySensors(readData()[0], readData()[1], readData()[2], readData()[3]); // CHANGE
      // curr = verifySensors(std::get<0>(readData()), stubValue);
      prev = Verification;
    };
    case PreAcceleration:
    {
      curr = openBrakes();
      prev = PreAcceleration;
    };
    case Acceleration:
    {
      curr = accelerate(lidar_distanceMax[0], traveledDist);
      prev = Acceleration;
    };
    case Cruise:
    {
      curr = cruise(lidar_distanceMax[0], traveledDist);
      prev = Cruise;
    };
    case Deceleration:
    {
      curr = decelerate(traveledDist);
      prev = Deceleration;
    };
    case Crawl:
    {
      curr = accelerate(lidar_distanceMax[0], traveledDist); // accelerate with slower speed
      prev = Crawl;
    };
    case Emergency:
    {
      curr = emergency();
      prev = Emergency;
    };
    case Stop:
    {
      curr = stop(traveledDist);
    };
    case PodOff:
    {
      break;
    }
    }
  }
}