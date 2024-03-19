//Gmock testing class

#include <MockSerialClass.h>
#include <gmock/gmock.h>
#include <gtest/gtest.h>

class MockSensors : public MockSerial {
    public:
        //MOCK_METHOD format
        //MOCK_METHOD(funcType, funcName, (params), (override));
        MOCK_METHOD(int, ReadData, (char *buffer, unsigned int nbChar), (const, override));
        MOCK_METHOD(bool, WriteData, (const char *buffer, unsigned int nbChar), ( override));
        MOCK_METHOD(bool, IsConnected, (), (override));



};