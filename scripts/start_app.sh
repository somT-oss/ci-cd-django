#!/usr/bin/bash 

sed -i 's/\[]/\["3.84.7.210"]/' /home/ubuntu/ci-cd-django/main/settings.py
sudo systemctl restart gunicorn
sudo systemctl restart nginx
