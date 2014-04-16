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
Update 116 on 2014-02-06 17:15:25
Update 126 on 2014-02-07 00:50:16
Update 127 on 2014-02-07 15:51:16
Update 128 on 2014-02-07 10:10:26
Update 140 on 2014-02-17 00:51:40
Update 146 on 2014-02-23 13:01:24
Update 151 on 2014-02-24 21:19:04
Update 154 on 2014-02-24 21:09:09
Update 155 on 2014-02-24 17:55:11
Update 161 on 2014-02-25 06:12:14
Update 175 on 2014-03-03 00:10:26
Update 177 on 2014-03-04 05:23:42
Update 179 on 2014-03-04 06:24:40
Update 188 on 2014-03-05 07:52:12
Update 192 on 2014-03-06 06:03:09
Update 199 on 2014-03-06 02:59:33
Update 210 on 2014-03-08 23:43:39
Update 211 on 2014-03-11 14:43:26
Update 213 on 2014-03-11 10:42:34
Update 216 on 2014-03-11 12:57:22
Update 218 on 2014-03-11 09:47:56
Update 221 on 2014-03-13 01:59:15
Update 223 on 2014-03-13 07:20:56
Update 226 on 2014-03-13 15:22:06
Update 230 on 2014-03-17 00:25:00
Update 235 on 2014-03-20 20:45:49
Update 252 on 2014-03-24 00:42:39
Update 261 on 2014-03-26 11:17:08
Update 263 on 2014-03-26 17:03:00
Update 268 on 2014-03-26 01:21:28
Update 272 on 2014-03-28 02:47:54
Update 277 on 2014-04-04 21:00:39
Update 288 on 2014-04-15 11:37:25
Update 291 on 2014-04-15 17:23:57
Update 293 on 2014-04-15 12:43:11
Update 295 on 2014-04-16 16:40:59
