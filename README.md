# django-project
Building a ReST API with Django's rest framework

There are certain pre-requisites that need to be met before we start working with our django project:

1. Run these commands to update the apt in your Ubuntu machine to upgrade apt

    sudo apt-get update
    
    sudo apt-get upgrade
    
2. Run this command to install all of the following modules listed below:

    sudo apt-get install build-essential python3-dev apache2 apache2-dev libapache2-mod-wsgi-py3 libmysqlclient-dev python3-venv
    
3. Now restart the apache server:

    sudo systemctl restart apache2.service
    
4. Configure the virtual environment (venv) for Django installation

    python3 –m venv venv
    
    source venv/bin/activate
    
5. Run the following commands to configure Django with Python3:

    sudo apt-get install python3-pip

    pip3 install django

    pip3 install djangorestframework
    
Now we have successfully installed Django (configured with the rest framework as well) and we can start developing our website using Django and Python3.

Once you have downloaded this folder, cd into the installation directory and run the following commands to get your website up and running:

python manage.py runserver
 
