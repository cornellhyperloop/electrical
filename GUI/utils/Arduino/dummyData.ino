void setup() {
    // put your setup code here, to run once:
    Serial.begin(9600);
}

void loop() {
    double s1val1 = 10.0;
    double s1val2 = 15.0;
    double s2val1 = 10.0;
    double s2val2 = 2.5;
    double s3val1 = 2.7;
    double s3val2 = 1.5;

    Serial.println("{ \"Sensor_name_1\": { \"Param_name_1\":" + String(s1val1) +
                   "\"Param_name_2\":" + String(s1val2) + "}," +
                   "{ \"Sensor_name_2\": { \"Param_name_1\":" + String(s2val1) +
                   "\"Param_name_2\":" + String(s2val2) + "}," +
                   "{ \"Sensor_name_3\": { \"Param_name_1\":" + String(s3val1) +
                   "\"Param_name_2\":" + String(s3val2) + "}");
}
