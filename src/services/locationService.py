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
