import requests
import config
import time
import smtplib
from email.mime.text import MIMEText
 
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
        sender_email = config.EMAIL_SENDER
        receiver_email = config.EMAIL_RECEIVER
        subject = "Your IP has changed"
        message = f"Your IP has changed from {config_ip} to {ip}\n\nPowered by @MATMAF\nhttps://www.mat.run"

        smtp_server = config.SMTP_SERVER
        smtp_port = config.SMTP_PORT

        smtp_username = config.EMAIL_SENDER
        smtp_password = config.SENDER_PASSWORD

        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(smtp_username, smtp_password)

        msg = MIMEText(message)
        msg['From'] = f'{sender_name} <{sender_email}>'
        msg['To'] = receiver_email
        msg['Subject'] = subject

        server.sendmail(sender_email, [receiver_email], msg.as_string())

        server.quit()

        ChangeIPInConfig(ip)

        config_ip = ip