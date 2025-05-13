# Check url.json's websites accessiability

import json
import urllib.request
from loguru import logger

# Read url.json
def check_main(json_path = "url.json"):
    try:
        with open(json_path, 'r', encoding = 'utf-8') as f:
            data: dict = json.load(f)
            return data
    except Exception as e:
        logger.error(f"Open url.json_Error {e}")

# Use urllib.request to test accessiablility
def check_every_url(url: dict):
    for _, value in url.items():
        s = urllib.request.Request(value)
        try:
            urllib.request.urlopen(s)
            return value
        except Exception as e:
            logger.error(f"Unaccessiable website: {value}, Error {e}")
            continue
    return None