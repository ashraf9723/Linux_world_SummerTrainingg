from geopy.geocoders import Nominatim

# Initialize the geolocator
geolocator = Nominatim(user_agent="my_gps_app")

# Geocoding: Convert address to GPS coordinates
location = geolocator.geocode("1600 Amphitheatre Parkway, Mountain View, CA")
print("Latitude:", location.latitude)
print("Longitude:", location.longitude)

# Reverse Geocoding: Convert GPS coordinates to address
location = geolocator.reverse((37.422611, -122.084057))
print("Address:", location.address)

