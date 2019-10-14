
django-project:
	#sudo apt-get update
	#sudo apt-get upgrade
	sudo apt-get install build-essential python3-dev apache2 apache2-dev libapache2-mod-wsgi-py3 libmysqlclient-dev
	sudo systemctl restart apache2.service
	sudo apt-get install python3-pip
	pip3 install django djangorestframework
