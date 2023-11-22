import logging

logging.basicConfig(filename="OfferDiscount.log",level=logging.DEBUG,format='%(asctime)s :%(filename)s :%(levelname)s :%(message)s')

VAR1 = int(input("Enter your ticket number which is ranging between 1 to 20000: "))

if VAR1 <= 4000:
    print(f"Your ticket number is {VAR1} and you will get discount offer up to limit 4K.")
    logging.debug(f"Ticket number was {VAR1} and discount given 4K.")
elif VAR1 <= 8000:
    print(f"Your ticket number is {VAR1} and you will get discount offer up to limit 8K.")
    logging.debug(f"Ticket number was {VAR1} and discount given 8K.")
elif VAR1 <= 12000:
    print(f"Your ticket number is {VAR1} and you will get discount offer up to limit 12K.")
    logging.debug(f"Ticket number was {VAR1} and discount given 12K.")
elif VAR1 <= 16000:
    print(f"Your ticket number is {VAR1} and you will get discount offer up to limit 16K.")
    logging.debug(f"Ticket number was {VAR1} and discount given 16K.")
elif VAR1 <= 20000:
    print(f"Your ticket number is {VAR1} and you will get discount offer up to limit 20K.")
    logging.debug(f"Ticket number was {VAR1} and discount given 20K.")
else:
    print(f"Your ticket number is wrong and there is no discount offer.")
    logging.debug("Your ticket number is wrong and there is no discount offer.")
