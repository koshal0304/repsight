"""Celery worker and beat entry point (05 §3.1). No business logic here: tasks live in `app`."""

from celery import Celery

from app.core.settings import settings

celery = Celery("repsight", broker=settings.celery_broker_url)
