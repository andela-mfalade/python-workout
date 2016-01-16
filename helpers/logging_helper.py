import logging


class LoggingHelper():
    logger = logging.getLogger(__file__)
    format = '[%(asctime)s] {%(pathname)s:%(lineno)d}' + \
        ' [%(levelname)s] - %(message)s'
    logging.basicConfig(
        format=format,
        level=logging.DEBUG,
        datefmt='%H:%M:%S'
    )

    def __init__(self):
        pass
