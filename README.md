# LDU STATS - BACKEND ⌨ ⚙️

Collect biometric and performance data from players' vests during football practice to improve athletic performance, customization of training programs, player health monitoring, etc.

## Project objetives

Allow coaching staff members generation of detailed reports on player performance and identification of training patterns to improve athletic performance 👓

Enhanced understanding of players' physical performance and the ability to adjust training strategies more effectively.

The project aims to improve decision-making in sports training through detailed analysis of data from players' vests 📈


## Libraries 📚

* 📚 rest_framework - To build web APIs in Django
* 📚 rest_framework_simplejwt - Provides a simple way to implement JWT-based authentication
* 📚 corsheaders - To facilitate the configuration of Cross-Origin Resource Sharing

## Folder Structure 📁
The project is structured as follows:

📁 ldustats-backend   
&nbsp;&nbsp;📁 app  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;📄 admin.py -> File to configure the administration interface  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;📄 apps.py -> Configure the application  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;📄 models.py -> Define the models of the database   
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;📄 serializer.py -> Define the serializers to the models  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;📄 tests.py -> To testing  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;📄 urls.py -> To define the URL of the application  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;📄 views.py -> File to define the views for the API REST  
&nbsp;&nbsp;📁 project  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;📄 settings.py -> Main configuration file of the project  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;📄 urls.py -> To define the URL of the project  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;📄 asgi.py -> To define the Asynchronous Server Gateway Interface  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;📄 wsgi.py -> To define the Web Server Gateway Interface  
&nbsp;&nbsp;🐍 manage.py -> Manage scripts of the project  
&nbsp;&nbsp;📄 requirements.txt -> List of dependencies of project  

## Technologies

* Django and Django Rest Framework for the server side ⚙️
* Vite with React JavaScript for the client side 👉👉 [ldustats-frontend](https://github.com/codigo-alan/ldustats-frontend) 🌐
* PostgreSQL 🗄️
