import geocoder

def get_current_location():
    try:
        # Get your current location using the 'ipinfo.io' provider
        location = geocoder.ip('me')
        
        # Print the latitude and longitude
        if location:
            print("Latitude:", location.latlng[0])
            print("Longitude:", location.latlng[1])
        else:
            print("Location not found")
    
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    get_current_location()


import math

# Define waypoints for your route (latitude, longitude)
waypoints = [
    (48.14827, 19.554161),  # depo
    (48.14489, 19.555331),  # zel st
    (48.144310, 19.56830),  # ip. teh.
    (48.14489, 19.56355),  # cast zel.st
    (48.14337, 19.563359),  # sasbik
    (48.145393, 19.572706),  # gortva
    (48.145182, 19.574502),  # gortva do zab.
    (48.133587, 19563729),  # kolonia
    (48.132788, 19.564949),  # kol do pose
    (48.133415, 19.564921),  # do kol.
    (48.132801, 19.565946),  # do doh
    (48.132652, 19.57910),  # do ostra skala
    (48.131545, 19.571070),  # doh
    (48.131349, 19.572230),  # durenda
    (48.13568, 19.573238),  # do hrad
    (48.13934, 19.574806),  # nove cintorin
    (48.132169, 19.582328),  # ragacou
    (48.13153, 19.574041),  # Hajnácka ulica Nového
    (48.13297, 19.573276),  # Hajnácka ulica Na Hradu
    (48.124715, 19.574760),  # Hajnácka ulica Selecov
    (48.125526, 19.581430),  # Hajnácka Zabovy
    (48.125803, 19.572141),  # Hajnácka Pekáren
    (48.125825, 19.571669),  # Hajnácka Lekáren
    (48.125590, 19.571480),  # Hajnácka Futbal Stadion
    (48.124722, 19.571848),  # Hajnácka ulica Pesov
    (48.125809, 19.571178),  # Hajnácka Centrum
    (48.13727, 19.57695),  # Hajnácka do Centrum
    (48.131545, 19.571070),  # Hajnácka Doh.
    (48.13044, 19.57132),  # Hajnácka Posa
    (48.125020, 19.564450),  # Hajnácka do Tilic
    (),  # Hajnacka Do Tenkes 
    (48.122840, 19.57837),  # Hajnácka Tenkes
    (48.12573, 19.57905),]  # Hajnácka do S.J.R.D.
# Simulated GPS coordinates (latitude, longitude)
current_location = (get_current_location())  # Start at the first waypoint

# Calculate the distance between two points using the Haversine formula
def calculate_distance(point1, point2):
    lat1, lon1 = point1
    lat2, lon2 = point2
    radius = 6371  # Earth's radius in kilometers

    # Convert latitude and longitude from degrees to radians
    lat1 = math.radians(lat1)
    lon1 = math.radians(lon1)
    lat2 = math.radians(lat2)
    lon2 = math.radians(lon2)

    # Haversine formula to calculate distance between two points
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    distance = radius * c

    return distance

# Calculate the initial route and distances
route_distances = []
for i in range(len(waypoints) - 1):
    distance = calculate_distance(waypoints[i], waypoints[i + 1])
    route_distances.append(distance)

# Simulate moving along the route
for i, waypoint in enumerate(waypoints[1:], start=1):
    current_distance = calculate_distance(current_location, waypoint)
    print(f"Distance to waypoint {i}: {current_distance:.2f} km")

    if current_distance < 0.1:  # Assuming you've arrived within 0.1 km
        print(f"You have arrived at waypoint {i}.")
    else:
        current_location = waypoint

print("You have reached your final destination.")

# Total route distance
total_distance = sum(route_distances)
print(f"Total route distance: {total_distance:.2f} km")