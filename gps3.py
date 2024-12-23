import gpsd

def get_gps_location():
    session = gps.gps("localhost", "2947")  # Connect to the local gpsd service
    session.stream(gps.WATCH_ENABLE | gps.WATCH_NEWSTYLE)

    try:
        while True:
            report = session.next()
            if report['class'] == 'TPV':
                if hasattr(report, 'lat') and hasattr(report, 'lon'):
                    latitude = report.lat
                    longitude = report.lon
                    print(f"Latitude: {latitude}, Longitude: {longitude}")
    except KeyboardInterrupt:
        print("GPS tracking stopped.")

if __name__ == "__main__":
    get_gps_location()