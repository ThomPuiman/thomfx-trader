import thomfx.config as cfg
import requests
from datetime import datetime as dt

def execute(action, params, method='GET'):
    url = cfg.API_BASE_URL + action
    req_headers = {
        'Authentication': 'Bearer %s' % cfg.OANDA_TOKEN
    }
    if method == 'GET':
        res = requests.get(url, params=params, headers=req_headers)
        return res.json()

def get_formatted_time(date=dt.now()):
    return date.strftime(cfg.OANDA_DATE_FORMAT)