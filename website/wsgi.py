import os
import sys

# Ajoutez le chemin de votre projet à la variable d'environnement PYTHONPATH
sys.path.append('/home/django-blog/blog')

# Spécifiez le paramètre de module pour l'application
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'website.settings')

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
