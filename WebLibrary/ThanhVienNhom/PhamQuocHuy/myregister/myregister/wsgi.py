"""
<<<<<<< HEAD
WSGI config for myregister project.
=======
WSGI config for Myregister project.
>>>>>>> f4edfd9e7fb786eb5df392a54a82db2019aa53b2

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

<<<<<<< HEAD
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myregister.settings')
=======
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Myregister.settings')
>>>>>>> f4edfd9e7fb786eb5df392a54a82db2019aa53b2

application = get_wsgi_application()
