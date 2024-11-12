#inclass code

import logging
import time
import  random
logger = logging.getLogger(__name__)

FORMAT = "[%(asctime)s][%(filename)s][%(levelname)s]%(msg)s"

def main():
    logging.basicConfig(filename='log.txt', level=logging.INFO, format=FORMAT)
    logger.info('Started')

    running = True
    while(running):
        random_integer = random.randint(0,3)
        if random_integer == 0:
            logger.error("Task Failed")
        elif random_integer == 1:
            logger.warning('Issue with task...')
        else:
            logger.info('Updated task...')
        
        time.sleep(1)
    
    logger.info('Finished')

if __name__ == '__main__':
    main()
