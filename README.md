# AWS CI/CD DJANGO

## Overview
This repository is for a tutorial on how to implement Django CI/CD Pipeline in AWS.
It contains important scripts needed to carry out both CI and CD operations respectively on AWS throoug CodeBuild and CodeDeploy


## CodeBuild
The script for running builds and tests for your application is the **buildspec.yml** file.

## CodeDeploy 
The script for running automated deployments to your server is the **appspec.ymL** file. 
This script contains paths to important scripts needed for the automated deployment
These scripts are described in-depth below

### Gunicorn
Gunicorn is an important component needed for deploying a django application to a server.
The configurations for the gunicorn service file is located in ```/gunicorn/gunicorn.service```

### Nginx
Nginx is also an essential component needed for deploying a django application to a server.
The configurations for the nginx configuration file is located in ```/nginx/nginx.conf```

### Scripts
The scripts folder holds scripts that are needed to automate the deployment.
Each script runs an important task that ultimately leads to the successfull deployment of your application
I will explain the use of each script below.
- ```clean_instance.sh``` : This script clears all files and directory in the path scpecified
- ```instance_os_dependencies.sh``` : This script installs the linux packages needed for the deployment of our application such as nginx, python3, python3-pip, etc.
- ```python_dependencies.sh``` : This script helps create a virtual environment, activates it, and installs the dependencies from the requirements.txt file specified
- ```gunicorn.sh``` : This script copies the specified gunicorn service to a gunicorn service on the server, starts the gunicorn service, and enables it.
- ```nginx.sh``` : This script copies the nginx configuration on our repository to another nginx configuration file on our server, and starts the nginx xervice.
- ```start_app.sh``` : This script edits the settings.py of your django project, adding the ip-address of your server to the ALLOWED_HOSTS list, and then restarts both the nginx and gunincorn services so the changes can take effect
- ```after_install.sh``` : This is a script that runs after the other scripts are successful.

## Conclusion
This is a simple CI/CD Django Pipeline repository that contains information and guides that helps explain the important scripts needed to setup a Django CI/CD Pipeline on AWS.

Contributions are welcome as well.
