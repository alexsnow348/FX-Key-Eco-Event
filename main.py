import requests as rq
import pandas as pd
import json
from datetime import datetime


class API(object):
    """docstring for API."""

    def __init__(self, url):
        super(API, self).__init__()
        self.url = url
        request = rq.get(self.url)
        data = json.loads(request.text)
        self.data_df = pd.DataFrame(data)

    def processData(self):
        print(self.data_df['data'])


if __name__ == '__main__':
    url = 'https://ecocalendar.000webhostapp.com/api/'
    sample_call = API(url)
    sample_call.processData()
