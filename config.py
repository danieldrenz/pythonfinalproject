import os
basedir = os.path.abspath(os.path.dirname(__file__))

CSRF_ENABLED = True
SECRET_KEY = 'god-is-good-all-the-time'

OPENID_PROVIDERS = [
	{'name': 'Yahoo', 'url': 'http://me.yahoo.com'}
]

'''OAUTH_CREDENTIALS = {
    'facebook': {
        'id': '695672250572235',
        'secret': 'a6c72f7491762f5a0ad572e06f5d2c93'
    }'''


SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

# mail server settings
MAIL_SERVER = 'localhost'
MAIL_PORT = 25
MAIL_USERNAME = None
MAIL_PASSWORD = None

# administrator list
ADMINS = ['you@example.com']
