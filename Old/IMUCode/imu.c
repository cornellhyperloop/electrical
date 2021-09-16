#include <stdio.h>

typedef struct {
	double x, y, z;
} Vec_t;

typedef struct {
	Vec_t ypr;
	Vec_t mag;
	Vec_t acc;
	Vec_t ang;
} IMU_data_t;

int is_valid(IMU_data_t imu_data) {
	return 1;
}

int main() {
	IMU_data_t imu_data = {
		{.1, .2, .3},
		{-.1, -.2, -.3},
		{1.1, 1.2, 1.3},
		{-1.1, -1.2, -1.3}
	};
    printf("%s\n", is_valid(imu_data) ? "true" : "false");
    return 0;
}
