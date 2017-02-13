
import falcon
from waitress import serve
from thomfx.controllers import graph

class CorsMiddleware(object):

    def process_request(self, request, response):
        origin = request.get_header('Origin')
        response.set_header('Access-Control-Allow-Origin', 'http://')

falcon_api = falcon.API(middleware=[CorsMiddleware()])
falcon_api.add_route('/graph/{graphType}', graph.GraphController())
serve(falcon_api, host='', port=3333)