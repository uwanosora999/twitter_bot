from apscheduler.schedulers.blocking import BlockingScheduler
import bot

twische = BlockingScheduler()

@twische.scheduled_job('interval',minutes=1)
def timed_job():
    bot.puttweet()

if __name__ == "__main__":
    twische.start()