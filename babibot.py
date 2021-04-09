import logging
import uci
import sys


def main():

    logging.basicConfig(filename='logs.txt', level=logging.INFO,
                        format='%(asctime)s %(message)s')

    logging.info('Babibot started')

    try:

        while True:
            msg = input()
            uci.command_received(msg)

    except Exception:
        logging.exception('Fatal error in main loop')


if __name__ == '__main__':
    main()
