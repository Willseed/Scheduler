import os
import time
import json
from apscheduler.schedulers.background import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger

class Crontab:
    def __init__(self):
        with open('settings.path.crontab', 'r', encoding = 'utf-8') as f1:
            crontab_path = f1.read()
        with open(crontab_path, 'r', encoding = 'utf-8') as f2:
            self.data_sources = json.loads(f2.read())

    def getCrontabProperty(self, key):
        dataSource = self.data_sources[key]
        return dataSource


def daily_job():
    with open('settings.path.properties', 'r', encoding = 'utf-8') as f1:
        properties_path = f1.read()
    with open(properties_path, 'r', encoding = 'utf-8') as f2:
        for line in f2.readlines():
            os.system(line)

if __name__ == "__main__":
    # 建立排程物件
    scheduler = BlockingScheduler()

    # 排程設定class
    crontab = Crontab()
    # 取的小時設定檔
    hour = crontab.getCrontabProperty('hour')
    # 取的分鐘設定檔
    minute = crontab.getCrontabProperty('minute')

    # 使用cronTab方式設定作業時間
    cronTrigger = CronTrigger(hour = hour, minute = minute)

    # 設定排程工作
    scheduler.add_job(daily_job, cronTrigger, id='daily_job_id')

    # 執行排程工作
    scheduler.start()