from datetime import datetime
import logging
import time
import webbrowser


logger = logging.getLogger(__file__)
format = '[%(asctime)s] {%(pathname)s:%(lineno)d}' + \
    ' [%(levelname)s] - %(message)s'
logging.basicConfig(
    format=format,
    level=logging.DEBUG,
    datefmt='%H:%M:%S'
)


class BreakTime:
    def __init__(self, allowance=None, playground=None):
        self.num_breaks = 0
        self.allowed_daily_breaks = allowance
        self.playground = playground

    def start(self):
        while self.num_breaks < self.allowed_daily_breaks:
            current_time = datetime.now()
            logger.info('The time is %s', str(current_time))
            logger.info("Your next break is in 1 hour. Enjoy!")
            time.sleep(3600)
            logger.info("Opening url: %s", self.playground)
            webbrowser.open(self.playground)
            self.num_breaks += 1


def main():
    logger.info("Starting Script")
    allowance = 3
    playground = 'https://www.facebook.com/'
    logger.info("Creating new instance of BreakTime")
    break_time = BreakTime(allowance=allowance, playground=playground)
    break_time.start()

if __name__ == '__main__':
    main()
