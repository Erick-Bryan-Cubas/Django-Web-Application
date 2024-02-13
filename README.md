# Django Web Application

## Overview
This repository contains a Django web application which is deployed using NGINX as the web server, uWSGI as the WSGI server, and is managed by systemd on an AWS EC2 instance. This setup ensures a robust production environment for handling web requests.

## Architecture
- **NGINX**: Serves as the front-facing web server to handle client requests and static assets.
- **uWSGI**: Acts as the WSGI server which serves the Django application by translating web requests from NGINX to Python calls.
- **Systemd**: Used for initializing and managing the uWSGI process.
- **Django**: The Python web framework where the application logic resides.

## Prerequisites
- Python 3.6 or higher
- Django 2.2 or higher
- uWSGI
- NGINX
- Virtualenv (recommended)
- AWS EC2 instance
- SSH client
- Private key file (e.g., `django-master-key.pem`)

## Installation & Setup

### Connect to AWS EC2 Instance
1. Remove inherited permissions and assign unique permissions to your user:
   ```powershell
   icacls.exe "django-master-key.pem" /reset
   icacls.exe "django-master-key.pem" /grant:r "$($env:USERNAME):(R)"
   icacls.exe "django-master-key.pem" /inheritance:r
   ```

2. Connect to your instance using the provided public DNS (replace `'IP-segmented-by-dashes'` with your actual IP address):
   ```sh
   ssh -i "django-master-key.pem" ubuntu@ec2-'IP-segmented-by-dashes'.compute-1.amazonaws.com
   ```

### Set Up the Django Project
1. Clone the repository:
   ```sh
   git clone https://github.com/Erick-Bryan-Cubas/DjangoMaster.git
   ```
2. Navigate to the project directory:
   ```sh
   cd DjangoMaster/carros
   ```
3. Create a virtual environment and activate it:
   ```sh
   virtualenv venv
   source venv/bin/activate
   ```
4. Install the required dependencies:
   ```sh
   pip install -r requirements.txt
   ```

### Configure NGINX
1. Install NGINX and create `carros.conf`:
   ```sh
   sudo apt install nginx
   cd /etc/nginx/sites-available
   sudo nano carros.conf
   ```
2. Add the following server block to `carros.conf`, replacing `<YOUR_IP>` with your server's IP:
   ```nginx
   upstream django {
       server unix:///var/www/DjangoMaster/carros/carros.sock; # for a file socket
   }
   server {
       listen 80;
       server_name <YOUR_IP>;
       
       client_max_body_size 75M;
       
       location /media  {
           alias /var/www/DjangoMaster/carros/media; # your Django project's media files
       }
       
       location /static {
           alias /var/www/DjangoMaster/carros/static; # your Django project's static files
       }
       
       location / {
           uwsgi_pass django;
           include /var/www/DjangoMaster/carros/uwsgi_params; # the uwsgi_params from Django
       }
   }
   ```

### Set Up uWSGI
1. Create `carros_uwsgi.ini` inside your project directory with the following content:
   ```ini
   [uwsgi]
   chdir           = /var/www/DjangoMaster/carros
   module          = app.wsgi
   home            = /var/www/DjangoMaster/carros/venv
   master          = true
   processes       = 10
   socket          = /var/www/DjangoMaster/carros/carros.sock
   chmod-socket    = 666
   vacuum          = true
   ```

### Configure Systemd
1. Create a systemd service file for your project:
   ```sh
   sudo nano /etc/systemd/system/carros.service
   ```
2. Add the following configuration, adjusting paths as needed:
   ```ini
   [Unit]
   Description=uWSGI instance to serve carros
   After=network.target
   
   [Service]
   User=root
   Group=root
   WorkingDirectory=/var/www/DjangoMaster/carros
   ExecStart=/var/www/DjangoMaster/carros/venv/bin/uwsgi --ini /var/www/DjangoMaster/carros/carros_uwsgi.ini
   
   [Install]
   WantedBy=multi-user.target
   ```

## Running the Application
To start the application, use the following systemd commands:
```sh
sudo systemctl daemon-reload
sudo systemctl start carros
sudo systemctl enable carros
sudo systemctl status carros
```

## License
Please see the [LICENSE.md](https://github.com/Erick-Bryan-Cubas/DjangoMaster/blob/main/LICENSE.md) file for details.

## Contributors ✨
We welcome contributions! Please read the [CONTRIBUTING.md](https://github.com/Erick-Bryan-Cubas/DjangoMaster/blob/main/CONTRIBUTING.md) file to see how you can help improve this project.
