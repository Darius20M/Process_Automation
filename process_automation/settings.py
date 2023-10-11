import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-j58nn)ugu+flld5w-(sm%cs$+48*r4#&+z*%@fx%to%m=ep=0g'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework.authtoken',
    'rest_framework_simplejwt',
    'sequences.apps.SequencesConfig',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'dj_rest_auth.registration',
    'dj_rest_auth',
    'drf_yasg',
    'accounts',
    'general',
    'security',
    'catalog',
    'orders',
]
SITE_ID = 1

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = 'dariusjosedelacruzhilario@gmail.com'
DJANGO_FROM_EMAIL = 'dariusjosedelacruzhilario@gmail.com'
EMAIL_HOST_PASSWORD = 'lpsrosgrnpygneqi'

ACCOUNT_EMAIL_REQUIRED = True
EMAIL_CONFIRMATION = True
ACCOUNT_ADAPTER = 'security.adapters.CustomAccountAdapter'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'process_automation.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'process_automation.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": 'automation_process',
        "USER": 'darius',
        "PASSWORD": 'Darius20',
        "HOST": 'localhost',
        "PORT": 5432
    }
}
REST_AUTH = {
    'USE_JWT': True,
    'JWT_AUTH_COOKIE': 'access',
    'JWT_AUTH_REFRESH_COOKIE': 'refresh',
}
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        'dj_rest_auth.jwt_auth.JWTCookieAuthentication',

    ),
}
SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'APP': {
            'client_id': "246322974788-vao3rqf7tkft96r4p02speg49ovah837.apps.googleusercontent.com",
            'secret': "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",
            'key': ''
        },
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'online',
        },
        'OAUTH_PKCE_ENABLED': True,
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

JAZZMIN_SETTINGS = {
    "site_title": "UCSD",
    "site_header": "UCSD",
    "site_brand": "UCSD",
    "login_logo": None,

    "login_logo_dark": None,
    "site_logo_classes": "img-circle",
    "site_logo": "img/LogoFacultadCienciasytecnologia.png",
    "site_icon": "img/pru.png",
    "show_title_ajax": True,
    # Welcome text on the login screen
    "welcome_sign": "Welcome to the UCSD Admin",

    "copyright": "Darius de la cruz",
    "search_model": ["auth.User", "auth.Group"],

    "user_avatar": "img/man.png",

    "topmenu_links": [

        {"name": "Home", "url": "admin:index", "permissions": ["auth.view_user"]},
        {"name": "Support", "url": "https://github.com/farridav/django-jazzmin/issues", "new_window": True},
        {"model": "auth.User"},
        {"app": "books"},
    ],

    "usermenu_links": [
        {"name": "Support", "url": "https://github.com/farridav/django-jazzmin/issues", "new_window": True},
        {"model": "auth.user"}
    ],

    "show_sidebar": True,

    # Whether to aut expand the menu
    "navigation_expanded": True,
    "hide_apps": [],
    "hide_models": [],
    "order_with_respect_to": ["auth", "books", "books.author", "books.book"],

    "custom_links": {
        "books": [{
            "name": "Make Messages",
            "url": "make_messages",
            "icon": "fas fa-comments",
            "permissions": ["books.view_book"]
        }]
    },

    "messages": {
        "extra_tags": "alert-danger",  # Agrega clases CSS adicionales a los mensajes de error.
        "error_tags": "alert-danger",  # Clases CSS para mensajes de error.
        "warning_tags": "alert-warning",  # Clases CSS para mensajes de advertencia.
        "info_tags": "alert-info",  # Clases CSS para mensajes informativos.
        "success_tags": "alert-success",  # Clases CSS para mensajes de éxito.
    },
    "colors": {
        "primary": "#28a745",  # Cambia este valor al color verde que desees
        "secondary": "#6c757d",
        "info": "#17a2b8",
        "danger": "#dc3545",
        "warning": "#ffc107",
        "success": "#28a745",  # También cambia este valor para que coincida con el color principal
    },

    "icons": {
        "auth": "fas fa-user-lock",  # Cambia el ícono de autenticación
        "auth.user": "fas fa-user-circle",  # Cambia el ícono de usuario
        "accounts.DeanModel": "fas fa-user-circle",
        "accounts.TeacherModel": "fas fa-user-circle",
        "accounts.DirectorModel": "fas fa-user-circle",
        "accounts.StudentProfileModel": "fas fa-user-circle",
        "accounts.RoleModel": "fas fa-cog",
        "auth.Group": "fas fa-users",  # Cambia el ícono de grupo
    },
    "default_icon_parents": "fas fa-building",  # Cambia el ícono predeterminado para aplicaciones
    "default_icon_children": "fas fa-building",  # Cambia el ícono predeterminado para modelos

    "related_modal_active": False,
    "custom_css": None,
    "custom_js": None,
    "use_google_fonts_cdn": True,
    "show_ui_builder": True,

    "changeform_format": "single",
    "changeform_format_overrides": {"auth.user": "collapsible", "auth.group": "vertical_tabs"},

}

JAZZMIN_UI_TWEAKS = {
    "navbar_small_text": False,
    "footer_small_text": False,
    "body_small_text": False,
    "brand_small_text": False,
    "brand_colour": "navbar-navy",
    "accent": "accent-navy",
    "navbar": "navbar-navy navbar-dark",
    "no_navbar_border": False,
    "navbar_fixed": True,
    "layout_boxed": False,
    "footer_fixed": False,
    "sidebar_fixed": True,
    "sidebar": "sidebar-dark-success",
    "sidebar_nav_small_text": False,
    "sidebar_disable_expand": False,
    "sidebar_nav_child_indent": False,
    "sidebar_nav_compact_style": False,
    "sidebar_nav_legacy_style": False,
    "sidebar_nav_flat_style": False,
    "theme": "default",
    "dark_mode_theme": None,
    "button_classes": {
        "primary": "btn-primary",
        "secondary": "btn-secondary",
        "info": "btn-info",
        "warning": "btn-warning",
        "danger": "btn-danger",
        "success": "btn-success"
    },
    "actions_sticky_top": False
}
