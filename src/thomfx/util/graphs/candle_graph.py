from thomfx.util.graph import GraphAbstract
from thomfx.util import api
from datetime import datetime, timedelta

class CandleGraph(GraphAbstract):

    def retrieve_data(self, instrument):
        start = api.get_formatted_time(datetime.today().replace(hour=0,minute=0,second=0))
        end = api.get_formatted_time(datetime.today().replace(hour=0,minute=0,second=0) + timedelta(days=1))
      
        res = api.execute('candles', {
            'instrument': instrument,
            'granularity': 'M15',
            'candleFormat': 'midpoint',
            'dailyAlignment': '0',
            'start': start,
            'end': end
        })

        if 'candles' in res:
            return res['candles']
        elif 'message' in res:
            print('ERROR: ', res['message'])
            return []
        else:
            return []
