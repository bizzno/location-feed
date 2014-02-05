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
Update 60 on 2014-01-20 10:52:05
Update 62 on 2014-01-24 23:39:11
Update 75 on 2014-01-26 08:10:51
Update 78 on 2014-01-26 21:53:24
Update 80 on 2014-01-27 06:55:53
Update 86 on 2014-01-30 12:16:36
Update 87 on 2014-01-30 03:44:17
Update 97 on 2014-02-03 10:35:43
Update 101 on 2014-02-03 01:14:33
Update 107 on 2014-02-05 22:36:34
Update 108 on 2014-02-05 05:11:54
Update 113 on 2014-02-05 12:09:32
