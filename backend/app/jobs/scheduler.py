from apscheduler.schedulers.background import BackgroundScheduler


def sample_job():
    print("scheduler: sample job running")


def start_scheduler():
    scheduler = BackgroundScheduler()
    scheduler.add_job(sample_job, "interval", seconds=60)
    scheduler.start()
