from apscheduler.schedulers.blocking import BlockingScheduler
import bot

twische = BlockingScheduler()

@twische.scheduled_job('interval',minutes=60)
def timed_job():
    bot.tweet()
    bot.reply()

if __name__ == "__main__":
    twische.start()