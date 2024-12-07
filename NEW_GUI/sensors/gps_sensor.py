from .base_sensor import BaseSensor


class Sensor(BaseSensor):
    def __init__(self, communication):
        super().__init__(
            name='GPS Sensor',
            communication=communication,
            sensor_id='GPS_SENSOR',
            data_fields=['latitude', 'longitude', 'altitude']
        )

    """
    Validate the incoming branch of data to ensure proper data flow
    """

    def validate_data(self, data):
        try:
            latitude = float(data['latitude'])
            longitude = float(data['longitude'])
            if not (-90 <= latitude <= 90):
                raise ValueError("Latitude out of range (-90 to 90)")
            if not (-180 <= longitude <= 180):
                raise ValueError("Longitude out of range (-180 to 180)")
            return True
        except (ValueError, KeyError) as e:
            print(f"Data validation error: {e}")
            return False

    def process_data(self, data):
        if self.validate_data(data):
            return {
                "latitude": round(float(data['latitude']), 6),
                "longitude": round(float(data['longitude']), 6),
                "altitude": round(float(data['altitude']), 2),
            }
        else:
            return None

    def read_sensor_data(self):
        raw_data = self.communication.receive()
        if raw_data:
            processed_data = self.process_data(raw_data)
            if processed_data:
                self.store_data(processed_data)
                return processed_data
        return None
