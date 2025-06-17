# Import the geopy library's distance module to calculate geographic distances
import geopy.distance

# Function to calculate the distance between pickup and drop locations
def get_distance(pickup_location, drop_location):
    # Use geopy to calculate the great-circle distance in kilometers
    distance = geopy.distance.distance(pickup_location, drop_location).km
    return distance  # Return the distance in kilometers

# Function to determine price per kilometer based on booking hour
def price_per_km(hour):
    # If the booking hour is between 8 AM and 12 PM (inclusive)
    if hour >= 8 and hour <= 12:
        return 20  # Morning rate: 20 per km

    # If the booking hour is between 12 PM and 5 PM (inclusive)
    elif hour >= 12 and hour <= 17:
        return 15  # Afternoon rate: 15 per km

    else:
        return 10  # Evening/Night rate: 10 per km

# Function to calculate the final price based on distance and time
def get_final_price(pickup_location, drop_location, booking_hour):
    # Step 1: Calculate total distance using the helper function
    total_distance = get_distance(pickup_location, drop_location)

    # Step 2: Get the price per km based on booking time
    actual_price_per_km = price_per_km(booking_hour)

    # Step 3: Multiply distance with rate, round to 2 decimal places
    final_price = round(total_distance * actual_price_per_km, 2)

    return final_price  # Return the total price

# Example usage:

# Define pickup and drop coordinates as latitude and longitude
pickup_location = (23.4, 25.6)
drop_location = (34.6, 64.7)

# Define the hour of booking
booking_hour = 8

# Calculate and print the final price based on the given data
print("Final Price:", get_final_price(pickup_location, drop_location, booking_hour))

# Also print the distance separately
print("Distance in km:", get_distance(pickup_location, drop_location))
