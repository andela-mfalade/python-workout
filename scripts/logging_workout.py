import logging
import sys

format = '[%(asctime)s] {%(pathname)s:%(lineno)d}' + \
    ' [%(levelname)s] - %(message)s'
logging.basicConfig(
    format=format,
    level=logging.DEBUG,
    datefmt='%H:%M:%S'
)
logger = logging.getLogger()


class CustomLogger(object):
    def __init__(self):
        logger.info("Initializing New Custom Logger.")

    def info(self, message):
        self.message = message
        logger.info("Message: %s", self.message)


def main():
    message = " Sorry I'm not hungry"
    new_log = CustomLogger()
    return new_log.info(message)

if __name__ == "__main__":
    sys.exit(main())
