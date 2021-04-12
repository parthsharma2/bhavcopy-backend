import csv
import io
import zipfile

import redis
import requests
from bs4 import BeautifulSoup

from . import settings


def fetch_equity_data():
    redis_instance = redis.StrictRedis(
        host=settings.REDIS_HOST, port=settings.REDIS_PORT
    )

    bhavcopy_url = 'https://www.bseindia.com/markets/MarketInfo/BhavCopy.aspx'
    headers = {
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36'
    }

    page = requests.get(bhavcopy_url, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')

    zip_url = soup.find_all('table')[3].find('a').get('href')

    zip_response = requests.get(zip_url, headers=headers)
    with zipfile.ZipFile(io.BytesIO(zip_response.content)) as z:
        csv_filename = z.filelist[0].filename
        csv_str = z.read(csv_filename).decode()

        # flush all keys in Redis before adding new keys
        redis_instance.flushall()

        for record in csv.DictReader(io.StringIO(csv_str)):
            key = f'{record["SC_CODE"].strip()}{record["SC_NAME"].strip()}'
            value = {
                'code': record['SC_CODE'],
                'name': record['SC_NAME'],
                'open': record['OPEN'],
                'close': record['CLOSE'],
                'high': record['HIGH'],
                'low': record['LOW'],
            }

            redis_instance.hmset(key, value)
