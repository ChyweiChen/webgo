# WebGo

Professional website builder landing site for small &amp; medium businesses, built with
**Python + Flask**. It serves a marketing homepage and hosts client showcase sites.

## Features

- **Live site**: <https://webgo.fun/> (deployed on Alibaba Cloud ECS behind Nginx + HTTPS)
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

## Deploy to Ubuntu / Debian (apt-based)

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

## Deploy to Alibaba Cloud Linux 3 / Anolis (verified)

The following is the exact, verified flow for **Alibaba Cloud Linux 3 (OpenAnolis Edition)**,
which uses `dnf` (not `apt`) and keeps Nginx config under `/etc/nginx/conf.d/` (not
`sites-available/`). This is how <https://webgo.fun/> was deployed.

### 1. Install Docker and start the app

```bash
sudo dnf install -y docker git
sudo systemctl enable --now docker
sudo usermod -aG docker $USER      # then re-login (or run: newgrp docker)

git clone <your-repo-url> webgo
cd webgo
docker compose up -d --build
curl http://localhost/healthz      # -> {"status":"ok"}
```

At this point the container publishes port 80 directly and the site is reachable at
`http://<server-ip>/`.

### 2. Open ports in the Alibaba Cloud Security Group

In the ECS console → Security Group → inbound rules, allow:

- `80/tcp` (HTTP / certificate validation)
- `443/tcp` (HTTPS)

Source `0.0.0.0/0`. This is separate from any OS firewall and is required for public access.

### 3. Point the domain at the server

Add two DNS **A records** for your domain, both pointing to the server's public IP:

| Host | Type | Value |
|------|------|-------|
| `@`  | A    | your-server-ip |
| `www`| A    | your-server-ip |

Verify with `ping webgo.fun` before continuing.

### 4. Free port 80 for Nginx

Nginx must own ports 80/443, so move the container to a local-only port:

```bash
cd ~/webgo
sed -i 's|"80:5000"|"127.0.0.1:8000:5000"|' docker-compose.yml
grep -n 5000 docker-compose.yml            # expect: - "127.0.0.1:8000:5000"
docker compose up -d --force-recreate
docker compose ps                          # PORTS -> 127.0.0.1:8000->5000/tcp
sudo ss -tlnp | grep ':80 '                # should print nothing (port 80 free)
```

> Note: `docker compose up -d` only recreates the container when the config actually
> changed. If `docker compose ps` still shows `0.0.0.0:80->5000`, use `--force-recreate`.

### 5. Install and configure Nginx

```bash
sudo dnf install -y nginx

sudo tee /etc/nginx/conf.d/webgo.conf > /dev/null <<'EOF'
server {
    listen 80;
    listen [::]:80;
    server_name webgo.fun www.webgo.fun;

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
EOF

sudo nginx -t
sudo systemctl enable --now nginx
curl -I http://webgo.fun            # HTTP/1.1 200 OK, Server: nginx
```

A ready-made copy of this file lives at `nginx/webgo.conf` in the repo.

### 6. Enable HTTPS with a free Let's Encrypt certificate

```bash
sudo dnf install -y certbot python3-certbot-nginx   # add EPEL first if needed: sudo dnf install -y epel-release
sudo certbot --nginx -d webgo.fun -d www.webgo.fun
```

Answer the prompts:

1. **Email** — a real address (expiry reminders)
2. **Agree to Terms of Service** — **Y** (required; this is just the usage agreement, no cost)
3. **Share email with EFF** — N (optional)
4. **Redirect HTTP to HTTPS** — choose **2 (Redirect)**

Certbot deploys the certificate into `/etc/nginx/conf.d/webgo.conf`, enables the HTTP→HTTPS
redirect, and schedules automatic renewal. Verify:

```bash
curl -I https://webgo.fun          # HTTP/2 200
sudo certbot renew --dry-run       # confirm auto-renewal works
```

### 7. Firewall note (if firewalld is enabled)

```bash
sudo firewall-cmd --permanent --add-service=http
sudo firewall-cmd --permanent --add-service=https
sudo firewall-cmd --reload
```

### Architecture after setup

```
User → https://webgo.fun (443)
     → Nginx (TLS termination + reverse proxy)
     → Docker container (127.0.0.1:8000 → gunicorn:5000)
     → Flask app
```

Updating the site later does not touch Nginx or the certificate:

```bash
cd ~/webgo
git pull
docker compose up -d --build
```

---

## Optional: custom domain + HTTPS on Ubuntu/Debian (Nginx reverse proxy)

> For **Alibaba Cloud Linux / CentOS**, use the `dnf`-based section above instead —
> its Nginx config lives in `/etc/nginx/conf.d/`, not `sites-available/`.


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
