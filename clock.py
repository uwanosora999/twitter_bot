from apscheduler.schedulers.blocking import BlockingScheduler
import bot
import subprocess
import os

twische = BlockingScheduler()

@twische.scheduled_job('interval',minutes=1)
def timed_job():
    bot.tweet()
    bot.reply()

@twische.scheduled_job('interval',minutes=30)
def requests():
    app_name = os.environ["APP_NAME"]
    cmd = 'curl http://{}.herokuapp.com/'.format(app_name)
    subprocess.Popen(cmd.split())

if __name__ == "__main__":
    twische.start()
