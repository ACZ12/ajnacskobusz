import tkinter as tk
from tkinterweb import HtmlFrame
import folium
import geocoder
import os

# Function to get current location
def get_current_location():
    g = geocoder.ip('me')  # Get location based on IP address
    return g.latlng if g.latlng else [52.2297, 21.0122]  # Default to Warsaw if location not found

# Function to create and save a Folium map as an HTML file
def create_map():
    location = get_current_location()
    m = folium.Map(location=location, zoom_start=13)
    folium.Marker(location, popup="You are here").add_to(m)
    map_path = "C:/Users/adamc/My__rep/my_location_map2.html"
    m.save(map_path)
    return map_path

# Tkinter window setup
root = tk.Tk()
root.title("Map Display with Drawing in Tkinter")
root.geometry("800x600")

# Create the map and get the path to the HTML file
map_path = create_map()

# Convert the file path to a proper URL format
map_url = f"file:///{map_path.replace(os.sep, '/')}"  # Ensure forward slashes for URL

# Create a Tkinter HtmlFrame to display the HTML content
frame = HtmlFrame(root, horizontal_scrollbar="auto")
frame.pack(fill="both", expand=True)

# Error handling for loading the website
try:
    frame.load_website(map_url)
except Exception as e:
    print(f"Error loading website: {e}")

# Run the Tkinter main loop
root.mainloop()
