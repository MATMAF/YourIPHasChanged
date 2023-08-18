import requests
import config
import time

def ChangeIPInConfig(ip):
    with open('config.py', 'r') as file:
        lines = file.readlines()
    new_value = ip
    for i, line in enumerate(lines):
        if 'IP_ADDRESS' in line:
            lines[i] = f'IP_ADDRESS = "{new_value}"\n'
    with open('config.py', 'w') as file:
        file.writelines(lines)

config_ip = config.IP_ADDRESS

while True:
    ip = requests.get("https://whatsmyipaddress.dev/ip").text

    if ip == config_ip:
        time.sleep(config.SLEEP_TIME)
    else:
        sender_name = 'YourIPHasChanged'
        receiver_email = config.EMAIL_RECEIVER
        subject = "Your IP has changed"
        message = f"Your IP has changed from {config_ip} to {ip}\n\nPowered by @MATMAF\nhttps://www.mat.run"
        SendMail = requests.get(f"https://mail.mat.run/api?name={sender_name}&receiver={receiver_email}&sub={subject}&message={message}")
        ChangeIPInConfig(ip)
        config_ip = ip