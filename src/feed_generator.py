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
