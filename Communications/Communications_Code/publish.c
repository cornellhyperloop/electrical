#include <unistd.h>
#include <zcm/zcm.h>
#include <sensor_info_t.h>
#include <stdio.h>
#include <stdlib.h>
#include <sys/ioctl.h>
#include <fcntl.h>
#include <termios.h>
#include <stdlib.h>
#include <stdio.h>
#include <fcntl.h>

int main(int argc, char *argv[])
{
	zcm_t *zcm = zcm_create("udpm://234.255.76.67:7667?ttl=1");
	int fd;
	int stop=0;
	// system( "MODE /dev/ttyACM0: BAUD=9600 PARITY=n DATA=8 STOP=1" );
  	fd = open("/dev/ttyACM0", O_RDWR | O_NOCTTY);
	char buf[28];
	// int n = read(serialPort, &buf, 128);
	sensor_info_t msg;
	// printf("%s\n",buf);
	struct termios toptions;

	/* Get currently set options for the tty */
	tcgetattr(fd, &toptions);

	/* Set custom options */

	/* 9600 baud */
	cfsetispeed(&toptions, B9600);
	cfsetospeed(&toptions, B9600);
	/* 8 bits, no parity, no stop bits */
	toptions.c_cflag &= ~PARENB;
	toptions.c_cflag &= ~CSTOPB;
	toptions.c_cflag &= ~CSIZE;
	toptions.c_cflag |= CS8;
	/* no hardware flow control */
	toptions.c_cflag &= ~CRTSCTS;
	/* enable receiver, ignore status lines */
	toptions.c_cflag |= CREAD | CLOCAL;
	/* disable input/output flow control, disable restart chars */
	toptions.c_iflag &= ~(IXON | IXOFF | IXANY);
	/* disable canonical input, disable echo,
	disable visually erase chars,
	disable terminal-generated signals */
	toptions.c_lflag &= ~(ICANON | ECHO | ECHOE | ISIG);
	/* disable output processing */
	toptions.c_oflag &= ~OPOST;

	/* wait for 1 character to come in before read returns */
	/* WARNING! THIS CAUSES THE read() TO BLOCK UNTIL ALL */
	/* CHARACTERS HAVE COME IN! */
	toptions.c_cc[VMIN] = 1;
	/* no minimum time to wait before read returns */
	toptions.c_cc[VTIME] = 0;

	/* commit the options */
	tcsetattr(fd, TCSANOW, &toptions);

	/* Wait for the Arduino to reset */
	usleep(1000*1000);
	/* Flush anything already in the serial buffer */
	tcflush(fd, TCIFLUSH);

	while(stop == 0){

		/* read up to 128 bytes from the fd */
		int n = read(fd, &buf, 128);
		usleep(3000*1000);
		/* print how many bytes read */
		printf("%i bytes got read...\n", n);
		/* print what's in the buffer */
		printf("Buffer contains...\n%s\n", buf);
	}

	// struct sensor_info_t
	// {
	//   float imu_acceleration_x;
	//   float imu_acceleration_y;
	//   float imu_acceleration_z;
	//   float imu_gyroscope;
	//   float imu_magnetometer;
	//   float pressure;
	//   float temperature;
	//   float proximity;
	//   float distance;
	// }

	msg.imu_acceleration_x = 1.0;
	msg.imu_acceleration_y = 2.0;
	msg.imu_acceleration_z = 3.0;
	msg.imu_gyroscope = 4.0;
	msg.imu_magnetometer = 5.0;
	msg.pressure = 6.0;
	msg.temperature = 6.0; //TODO: Get value from arduino
	msg.proximity = 8.0;
	msg.distance = 9.0;

	while (1) {
		sensor_info_t_publish(zcm, "SENSOR_INFO", &msg);
		usleep(1000000); /* sleep for a second */
	}

	zcm_destroy(zcm);
	return 0;
}
