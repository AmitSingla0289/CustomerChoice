from crontab import CronTab
from datetime import datetime

def cronJob(time,week,day,hour,noOfTimes):
    cron = CronTab(user =True)
    cron.remove_all()
    job = cron.new( command = 'python ApplicationController.py')
    job.hour.every('3')
    Cron().schedule(
        # Turn off logging for job that runs every five seconds
        Tab(name='my_fast_job', verbose=False).every(seconds=5).run(my_job, 'fast', seconds=5),
    #job.minute.every(1)
    for item in cron:
        print( item);
    cron.write()