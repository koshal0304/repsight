"""E0-T03: the Celery app reads its broker from settings, never os.environ (05 §5.2)."""

from app.core.settings import settings
from worker import celery


def test_worker_takes_broker_url_from_settings() -> None:
    assert celery.conf.broker_url == settings.celery_broker_url
