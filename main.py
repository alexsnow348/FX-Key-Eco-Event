import requests as rq
import pandas as pd
import json
from datetime import datetime
import time


class API(object):
    """docstring for API."""

    def __init__(self, url):
        super(API, self).__init__()
        self.url = url
        request = rq.get(self.url)
        data = json.loads(request.text)
        self.data_df = pd.DataFrame(data)
        self.data_df = self.data_df.dropna(how='any', axis=0)

    def processData(self):

        self.data_df['timestamp_af'] = self.data_df['timestamp'].apply(
            lambda x: int(time.mktime(time.strptime(x, '%Y-%m-%d %H:%M:%S'))) - time.timezone)
        self.data_df['timestamp_af'] = self.data_df['timestamp_af'].apply(
            lambda x: time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(x)))
        print(self.data_df[['timestamp', 'timestamp_af']])


if __name__ == '__main__':
    url = 'https://eco-event.000webhostapp.com/'
    sample_call = API(url)
    sample_call.processData()
