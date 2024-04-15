/*
LinuxSerialClass parses data from our Serial Port
for our Raspberry Pi using standard Linux libraries
instead of Windows Libraries, which interfere with the
standard RaspbianOS on the Pi.

*/
#include <stdio.h>   // Standard input/output operations
#include <unistd.h>  // UNIX standard function definitions
#include <fcntl.h>   // File control options
#include <termios.h> // POSIX terminal control definitions
#include <string.h>  // String manipulation functions

class Serial
{
private:
    int hSerial;        // File descriptor for the serial port
    bool connected;     // Flag indicating whether the serial port is connected
    struct termios tty; // Structure to hold terminal settings

public:
    // Constructor to initialize the serial port
    Serial(const char *portName);
    // Destructor to close the serial port
    ~Serial();
    // Function to read data from the serial port
    int ReadData(char *buffer, unsigned int nbChar);
    // Function to write data to the serial port
    bool WriteData(const char *buffer, unsigned int nbChar);
    // Function to check if the serial port is connected
    bool IsConnected();
};

// Constructor definition
Serial::Serial(const char *portName)
{
    // Open the serial port
    hSerial = open(portName, O_RDWR | O_NOCTTY | O_NDELAY);
    if (hSerial == -1)
    {
        // Print error message if opening the port fails
        printf("Error opening port %s\n", portName);
        return;
    }

    // Get current serial port settings
    struct termios options;
    tcgetattr(hSerial, &options);

    // Set baud rate
    cfsetospeed(&options, B9600);
    cfsetispeed(&options, B9600);

    // Set data bits, parity, and stop bits
    options.c_cflag &= ~PARENB; // No parity
    options.c_cflag &= ~CSTOPB; // 1 stop bit
    options.c_cflag &= ~CSIZE;  // Clear the mask
    options.c_cflag |= CS8;     // 8 data bits

    // Apply the new settings
    tcsetattr(hSerial, TCSANOW, &options);

    // Flush any remaining data in the buffers
    tcflush(hSerial, TCIOFLUSH);

    // Set connected flag
    connected = true;
}

// Destructor definition
Serial::~Serial()
{
    // Close the serial port
    close(hSerial);
}

// Function to read data from the serial port
int Serial::ReadData(char *buffer, unsigned int nbChar)
{
    return read(hSerial, buffer, nbChar); // function to read data
}

// Function to write data to the serial port
bool Serial::WriteData(const char *buffer, unsigned int nbChar)
{
    return write(hSerial, buffer, nbChar) == nbChar;
}

// Function to check if the serial port is connected
bool Serial::IsConnected()
{
    return connected;
}
