# Crud_authentication
un ejemplo que expone el manejo de CRUD's  con authenticacion por token en inicio de usuario
para correrlo ejecutar los siguientes comandos en el CMD:

Para crear el entorno virtual:

cd C:\Users\...\Documents\Entornos
virtualenv rest
cd rest/Scripts/activate
cd rest/pip install django

luego ejecutamos migraciones de base de datos del proyecto :

cd C:\Users\...\Documents\Proyectos\crud_authention

python manage.py makemigrations
python manage.py migrate

ejecutamos tambien:
pip install django-bootstrap4
pip install django-widget-tweaks
pip install djangorestframework
pip install django-rest-auth
pip install django-crispy-forms

y por ultimo iniciamos el servidor
python manage.py runserver





