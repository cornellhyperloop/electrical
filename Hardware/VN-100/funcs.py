#!/usr/bin/env python

"""
Module containing additional functions for the IMU.
"""


def extraData(s):
    # Acceleration
    accX = s.read_acceleration_measurements().x
    accY = s.read_acceleration_measurements().y
    accZ = s.read_acceleration_measurements().z

    # Angular Rate
    angRateX = s.read_angular_rate_measurements().x
    angRateY = s.read_angular_rate_measurements().y
    angRateZ = s.read_angular_rate_measurements().z

    # Magnetic field
    magX = s.read_imu_measurements().mag.x
    magY = s.read_imu_measurements().mag.y
    magZ = s.read_imu_measurements().mag.z

    # Internal Temperature
    temp = s.read_imu_measurements().temp

    # Pressure
    pressure = s.read_imu_measurements().pressure

    # Attitude Quaternion
    attQ = s.read_attitude_quaternion()

    return [accX, accY, accZ, angRateX, angRateY, angRateZ, magX, magY, magZ, temp, pressure, attQ]
