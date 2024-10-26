import requests
import phonenumbers
from phonenumbers import geocoder, carrier

def get_ip_info(ip):
    url = f"http://ip-api.com/json/{ip}"
    response = requests.get(url)
    data = response.json()

    if data['status'] == 'success':
        return data
    else:
        return None

def get_phone_info(phone):
    number = phonenumbers.parse(phone, "CH")
    location = geocoder.description_for_number(number, "en")
    service_provider = carrier.name_for_number(number, "en")
    return location, service_provider

def main():
    phone_number = input("Enter the phone number with country code (e.g., +1234567890): ")
    
    # Get phone info
    location, service_provider = get_phone_info(phone_number)
    
    print(f"Location: {location}")
    print(f"Service Provider: {service_provider}")
    
    ip_address = input("Enter an IP address to lookup: ")
    
    # Get IP info
    ip_info = get_ip_info(ip_address)
    if ip_info:
        print(f"IP: {ip_info['query']}")
        print(f"Country: {ip_info['country']}")
        print(f"Region: {ip_info['regionName']}")
        print(f"City: {ip_info['city']}")
        print(f"ZIP: {ip_info['zip']}")
        print(f"Latitude: {ip_info['lat']}")
        print(f"Longitude: {ip_info['lon']}")
        print(f"ISP: {ip_info['isp']}")
        print(f"Org: {ip_info['org']}")
        print(f"AS: {ip_info['as']}")
    else:
        print("Invalid IP address or request limit exceeded.")

if __name__ == "__main__":
    main()
