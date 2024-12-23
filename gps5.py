import time, geocoder
from geopy.distance import geodesic


def get_current_location():
    location = geocoder.ip('me')

# Define the target coordinates (latitude, longitude)
target_coordinates = (48.14489, 19.555331)  # Replace with your target coordinates

def get_current_location1():
    try:
        # Simulate your current location (replace with your actual method of getting coordinates)
        current_coordinates = (location.latlng[0], location.latlng[1])  # Replace with your current coordinates

        # Calculate the distance between your current location and the target coordinates
        distance = geodesic(current_coordinates, target_coordinates).meters

        # Define a threshold distance (adjust as needed)
        threshold_distance = 100  # in meters

        # Check if you have arrived at the target location
        if distance <= threshold_distance:
            print("Arrived at the target location!")
        else:
            print(f"Distance to target location: {distance} meters")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    while True:
        get_current_location()
        get_current_location1()
        time.sleep(60)  # Check location every 60 seconds (adjust as needed)
