# Location Feed

Location tracking service with real-time feed generation and geolocation features.

## Features

- GPS location tracking
- Location history storage
- Feed generation with timestamps
- Geofencing and location alerts
- Distance and route calculation
- Map visualization support
- Privacy controls and data export

## Structure

```
src/
├── services/    - LocationService, tracking, and feed generation
├── models/      - Location and Route data models
├── utils/       - Distance calculation and geospatial utilities
└── storage/     - Database integration for location history
```

## Installation

Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Track a location:
```python
from src.services.locationService import LocationService

service = LocationService()
service.add_location(lat=37.7749, lng=-122.4194)
```

Generate location feed:
```python
feed = service.generate_feed(user_id='123', days=7)
for location in feed:
    print(f"{location['timestamp']}: {location['lat']}, {location['lng']}")
```

## Requirements

- Python 3.6 or higher
- geopy for geospatial calculations
- Database (SQLite, PostgreSQL, etc.)

## License

MIT
