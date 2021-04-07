import os

from celery import Celery
from time import sleep
from celery.utils.log import get_task_logger

os.environ.setdefault('CELERY_CONFIG_MODULE', 'celery_config')

celery = Celery('app')
celery.config_from_envvar('CELERY_CONFIG_MODULE')

# Create logger - enable to display messages on task logger
celery_log = get_task_logger(__name__)

@celery.task
def add(x, y):
    res = int(x) + int(y)
    celery_log.info("Adding %s + %s, res: %s" % (x, y, res))
    return res

@celery.task
def power(x, y):
    res = int(x) ** int(y)
    celery_log.info("Power %s + %s, res: %s" % (x, y, res))
    return res

@celery.task
def add_2(x, y):
    res = x + y
    celery_log.info("Adding %s + %s, res: %s" % (x, y, res))
    return res