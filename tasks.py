import os
import time
from sentiments import getSentimentScores
from celery import Celery

host = os.environ['UPSTASH_REDIS_HOST']
password = os.environ['UPSTASH_REDIS_PASSWORD']
port = os.environ['UPSTASH_REDIS_PORT']
connection_link = "rediss://:{}@{}:{}?ssl_cert_reqs=CERT_REQUIRED".format(
    password, host, port)

celery = Celery('tasks', backend=connection_link,
                broker=connection_link, result_expires=60 * 60 * 16)


@celery.task(name='tasks.sentiment_scores')
def processTask(comments, videoId):
  result = getSentimentScores(comments, videoId)
  return result
