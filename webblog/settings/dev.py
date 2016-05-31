from .common import *

INSTALLED_APPS += [
    'debug_toolbar',
]

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'