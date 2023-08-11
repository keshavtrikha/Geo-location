from geopy.geocoders import Nominatim

# Initialize the geolocator
geolocator = Nominatim(user_agent="John")

# Get coordinates for a specific location
location = geolocator.geocode("Delhi")
latitude = location.latitude
longitude = location.longitude

print(f"Latitude of input place: {latitude},\nLongitude  of input place: {longitude}")
