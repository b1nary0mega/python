#!/usr/bin/python

"""
FILE:   template.py
DATE:   DD-MON-YY
DESC:   Keep is short and sweet; don't write a manual!
"""
__author__ = "James R. Aylesworth"
__copyright__ = "Copyright 2022"
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "James R. Aylesworth"
__website__ = "https://b1nary0mega.github.io/"
__status__ = "Development"

import os
import sys
import logging


# MAIN
def main(logger, menu_option):

    if menu_option == "clear":
        os.system("cls")
    elif menu_option == "exit":
        os._exit(0)
    return


if __name__ == "__main__":

    # Logger - manual @ https://docs.python.org/3/library/logging.html
    logging.basicConfig(
        filename=sys.argv[0] + ".log",
        format="%(asctime)s - %(levelname)s [Line %(lineno)s] - %(message)s",
        filemode="a",
    )
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)  # debug, info, warning, error & critical

    logger.info("=== program started ===")

    # Welcome Message
    menu = "\nWelcome.."

    # Menu Options
    menu_options = ("clear", "exit")

    # Menu Loop
    while True:

        print(menu)

        for option in menu_options:
            print("[" + str(menu_options.index(option)) + "] : " + str(option))

        user_choice = input("\nEnter Choice (other to exit): ").strip()

        try:
            if menu_options[int(user_choice)] == "exit":
                break
            else:
                main(logger, menu_options[int(user_choice)])
                continue
        except:
            logger.debug("Exception caught")
            break

    logger.info("=== program exiting ===")
    sys.exit(0)
