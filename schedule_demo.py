import schedule
import time


def schedule_job():
    print("Schedule job is working......")

def main():
    schedule.every(10).seconds.do(schedule_job)
    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == '__main__':
    main()