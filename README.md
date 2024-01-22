# YourIPHasChanged
Simple email sender when your IP address changed.
## Install
### Clone this repo
```
git clone https://github.com/MATMAF/YourIPHasChanged.git
cd YourIPHasChanged
```

Edit `docker-compose.yml`

Replace `EMAIL_RECEIVER=email@example.com` with your email address

### Start docker container

```
docker compose up -d
```

You will receive an email with your IP address and the new one if your IP changed.
