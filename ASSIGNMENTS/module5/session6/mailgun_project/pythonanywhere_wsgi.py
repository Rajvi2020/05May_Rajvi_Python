# +--------------------------------------------------------------------------+
# | PythonAnywhere WSGI Configuration Snippet                              |
# | Copy and paste the contents of this file into your PythonAnywhere WSGI   |
# | configuration file (located at /var/www/<your-username>_pythonanywhere_com_wsgi.py) |
# +--------------------------------------------------------------------------+

import os
import sys
from dotenv import load_dotenv

# 1. Add your project directory to the sys.path
path = '/home/YOUR_PYTHONANYWHERE_USERNAME/mailgun_project'
if path not in sys.path:
    sys.path.append(path)

# 2. Load environment variables from your .env file
env_path = os.path.join(path, '.env')
load_dotenv(dotenv_path=env_path)

# 3. Set the Django settings module
os.environ['DJANGO_SETTINGS_MODULE'] = 'api_project.settings'

# 4. Initialize WSGI application
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
