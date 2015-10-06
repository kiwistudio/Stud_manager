import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# sqlite database
#DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': os.path.join(BASE_DIR, '..', 'db.sqlite3'),
    # }

# mysql database
#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.mysql',
#        'HOST': 'localhost',
#        'USER': 'students_db_user',
#        'PASSWORD': 'password',
#        'NAME': 'students_db',
#    }
#}


# Postrgresql database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'students_db',
        'USER': 'students_dbuser',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '',
    }
}
