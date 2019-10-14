# Book sharing platform
Building a ReST API with Django's rest framework, where authenticated users can securely share details about the books they own. 

Directions for use on Ubuntu/ Linux based systems:

1. Clone the repo
2. cd into the django-project directory
3. Run the Makefile with the command 'make'.
4. Run the command 'python3 manage.py runserver' to get the API running on http://127.0.0.1:8000/

Now you can post details of the books you own, see what books are owned by other authenticated users.
 
### Ongoing Work 

Writing Terraform script to host this on several EC2 servers, connected to a load balancer and an auto-scaling group.
