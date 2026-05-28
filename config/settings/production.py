import os

from .base import *

DEBUG = False

allowed_host_str = os.environ.get("DJANGO_ALLOWED_HOST", "127.0.0.1,localhost").split(",")

ALLOWED_HOSTS = [host.strip() for host in allowed_host_str]


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.environ.get("POSTGRES_DB"),
        "USER": os.environ.get("POSTGRES_USER"),
        "PASSWORD": os.environ.get("POSTGRES_PASSWORD"),
        "HOST": os.environ.get("POSTGRES_HOST"),
        "PORT": int(os.environ.get("POSTGRES_DB_PORT")),
    }
}