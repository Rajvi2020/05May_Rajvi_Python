4. Purpose of Key Files 
1. manage.py
manage.py is the command-line utility for managing the Django project.
It is used to run the development server, create apps, apply database migrations, and execute other Django commands.
It acts as the entry point for interacting with the project.
2. settings.py
settings.py contains all the configuration settings of the Django project.
It includes database settings, installed apps, middleware, templates, static files, security settings, and other project configurations.
It controls how the Django application behaves.
3. urls.py
urls.py defines the URL routing for the project.
It maps web addresses (URLs) to the appropriate view functions or class-based views.
It determines which page or functionality is displayed when a user visits a specific URL.
4. wsgi.py
wsgi.py provides the WSGI (Web Server Gateway Interface) application for the project.
It is used when deploying the Django application on traditional web servers such as Gunicorn or uWSGI.
It allows the web server to communicate with the Django application.
5. asgi.py
asgi.py provides the ASGI (Asynchronous Server Gateway Interface) application for the project.
It supports asynchronous features such as WebSockets, real-time messaging, and long-lived connections.
It is commonly used for modern asynchronous Django deployments.



5. Comparison Between Django and Flask
Django	Flask
Django is a full-featured web framework with built-in authentication, admin panel, ORM, and security features.	Flask is a lightweight micro-framework that provides only the essential tools, allowing developers to choose additional libraries as needed.
It is suitable for large and complex web applications.	It is best for small projects, APIs, and simple web applications.
Example: Instagram or Zomato are better suited to Django because they require user authentication, database management, security, and scalability.	Flask is ideal for small applications such as a simple blog, portfolio website, or REST API where minimal setup and flexibility are important.