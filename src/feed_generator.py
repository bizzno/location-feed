"""Generate location feed from tracking data"""

def generate_feed(locations):
    """Generate RSS/JSON feed from location data"""
    feed = {
        'title': 'Location Feed',
        'items': []
    }

    for loc in locations:
        feed['items'].append({
            'coords': f"{loc['lat']},{loc['lng']}",
            'time': loc['timestamp']
        })

    return feed
Update 9 on 2014-01-08 12:02:55
Update 11 on 2014-01-10 07:07:35
Update 20 on 2014-01-15 23:02:07
Update 23 on 2014-01-15 02:12:25
Update 25 on 2014-01-15 07:11:25
Update 28 on 2014-01-16 10:59:03
Update 30 on 2014-01-16 06:57:29
Update 32 on 2014-01-16 00:02:08
Update 43 on 2014-01-18 16:56:50
Update 56 on 2014-01-20 04:28:38
Update 63 on 2014-01-24 06:46:35
Update 69 on 2014-01-24 10:10:01
Update 71 on 2014-01-26 04:49:28
Update 73 on 2014-01-26 05:08:54
Update 79 on 2014-01-26 18:14:38
Update 81 on 2014-01-27 03:11:27
Update 83 on 2014-01-27 06:56:14
Update 102 on 2014-02-03 09:51:43
Update 111 on 2014-02-05 21:32:34
Update 117 on 2014-02-06 00:22:02
Update 125 on 2014-02-07 02:14:30
Update 130 on 2014-02-07 03:11:54
Update 144 on 2014-02-19 06:14:23
Update 147 on 2014-02-23 08:14:31
Update 148 on 2014-02-23 20:10:34
Update 150 on 2014-02-24 15:35:58
Update 158 on 2014-02-24 22:03:25
Update 160 on 2014-02-25 15:40:03
Update 162 on 2014-02-25 05:32:47
Update 163 on 2014-02-25 17:12:22
Update 167 on 2014-02-26 17:02:36
Update 169 on 2014-02-26 10:59:23
Update 170 on 2014-03-01 23:49:06
Update 172 on 2014-03-01 09:00:21
Update 178 on 2014-03-04 12:13:37
Update 180 on 2014-03-04 09:40:23
Update 186 on 2014-03-05 15:36:37
Update 190 on 2014-03-05 01:49:48
Update 194 on 2014-03-06 06:32:12
Update 197 on 2014-03-06 06:00:07
Update 200 on 2014-03-06 04:14:37
Update 208 on 2014-03-08 17:25:56
Update 209 on 2014-03-08 01:23:41
