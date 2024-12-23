import time
import math
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut

def get_current_location():
    try:
        # Create a geocoder object (Nominatim in this case)
        geolocator = Nominatim(user_agent="myGeocoder")
        
        while True:
            # Get your current location
            location = geolocator.geocode("Fiľakovo")

            # Print the latitude and longitude
            if location:
                print("Latitude:", location.latitude)
                print("Longitude:", location.longitude)
            else:
                print("Location not found")

            # Wait for a specified interval (e.g., 60 seconds) before updating again
            time.sleep(1)  # You can adjust the interval as needed

    except GeocoderTimedOut:
        print("Geocoding service timed out. Try again later.")

if __name__ == "__main__":
    get_current_location()
