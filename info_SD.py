import logging
import info_OD

logger=logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
file_format=logging.Formatter('%(asctime)s :%(filename)s :%(levelname)s :%(message)s')
file_name=logging.FileHandler("info_SD.log")
file_name.setFormatter(file_format)
logger.addHandler(file_name)

#logging.basicConfig(filename="info_SD.log",level=logging.DEBUG,format='%(asctime)s :%(filename)s :%(levelname)s :%(message)s')

ticket = int(input("Enter your ticket number which is ranging between 1 to 20000: "))
sales = int(input("Enter total sales amount: "))

if ticket <= 4000:
    dis=int(sales*0.30)
    dis_per="30%"
    print(f"Your ticket number is {ticket} and you will get discount of INR-{dis} {dis_per}-off on total sale.")
    logger.debug(f"Your ticket number is {ticket} and you will get discount of INR-{dis} {dis_per}-off on total sale.")
elif ticket <= 8000:
    dis=int(sales*0.25)
    dis_per="25%"
    print(f"Your ticket number is {ticket} and you will get discount of INR-{dis} {dis_per}-off on total sale.")
    logger.debug(f"Your ticket number is {ticket} and you will get discount of INR-{dis} {dis_per}-off on total sale.")
elif ticket <= 12000:
    dis=int(sales*0.20)
    dis_per="20%"
    print(f"Your ticket number is {ticket} and you will get discount of INR-{dis} {dis_per}-off on total sale.")
    logger.debug(f"Your ticket number is {ticket} and you will get discount of INR-{dis} {dis_per}-off on total sale.")
elif ticket <= 16000:
    dis=int(sales*0.15)
    dis_per="15%"
    print(f"Your ticket number is {ticket} and you will get discount of INR-{dis} {dis_per}-off on total sale.")
    logger.debug(f"Your ticket number is {ticket} and you will get discount of INR-{dis} {dis_per}-off on total sale.")
elif ticket <= 20000:
    dis=int(sales*0.10)
    dis_per="10%"
    print(f"Your ticket number is {ticket} and you will get discount of INR-{dis} {dis_per}-off on total sale.")
    logger.debug(f"Your ticket number is {ticket} and you will get discount of INR-{dis} {dis_per}-off on total sale.")
else:
    print(f"Your ticket number is wrong and there is no discount offer.")
    logger.debug("Your ticket number is wrong and there is no discount offer.")
