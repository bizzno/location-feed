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
Update 3 on 2014-01-08 16:29:59
Update 6 on 2014-01-08 10:27:05
Update 7 on 2014-01-08 02:51:22
Update 12 on 2014-01-10 18:40:40
Update 16 on 2014-01-10 17:14:36
Update 29 on 2014-01-16 22:52:53
Update 35 on 2014-01-16 07:16:45
Update 46 on 2014-01-18 18:35:27
Update 47 on 2014-01-18 06:53:04
Update 50 on 2014-01-18 02:36:03
Update 55 on 2014-01-20 04:16:45
