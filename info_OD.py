
import logging

logger=logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
file_format=logging.Formatter('%(asctime)s :%(filename)s :%(levelname)s :%(message)s')
file_name=logging.FileHandler("info_OD.log")
file_name.setFormatter(file_format)
logger.addHandler(file_name)

#logging.basicConfig(filename="info_OD.log",level=logging.DEBUG,format='%(asctime)s :%(filename)s :%(levelname)s :%(message)s')

VAR1 = int(input("Enter your ticket number which is ranging between 1 to 20000: "))

if VAR1 <= 4000:
    print(f"Your ticket number is {VAR1} and you will get discount offer up to limit 4K.")
    logger.debug(f"Ticket number was {VAR1} and discount given 4K.")
elif VAR1 <= 8000:
    print(f"Your ticket number is {VAR1} and you will get discount offer up to limit 8K.")
    logger.debug(f"Ticket number was {VAR1} and discount given 8K.")
elif VAR1 <= 12000:
    print(f"Your ticket number is {VAR1} and you will get discount offer up to limit 12K.")
    logger.debug(f"Ticket number was {VAR1} and discount given 12K.")
elif VAR1 <= 16000:
    print(f"Your ticket number is {VAR1} and you will get discount offer up to limit 16K.")
    logger.debug(f"Ticket number was {VAR1} and discount given 16K.")
elif VAR1 <= 20000:
    print(f"Your ticket number is {VAR1} and you will get discount offer up to limit 20K.")
    logger.debug(f"Ticket number was {VAR1} and discount given 20K.")
else:
    print(f"Your ticket number is wrong and there is no discount offer.")
    logger.debug("Your ticket number is wrong and there is no discount offer.")
