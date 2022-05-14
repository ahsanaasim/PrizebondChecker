from apscheduler.schedulers.background import BackgroundScheduler
import time

from Helpers.PrizebondChecker import PrizebondChecker

def check():
  PrizebondChecker.check()

scheduler = BackgroundScheduler()
scheduler.add_job(check, 'interval', hours=12)
scheduler.start()

try:
    while True:
        time.sleep(2)
except (KeyboardInterrupt, SystemExit):
    scheduler.shutdown()