from . import BASE_DIR 



SECRET_KEY = 'django-insecure-wes3s**)s@$4c2z7^ps+ibwi_se+dd=iw8d)wmnsg)lc)e5@fm'


DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


ALLOWED_HOSTS = ['127.0.0.1']

AWS_ACCESS_KEY_ID = "AKIA6C4ROCUU6FVO6LUL"
AWS_SECRET_ACCESS_KEY = "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"
AWS_STORAGE_BUCKET_NAME = "django-site-files"