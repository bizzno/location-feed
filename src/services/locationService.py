"""Location tracking and feed service"""
import json
from datetime import datetime

class LocationService:
    def __init__(self):
        self.locations = []

    def add_location(self, lat, lng, timestamp=None):
        """Add a new location point"""
        location = {
            'lat': lat,
            'lng': lng,
            'timestamp': timestamp or datetime.now().isoformat()
        }
        self.locations.append(location)
        return location

    def get_recent(self, limit=10):
        """Get recent location points"""
        return self.locations[-limit:]
Update 1 on 2014-01-08 10:11:00
Update 5 on 2014-01-08 00:18:38
Update 10 on 2014-01-10 18:58:50
Update 14 on 2014-01-10 07:57:29
Update 18 on 2014-01-14 06:03:12
Update 22 on 2014-01-15 03:10:15
Update 27 on 2014-01-15 09:44:16
Update 31 on 2014-01-16 15:33:45
Update 37 on 2014-01-17 14:04:59
Update 42 on 2014-01-18 03:05:44
Update 48 on 2014-01-18 20:53:55
Update 51 on 2014-01-18 11:28:16
Update 53 on 2014-01-18 08:16:36
Update 57 on 2014-01-20 08:24:29
Update 59 on 2014-01-20 06:44:15
Update 70 on 2014-01-24 12:33:04
Update 77 on 2014-01-26 09:22:24
Update 84 on 2014-01-27 22:25:17
Update 89 on 2014-01-30 06:35:29
Update 93 on 2014-02-03 03:20:13
Update 94 on 2014-02-03 23:20:45
Update 96 on 2014-02-03 16:57:38
Update 99 on 2014-02-03 12:52:02
Update 109 on 2014-02-05 19:28:38
Update 110 on 2014-02-05 14:52:26
Update 129 on 2014-02-07 16:31:15
Update 133 on 2014-02-11 13:00:09
Update 143 on 2014-02-17 03:57:16
Update 149 on 2014-02-24 03:08:31
Update 157 on 2014-02-24 18:05:21
Update 159 on 2014-02-24 02:49:02
Update 171 on 2014-03-01 10:04:45
Update 173 on 2014-03-01 19:37:35
Update 176 on 2014-03-04 14:11:05
Update 181 on 2014-03-04 11:00:33
Update 184 on 2014-03-04 11:07:35
Update 195 on 2014-03-06 19:26:16
Update 198 on 2014-03-06 13:55:50
Update 205 on 2014-03-06 05:45:05
Update 207 on 2014-03-08 06:47:33
Update 212 on 2014-03-11 22:21:22
Update 217 on 2014-03-11 14:00:45
Update 224 on 2014-03-13 01:10:44
Update 232 on 2014-03-19 15:06:06
Update 233 on 2014-03-19 12:39:17
Update 236 on 2014-03-20 01:07:56
Update 237 on 2014-03-20 23:24:05
Update 247 on 2014-03-24 19:25:22
Update 248 on 2014-03-24 21:48:28
Update 255 on 2014-03-25 00:56:54
Update 258 on 2014-03-25 22:56:41
Update 274 on 2014-03-28 03:19:09
Update 276 on 2014-03-31 15:30:19
Update 280 on 2014-04-04 00:20:13
Update 289 on 2014-04-15 16:17:55
