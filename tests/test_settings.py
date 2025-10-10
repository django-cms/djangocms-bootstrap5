"""Django settings for djangocms-bootstrap5 tests."""
import os

# Build paths inside the project
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'test-secret-key-for-testing-only'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1']

# Application definition
INSTALLED_APPS = [
    'djangocms_admin_style',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.admin',

    # CMS
    'cms',
    'menus',
    'treebeard',
    'sekizai',

    # Dependencies
    'easy_thumbnails',
    'filer',
    'mptt',
    'djangocms_text_ckeditor',
    'djangocms_link',
    'djangocms_picture',

    # djangocms-bootstrap5
    'djangocms_bootstrap5',
    'djangocms_bootstrap5.contrib.bootstrap5_alerts',
    'djangocms_bootstrap5.contrib.bootstrap5_badge',
    'djangocms_bootstrap5.contrib.bootstrap5_card',
    'djangocms_bootstrap5.contrib.bootstrap5_carousel',
    'djangocms_bootstrap5.contrib.bootstrap5_collapse',
    'djangocms_bootstrap5.contrib.bootstrap5_content',
    'djangocms_bootstrap5.contrib.bootstrap5_grid',
    'djangocms_bootstrap5.contrib.bootstrap5_jumbotron',
    'djangocms_bootstrap5.contrib.bootstrap5_link',
    'djangocms_bootstrap5.contrib.bootstrap5_listgroup',
    'djangocms_bootstrap5.contrib.bootstrap5_media',
    'djangocms_bootstrap5.contrib.bootstrap5_picture',
    'djangocms_bootstrap5.contrib.bootstrap5_tabs',
    'djangocms_bootstrap5.contrib.bootstrap5_utilities',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.language.LanguageCookieMiddleware',
]

ROOT_URLCONF = 'tests.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'tests', 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'sekizai.context_processors.sekizai',
                'cms.context_processors.cms_settings',
            ],
        },
    },
]

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}

# Internationalization
LANGUAGE_CODE = 'en'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

LANGUAGES = [
    ('en', 'English'),
]

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Sites framework
SITE_ID = 1

# CMS Settings
CMS_LANGUAGES = {
    1: [
        {
            'code': 'en',
            'name': 'English',
            'public': True,
        },
    ],
    'default': {
        'fallbacks': ['en'],
        'redirect_on_fallback': True,
        'public': True,
        'hide_untranslated': False,
    }
}

CMS_TEMPLATES = [
    ('page.html', 'Page'),
]

CMS_PERMISSION = True
CMS_PLACEHOLDER_CONF = {}

# Thumbnail settings
THUMBNAIL_PROCESSORS = (
    'easy_thumbnails.processors.colorspace',
    'easy_thumbnails.processors.autocrop',
    'filer.thumbnail_processors.scale_and_crop_with_subject_location',
    'easy_thumbnails.processors.filters',
)

# djangocms-bootstrap5 settings
DJANGOCMS_PICTURE_RESPONSIVE_IMAGES = False
DJANGOCMS_PICTURE_RESPONSIVE_IMAGES_VIEWPORT_BREAKPOINTS = [576, 768, 992]
