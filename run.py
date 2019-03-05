import logging
import json
import os

from api.questrade import QTClient

logging.basicConfig(level=logging.INFO,
                        format="[%(asctime)s:%(levelname)s:%(filename)s:%(lineno)s - %(funcName)20s() ] %(message)s",
                        handlers=[logging.FileHandler("finances.log"),
                                  logging.StreamHandler()])

REFRESH_TOKEN = ""

if __name__ == '__main__':
    logging.info("Connecting to Questrdate")
    client = QTClient(REFRESH_TOKEN)
    logging.info("Connected to Questrade")