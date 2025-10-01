from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'replace-this-in-production'
DEBUG = True
ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'portal',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'mars_portal.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'mars_portal.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
LOGIN_REDIRECT_URL = '/records/'
LOGOUT_REDIRECT_URL = 'login'
# -------------------

# -------------------
# Email (Webmail SMTP)
# -------------------
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "mail.marsbpo.co"             # SMTP server (common for cPanel webmail)
EMAIL_PORT = 587                           # use 587 with TLS
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False
EMAIL_HOST_USER = "agent@marsbpo.co"       # full email address
EMAIL_HOST_PASSWORD = "Vre6Z~hdQK#O~7;l"   # your webmail password
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

# Optional: global recipients
NOTIFICATION_EMAILS = [
    "agent@marsbpo.co",
]

# Department-based recipients
DEPARTMENT_RECIPIENTS = {
    "Medicare": [
        "usamabutt@marsbpo.co",
        "hassanali@marsbpo.co",
        "rajamoiz@marsbpo.co",
        "faraz@marsbpo.co",
    ],
    "Final Expense": [
        "usamabutt@marsbpo.co",
        "hassanali@marsbpo.co",
        "faraz@marsbpo.co",
    ],
    "HVAC": [
        "usamabutt@marsbpo.co",
        "hassanali@marsbpo.co",
        "faraz@marsbpo.co",
    ],
    "CSR's": [
        "usamabutt@marsbpo.co",
        "hassanali@marsbpo.co",
        "faraz@marsbpo.co",
    ],
    "Management": [
        "usamabutt@marsbpo.co",
        "hassanali@marsbpo.co",
        "faraz@marsbpo.co",  
    ],
} 