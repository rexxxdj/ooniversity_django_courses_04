import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

#DEBUG = False
#TEMPLATE_DEBUG = False

ALLOWED_HOSTS = ['127.0.0.1']

LOGGING = {
    'version': 1,
    'loggers':
    {
        'courses':{
            'handlers': ['file_courses'],
            'level': 'DEBUG',
        },
        'students':{
            'handlers': ['file_students'],
            'level': 'DEBUG',
        },
    },
    'handlers':
    {
        'file_courses':{
            'level': 'DEBUG',
            'class': 'logging.FileHandler', 
            'filename': os.path.join(BASE_DIR,'courses_logger.log'),
            'formatter': 'simple',
        },
        'file_students':{
            'level': 'WARNING',
            'class': 'logging.FileHandler', 
            'filename': os.path.join(BASE_DIR,'students_logger.log'),
            'formatter': 'verbose',
        },
    },
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(funcName)s %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
}

EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'rexxx'
EMAIL_HOST_PASSWORD = 'l;buehlf87'