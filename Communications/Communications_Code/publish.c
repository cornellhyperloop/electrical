#include <unistd.h>
#include <zcm/zcm.h>
#include <sensor_info_t.h>
#include <stdio.h>
#include <stdlib.h>
#include <sys/ioctl.h>
#include <fcntl.h>
#include <termios.h>
#include <fcntl.h>
#include <string.h>

int main(int argc, char *argv[])
{
	zcm_t *zcm = zcm_create("udpm://234.255.76.67:7667?ttl=1");
	int fd;
	int stop = 0;
	// system( "MODE /dev/ttyACM0: BAUD=9600 PARITY=n DATA=8 STOP=1" );
	fd = open("/dev/ttyACM0", O_RDWR | O_NOCTTY);
	char buf[256];
	char accx[256];
	char accy[256];
	char accz[256];
	char gyro[256];
	char mag[256];
	char press[256];
	char prox[256];
	char dist[256];

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
	usleep(1000 * 1000);
	/* Flush anything already in the serial buffer */
	tcflush(fd, TCIFLUSH);

	msg.imu_acceleration_x = 1.0;
	// msg.imu_acceleration_x = atof(accx);
	msg.imu_acceleration_y = 2.0;
	// msg.imu_acceleration_y = atof(accy);
	msg.imu_acceleration_z = 3.0;
	// msg.imu_acceleration_z = atof(accz);
	msg.imu_gyroscope = 4.0;
	// msg.imu_gyroscope= atof(gyro);
	msg.imu_magnetometer = 5.0;
	// msg.imu_magnetometer = atof(mag);
	msg.pressure = 6.0;
	// msg.pressure = atof(press);
	// msg.temperature = 32.0;
	msg.temperature = atof(buf); // TODO: Get value from arduino
	msg.proximity = 8.0;
	// msg.proximity = atof(prox);
	msg.distance = 9.0;
	// msg.distance = atof(dist);

	while (stop == 0)
	{
		/* read up to 128 bytes from the fd */
		int n = read(fd, &buf, 128);
		usleep(500 * 1000);
		/* print how many bytes read */
		printf("%i bytes got read...\n", n);
		/* print what's in the buffer */
		printf("Buffer contains...\n%s\n", buf);

		// msg.temperature = atof(buf); // TODO: Get value from arduino
		sensor_info_t_publish(zcm, "SENSOR_INFO", &msg);
	}

	while (1)
	{
		sensor_info_t_publish(zcm, "SENSOR_INFO", &msg);
		usleep(1000000); /* sleep for a second */
	}

	zcm_destroy(zcm);
	return 0;
}
