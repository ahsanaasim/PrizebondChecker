from apscheduler.schedulers.background import BackgroundScheduler
import time

from Helpers.PrizebondChecker import PrizebondChecker
from Helpers.MailSender import MailSender
from dotenv import load_dotenv

load_dotenv()

def check():
  PrizebondChecker.check()

scheduler = BackgroundScheduler()
scheduler.add_job(check, 'interval', hours=12)
# scheduler.add_job(check, 'interval', seconds=15)
scheduler.start()

try:
    while True:
        time.sleep(2)
except (KeyboardInterrupt, SystemExit):
    scheduler.shutdown()