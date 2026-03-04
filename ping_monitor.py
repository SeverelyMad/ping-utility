import requests
import ping3
import time
from datetime import datetime

def get_geolocation(ip):
    response = requests.get(f"http://ip-api.com/json/{ip}")
    return response.json() if response.status_code == 200 else {}

def send_discord_notification(webhook_url, content):
    embed = {
        "embeds": [{
            "title": "Ping Status Update",
            "description": content,
            "timestamp": datetime.utcnow().isoformat(),
            "color": 5814783,  # Example color
        }]
    }
    requests.post(webhook_url, json=embed)

def main():
    ip_address = input("Enter the IP address to monitor: ")
    webhook_url = input("Enter your Discord webhook URL: ")
    previous_status = None

    while True:
        status = ping3.ping(ip_address)
        if status is None:
            current_status = "Offline"
        else:
            current_status = "Online"

        if current_status != previous_status:
            timestamp = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
            location = get_geolocation(ip_address)
            location_info = f"Location: {location.get('city', 'Unknown')}, {location.get('country', 'Unknown')}" if location else "Location: Unknown"
            message = f"{timestamp} - {ip_address} is now {current_status}. {location_info}"

            print(message)  # For console output
            send_discord_notification(webhook_url, message)
            previous_status = current_status

        time.sleep(5)  # Check every 5 seconds

if __name__ == "__main__":
    main()