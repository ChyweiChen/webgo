# WebGo

Professional website builder landing site for small &amp; medium businesses, built with
**Python + Flask**. It serves a marketing homepage and hosts client showcase sites.

## Features

- **Homepage** (`/`) — English, mobile-first. Presents the services: Content Showcase,
  AI Agent Building and AI Customer Service. Pricing from **€80 / year** with lifetime
  after-sales support.
- **Showcase sites**:
  - `/ume-nail-studio/` — Ume Nail Studio website
  - `/ume_sec/` — Ume Studio website
- **Health check**: `/healthz` returns `{"status": "ok"}`.

## Project structure

```
webgo/
├── app.py                 # Flask application (entry point: app:app)
├── requirements.txt       # Python dependencies (Flask + gunicorn)
├── Dockerfile             # Production image (gunicorn WSGI server)
├── docker-compose.yml     # Container orchestration
├── .dockerignore
├── templates/
│   └── index.html         # Homepage template
├── ume_nail/              # Ume Nail Studio static site + assets
└── ume_sec/               # Ume Studio static site + assets
```

## Run locally (without Docker)

```bash
python -m pip install -r requirements.txt
python app.py
# open http://127.0.0.1:5000/
```

## Run locally with Docker

```bash
docker compose up --build
# open http://127.0.0.1/
```

---

## Deploy to Ubuntu

These steps assume a fresh Ubuntu 22.04/24.04 server and a user with `sudo`.

### 1. Install Docker &amp; Docker Compose

```bash
sudo apt-get update
sudo apt-get install -y ca-certificates curl git

# Add Docker's official repository
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] \
  https://download.docker.com/linux/ubuntu $(. /etc/os-release && echo $VERSION_CODENAME) stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

sudo apt-get update
sudo apt-get install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin

# (Optional) run docker without sudo — log out/in afterwards
sudo usermod -aG docker $USER
```

### 2. Get the code onto the server

```bash
git clone <your-repo-url> webgo
cd webgo
# or copy the folder up with: scp -r ./webgo user@server:/home/user/
```

### 3. Build and start

```bash
docker compose up -d --build
```

The site is now served on **port 80**. Visit `http://<server-ip>/`.

### 4. Verify

```bash
docker compose ps
curl http://localhost/healthz        # -> {"status":"ok"}
curl -I http://localhost/ume-nail-studio/
```

### 5. Updating after code changes

```bash
git pull            # or re-copy the files
docker compose up -d --build
```

### 6. Logs, stop, restart

```bash
docker compose logs -f        # follow logs
docker compose restart        # restart
docker compose down           # stop and remove the container
```

---

## Optional: custom domain + HTTPS (Nginx reverse proxy)

If you want a domain and a free TLS certificate, run WebGo on an internal port and put
Nginx + Certbot in front.

1. Change the port mapping in `docker-compose.yml` from `"80:5000"` to `"127.0.0.1:8000:5000"`.
2. Restart: `docker compose up -d --build`.
3. Install Nginx and Certbot:

   ```bash
   sudo apt-get install -y nginx
   sudo snap install --classic certbot
   sudo ln -s /snap/bin/certbot /usr/bin/certbot
   ```

4. Create `/etc/nginx/sites-available/webgo`:

   ```nginx
   server {
       listen 80;
       server_name yourdomain.com www.yourdomain.com;

       location / {
           proxy_pass http://127.0.0.1:8000;
           proxy_set_header Host $host;
           proxy_set_header X-Real-IP $remote_addr;
           proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
           proxy_set_header X-Forwarded-Proto $scheme;
       }
   }
   ```

5. Enable it and request a certificate:

   ```bash
   sudo ln -s /etc/nginx/sites-available/webgo /etc/nginx/sites-enabled/
   sudo nginx -t && sudo systemctl reload nginx
   sudo certbot --nginx -d yourdomain.com -d www.yourdomain.com
   ```

Certbot will configure HTTPS and auto-renewal.

---

## Firewall note

If `ufw` is enabled, allow the web ports:

```bash
sudo ufw allow 80/tcp
sudo ufw allow 443/tcp   # only if using HTTPS
```
