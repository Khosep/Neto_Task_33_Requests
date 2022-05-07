import requests
from datetime import datetime
import time

def stackoverflow_search(tags, days_ago):
    url = 'https://api.stackexchange.com/2.3/questions'
    to_date = int(time.time())
    from_date = to_date - days_ago*24*60*60
    page = 1
    counter = 0
    for p in range(1, 26):
        params = {'fromdate': from_date,
                  'todate': to_date,
                  'order': 'desc',
                  'sort': 'creation',
                  'tagged': tags,
                  'page': page,
                  'pagesize': 100,
                  'site': 'stackoverflow'
                  }
        res = requests.get(url, params=params).json()
        if res['items']:
            for item in res['items']:
                counter += 1
                print(f'#{counter} {datetime.utcfromtimestamp(item["creation_date"])}')
                print(item['title'])
                print(item['link'])
                print(item['tags'])
                print('___________________')
        else:
            break
        time.sleep(1)
        page += 1


stackoverflow_search(tags='python', days_ago=2)    # sample for multiple tags:  'python;pandas;dataframe'