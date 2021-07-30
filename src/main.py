import time
import logging
import logging.config
from apscheduler.schedulers.background import BackgroundScheduler

from config import config as serviceConfig
from config import cron as cronConfig
from utils import common as commonUtils

schedulers = []
crons = [
    {
        "type": "interval", 
        "jobs": cronConfig.INTERAVL_CRON_JOBS
    }
]

def start_monitor():
    def startNewScheduler(jobs: list, job_type: str):
        s = BackgroundScheduler(timezone='MST', job_defaults=serviceConfig.CRON_SCHEDULES_CONFIG)
        for job in jobs:
            s.add_job(
                (commonUtils.get_lib_func_object(*commonUtils.get_cron_job(job['job'])).run), 
                job_type, 
                **job['time']
                )
            logging.info('Start [%s] Job'%(job['name']))
        schedulers.append(s)
    
    for cron in crons:
        startNewScheduler(cron['jobs'], cron['type'])
    
    for scheduler in schedulers:
        scheduler.start()

if __name__ == '__main__':
    logging.config.dictConfig(serviceConfig.LOG_CONFIG)
    start_monitor()

    logging.info("Monitor Starting. Done")

    # padding
    while True:
        try:
            time.sleep(86400)
        except KeyboardInterrupt:
            exit()