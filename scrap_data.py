import requests as rq
import pandas as pd
import json
from datetime import datetime

url = 'https://sslecal2.forexprostools.com/'

request = rq.get(url)
print(request.text)
