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
