import os
import datetime
import json
from apscheduler.schedulers.background import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger

class Crontab:
    def __init__(self):
        with open('settings.path.crontab', 'r', encoding = 'utf-8') as f1:
            crontab_path = f1.read()
        with open(crontab_path, 'r', encoding = 'utf-8') as f2:
            self.data_sources = json.loads(f2.read())

    def get_crontab_property(self, key):
        return self.data_sources[key]


def daily_job():
    print('%s ready to run script...' % (datetime.datetime.now()))
    with open('settings.path.properties', 'r', encoding = 'utf-8') as f1:
        properties_path = f1.read()
    with open(properties_path, 'r', encoding = 'utf-8') as f2:
        print('%s start running script...' % (datetime.datetime.now()))
        for command in f2.readlines():
            os.system(command)
        print('%s successfully running script.' % (datetime.datetime.now()))

if __name__ == "__main__":
    # 建立排程物件
    scheduler = BlockingScheduler()

    # 排程設定class
    crontab = Crontab()
    # 取的小時設定檔
    hour = crontab.get_crontab_property('hour')
    # 取的分鐘設定檔
    minute = crontab.get_crontab_property('minute')

    # 使用cronTab方式設定作業時間
    cronTrigger = CronTrigger(hour = hour, minute = minute)

    # 設定排程工作
    scheduler.add_job(daily_job, cronTrigger, id='daily_job_id')

    # 執行排程工作
    scheduler.start()