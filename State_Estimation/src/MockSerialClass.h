#ifndef SERIALCLASS_H_INCLUDED
#define SERIALCLASS_H_INCLUDED

#define ARDUINO_WAIT_TIME 2000

// to use instead of Mac OS X's default /dev/tty.*
#define SERIAL_PORT "/dev/tty.ttyACM0"
#include <windows.h>
#include <stdio.h>
#include <stdlib.h>

class MockSerial
{
private:
  // Serial comm handler
  HANDLE hSerial;
  // Connection status
  bool connected;
  // Get various information about the connection
  COMSTAT status;
  // Keep track of last error
  DWORD errors;

public:
  // Initialize Serial communication with the given COM port
  MockSerial(const char *portName);
  // Close the connection
  ~MockSerial();
  // Read data in a buffer, if nbChar is greater than the
  // maximum number of bytes available, it will return only the
  // bytes available. The function return -1 when nothing could
  // be read, the number of bytes actually read.
  virtual int ReadData(char *buffer, unsigned int nbChar) ;
  // Writes data from a buffer through the Serial connection
  // return true on success.
  virtual bool WriteData(const char *buffer, unsigned int nbChar);
  // Check if we are actually connected
  virtual bool IsConnected();

};

#endif // SERIALCLASS_H_INCLUDED
