import os 
from . import BASE_DIR 
import dj_database_url


##  SECRET KEY settings
SECRET_KEY = os.environ.get('SECRET_KEY')

ALLOWED_HOSTS = ['.herokuapp.com']

DEBUG = (os.environ.get('DEBUG_VALUE') == 'True')


'''
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.psycop',
        'NAME': os.environ.get('NAME')
        'USER': os.environ.get('USER'),
        'PASSWORD': os.environ.get('PASSWORD'),
        'HOST': os.environ.get('HOST'),
        'PORT': os.environ.get('PORT'),
    }
}
'''


DATABASES = { 
    'default': dj_database_url.config(
        default= os.environ.get('DATABASE_URL')
    )
}


AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = os.getenv('AWS_STORAGE_BUCKET_NAME')

AWS_S3_FILE_OVERWRITE = False
AWS_DEFAULT_ACL = None 

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

