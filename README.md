h1 table_booker - an app for booking tables in restaurants



    1. Create project folder - type 'mkdir table_booker' from home directory.
    2. Navigate to project folder i.e. type 'cd table_booker' in terminal 
    3. Type code . to open VSCODE in present working directory

    4. Type "pipenv shell" in VSCODE terminal - this creates Pipfile in the 'table_booker' project folder

    5. Type 'pipenv install --dev" in VSCODE terminal - this creates Pipfile.lock in the 'table_booker' project folder

    6. Type 'django-admin startproject project .' in VSCODE terminal. 
    This creates 'project' folder and 'manage.py' file in the 'table_booker' project folder 
    The (5) contents of the 'table_booker/project' folder are: --init.py, -- asgi.py, settings.py,  urls.py and wsgi.py

    5. Type 'python manage.py table_booker'in VSCODE terminal - This creates the 'table_booker/table_booker' app folder. 
    The (7) contents of the 'table_booker/table_booker' folder are: migrations folder (empty), --init--.py, admin.py, apps.py, models.py, tests.py and views.py

    6. Create urls.py in app folder - i.e. the 'table_booker/table_booker' folder. 
    In urls.py, type 'urlpatterns = []'

    7. Create 'templates' folder in 'table_booker/table_booker' folder

    8. Create 'table_booker' folder in 'templates' folder

    9. Open 'settings.py' in 'table_booker/project' folder. 
    Type 'table_booker.apps.TableBookerConfig' as the last line in 'INSTALLED_APPS' 
    In 'TEMPLATES', replace "DIRS: []," with "DIRS: [os.path.join(BASR_DIR, 'table_booker/templates/table_booker')],"

    10. Open 'urls.py' in 'table_booker/project' folder. 
    Type 'from django.contrib import admin' and 'from django.urls import include, path' at the top

    Type 'path("", include("table_booker.urls")),' as the top line in 'urlpatterns = [ ]'

BONUS STEPS

    Open models.py in 'table_booker/table_booker' folder 
    Type 'from django.db import models' at the top

    Type 'def --str--(self): 
    'return self.title' at the bottom

    Type 'python manage.py makemigrations' in VSCODE terminal

    Type 'python manage.py migrate' in VSCODE terminal

