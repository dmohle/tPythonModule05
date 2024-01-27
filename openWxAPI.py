import requests

api_key = '33c4b4e0a8a9d34bd274f6d8f6200255'

city = input('Enter city name: ')

url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=imperial'

from datetime import datetime, timedelta

def convert_unix_to_local_time(unix_time, timezone_offset_seconds):
    # Convert Unix timestamp to UTC datetime
    utc_time = datetime.utcfromtimestamp(unix_time)
    # Adjust for the timezone offset
    local_time = utc_time + timedelta(seconds=timezone_offset_seconds)
    return local_time.strftime('%Y-%m-%d %H:%M:%S')


def print_nested_dict(d, indent=0):
    for key, value in d.items():
        print('    ' * indent + f"Key: {key},", end=" ")
        if isinstance(value, dict):
            print()
            print_nested_dict(value, indent + 1)
        elif isinstance(value, list):
            print(f"List of {len(value)} items:")
            for item in value:
                if isinstance(item, dict):
                    print_nested_dict(item, indent + 1)
                else:
                    print('    ' * (indent + 1) + str(item))
        else:
            print(f"Value: {value}")


response = requests.get(url)

if response.status_code == 200:
    data = response.json()



    # Call the function with the API response
    print_nested_dict(data)

    # Convert and print sunrise and sunset times
    sunrise_time = convert_unix_to_local_time(data['sys']['sunrise'], data['timezone'])
    sunset_time = convert_unix_to_local_time(data['sys']['sunset'], data['timezone'])

    print(f"Local Sunrise Time: {sunrise_time}")
    print(f"Local Sunset Time: {sunset_time}")

else:
    print('Error fetching weather data')