# celery.py
from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# Установите переменную окружения 'DJANGO_SETTINGS_MODULE' равной вашему файлу настроек Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'practic.settings')

# Создайте экземпляр Celery и настройте его, используя файл настроек Django
celery_app = Celery('practic')

# Загрузите настройки из файла Django settings.py
celery_app.config_from_object('django.conf:settings', namespace='CELERY')

# Отметьте все файлы tasks.py внутри приложений Django
celery_app.autodiscover_tasks()
