//Currently doesnt work ... Updating soon - Dana (dlo49)

// #include "Joystick.h"
// #include <avr/io.h>
// #include <util/delay.h>
// #include <Arduino.h>
#include <stdio.h>   /* Standard input/output definitions */
#include <string.h>  /* String function definitions */
#include <unistd.h>  /* UNIX standard function definitions */
#include <fcntl.h>   /* File control definitions */
#include <errno.h>   /* Error number definitions */
#include <termios.h> /* POSIX terminal control definitions */
#include <time.h>
#include <sys/types.h>
#include <stdlib.h>
#include <stdint.h>  /* Standard types */
#include <string.h>  /* String function definitions */
#include <unistd.h>  /* UNIX standard function definitions */
#include <fcntl.h>   /* File control definitions */
#include <errno.h>   /* Error number definitions */
#include <termios.h> /* POSIX terminal control definitions */
#include <sys/ioctl.h>
#include <getopt.h>
#include <stdio.h>

int main()
{

  // Method 1
  //Open communication with arduino
  int portName = open("/dev/ttyUSB0", O_RDWR | O_NOCTTY | O_NDELAY);

  struct termios options;
  tcgetattr(portName, &options);
  cfsetispeed(&options, B9600);
  cfsetospeed(&options, B9600);
  options.c_cflag |= (CLOCAL | CREAD);
  tcsetattr(portName, TCSANOW, &options);
  //8 bit characters
  options.c_cflag &= ~CSIZE; /* Mask the character size bits */
  options.c_cflag |= CS8;    /* Select 8 data bits */
  //No parity
  options.c_cflag &= ~PARENB;
  options.c_cflag &= ~CSTOPB;

  //Send Take Sample command to arduino
  char num[] = "3";

  write(portName, num, 1);
  printf("%s\n", num);

  //Read Hb answer

  unsigned char Hb[9];
  int pos = 0;
  while (pos < 50)
  {
    read(portName, Hb + pos, 1);
    if (Hb[pos] == '\n')
      break;
    printf("%i ", pos);
    printf("%x\n", Hb[pos]);
    pos++;
  }
  printf("%i\n", pos);

  Hb[4] = '\0';

  //Close communication
  close(portName);
}
