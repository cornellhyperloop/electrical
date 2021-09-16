/*
Transmitter Code
Incorporates functions from Two-Thermistor and Inductive Proximity Sensor
Date: November 10, 2020
*/

// Setup code needed for Transmitter
#include <RH_ASK.h>
#include <SPI.h> // Not actually used but needed to compile
RH_ASK driver;

// Setup code needed for Inductive Proximity Sensor
const int proximityInput = 2; // Input Output
const int LED = 13;

int sensorState; // Sensor Variable
int dist;
char* distance;

// Setup code needed for Thermistors
int thermistorPin[] = {A0, A1}; //analog input pins
int thermistorNum = sizeof(thermistorPin)/sizeof(int);
int Vo;
float R1 = 10000;
float logR2, R2, T, Tc, Tf;
float c1 = 1.009249522e-03, c2 = 2.378405444e-04, c3 = 2.019202697e-07;
char* temp;
