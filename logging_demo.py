import logging
import time


def init_logger():
    logging.basicConfig(filename='app_log.log', level=logging.DEBUG)


if __name__ == '__main__':
    init_logger()
    start_time = time.time()
    logging.debug('A debug message')
    logging.info('An info message')
    logging.warning('A warning message')
    logging.error('An error message')
    time.sleep(2)
    end_time = time.time()
    execution_time = end_time - start_time
    logging.info("execution_time: %.2f", execution_time)
