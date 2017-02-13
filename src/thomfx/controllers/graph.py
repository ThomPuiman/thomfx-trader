import json
from thomfx.util.graph import GraphAbstract
from thomfx.util.graphs.candle_graph import CandleGraph
import sys
import pkgutil
class GraphController:
    def on_get(self, req, resp, graphType, instrument='EUR_USD'):
        candles = self.get_graph_type(graphType).retrieve_data(instrument)
        output = [[tick['time'], tick['openMid'], tick['highMid'], tick['lowMid'], tick['closeMid']] for tick in candles]
        resp.body = json.dumps(output)

    def get_graph_type(self, graphType) -> GraphAbstract:
        return {
            'candle': CandleGraph()
        }[graphType]