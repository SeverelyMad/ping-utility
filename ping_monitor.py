import os
import requests
import time

# Function to ping the given IP address
def ping_ip(ip_address):
    response = os.system('ping -c 1 ' + ip_address)
    return response == 0

# Function to send message to Discord webhook
def send_discord_message(webhook_url, ip_address, is_up):
    message = f'IP {ip_address} is {'up' if is_up else 'down'}.'
    data = {'content': message}
    requests.post(webhook_url, json=data)

# Main function to run the ping monitor
if __name__ == '__main__':
    ip_address = input('Please enter the IP address to monitor: ')
    webhook_url = input('Please enter your Discord webhook URL: ')

    while True:
        is_up = ping_ip(ip_address)
        send_discord_message(webhook_url, ip_address, is_up)
        time.sleep(60) # Wait for 60 seconds before the next ping
