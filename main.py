import phonenumbers
from phonenumbers import geocoder, carrier

# Function to read phone numbers from a file
def read_phone_numbers(file_path):
    with open(file_path, 'r') as file:
        # Read lines, strip whitespace, and split by '#' to ignore comments
        numbers = [line.strip().split('#')[0] for line in file.readlines() if line.strip()]
    return numbers

# Read phone numbers from the dataset
phone_numbers = read_phone_numbers("phone_numbers.txt")

# Loop through each phone number to get the location and carrier
for number in phone_numbers:
    try:
        # Parse the number with a default region (change "CH" and "RO" as needed)
        ch_nmber = phonenumbers.parse(number, "CH")  # For geolocation
        location = geocoder.description_for_number(ch_nmber, "en")
        print(f"Location for {number}: {location}")

        service_nmber = phonenumbers.parse(number, "RO")  # For carrier
        carrier_name = carrier.name_for_number(service_nmber, "en")
        print(f"Carrier for {number}: {carrier_name}")

    except phonenumbers.NumberParseException as e:
        print(f"Error parsing number {number}: {e}")
    except Exception as e:
        print(f"Unexpected error for {number}: {e}")


