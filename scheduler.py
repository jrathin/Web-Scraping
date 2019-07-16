from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
from datetime import datetime
from currentData import start
from injury import injuryScrap
from test import prin

def scrap():
    start()

def injury():
    injuryScrap()

if __name__ == '__main__':
    sched = BackgroundScheduler()
    #sched.add_job(scrap, 'cron', minute='*/2', day_of_week=1)
    sched.add_job(scrap, 'cron', day_of_week='4-6', hour='*/3', end_date='2018-05-12')
    sched.add_job(injury, 'cron', hour=5, day_of_week=1)
    sched.start()
    
    #sched.shutdown();
