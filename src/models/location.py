"""Location data model"""

class Location:
    def __init__(self, latitude, longitude, timestamp=None):
        self.latitude = latitude
        self.longitude = longitude
        self.timestamp = timestamp

    def to_dict(self):
        return {
            'latitude': self.latitude,
            'longitude': self.longitude,
            'timestamp': self.timestamp
        }
Update 2 on 2014-01-08 18:07:05
