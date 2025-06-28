from celery import Celery
import os

app = Celery('tasks',
             broker='redis://localhost:6379/0',
             backend='redis://localhost:6379/0',
             include=['main'])

# Optional configuration
app.conf.update(
    result_expires=3600,
)

if __name__ == '__main__':
    app.start()
